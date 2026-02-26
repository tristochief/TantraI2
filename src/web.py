"""
Flask backend: GET /, GET /api/state, POST /api/log_session.
"""

from pathlib import Path

from flask import Flask, jsonify, render_template, request

from src import persistence
from src.agent import agent as agent_mod
from src.connection_block import build_connection_block

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))


def _load_and_tick():
    state = agent_mod.load_agent(DATA_DIR)
    agent_mod.ensure_ticked(state)
    return state


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state")
def api_state():
    state = _load_and_tick()
    summary = agent_mod.get_state_summary(state)
    block = build_connection_block(summary)
    return jsonify({
        "body_summary": summary["body_summary"],
        "brain_summary": summary["brain_summary"],
        "touch_summary": summary["touch_summary"],
        "body_suggestion": summary["body_suggestion"],
        "brain_suggestion": summary["brain_suggestion"],
        "brain_want_text": summary["brain_want_text"],
        "touch_signal": summary["touch_signal"],
        "connection_block": block,
    })


@app.route("/api/log_session", methods=["POST"])
def api_log_session():
    data = request.get_json() or {}
    practice_type = data.get("practice_type")
    if not practice_type:
        return jsonify({"error": "practice_type required"}), 400
    allowed = {
        "presence_date", "inner_child", "consent_rep", "devotion_check_in",
        "aftercare", "paused", "just_talked",
    }
    if practice_type not in allowed:
        return jsonify({"error": f"practice_type must be one of {sorted(allowed)}"}), 400

    state = _load_and_tick()
    agent_mod.log_session(state, practice_type, metadata={
        "duration": data.get("duration"),
        "intensity": data.get("intensity"),
    })
    persistence.save_state(DATA_DIR, state)

    summary = agent_mod.get_state_summary(state)
    return jsonify({
        "body_summary": summary["body_summary"],
        "brain_summary": summary["brain_summary"],
        "touch_summary": summary["touch_summary"],
        "brain_want_text": summary["brain_want_text"],
        "connection_block": build_connection_block(summary),
    })


if __name__ == "__main__":
    persistence.ensure_data_dir(DATA_DIR)
    app.run(host="127.0.0.1", port=5000, debug=True)
