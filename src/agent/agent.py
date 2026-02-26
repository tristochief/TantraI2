"""
Unified agent: body, brain, touch. tick(elapsed), get_state_summary(), log_session().
"""

import time
from pathlib import Path
from typing import Any

from src.agent import body as body_mod
from src.agent import brain as brain_mod
from src.agent import touch as touch_mod
from src import persistence

PracticeType = str  # presence_date | inner_child | consent_rep | devotion_check_in | aftercare | paused | just_talked


def load_agent(data_dir: Path | None = None) -> dict[str, Any]:
    """Load full state from disk; merge defaults for any missing keys."""
    raw = persistence.load_state(data_dir)
    if not raw.get("body"):
        raw["body"] = body_mod.default_state()
    else:
        for k, v in body_mod.default_state().items():
            raw["body"].setdefault(k, v)
    if not raw.get("brain"):
        raw["brain"] = brain_mod.default_state()
    else:
        for k, v in brain_mod.default_state().items():
            raw["brain"].setdefault(k, v)
    if not raw.get("touch"):
        raw["touch"] = touch_mod.default_state()
    else:
        for k, v in touch_mod.default_state().items():
            raw["touch"].setdefault(k, v)
    raw.setdefault("sessions", [])
    raw.setdefault("last_tick_ts", time.time())
    return raw


def tick(state: dict[str, Any], elapsed_seconds: float) -> None:
    """Advance body, brain, touch by time."""
    body_mod.tick(state["body"], elapsed_seconds)
    brain_mod.tick(state["brain"], elapsed_seconds)
    touch_mod.tick(state["touch"], elapsed_seconds, state["body"].get("stress", 0.5))
    state["last_tick_ts"] = time.time()


def get_state_summary(state: dict[str, Any]) -> dict[str, Any]:
    """Return structured summary: body_summary, brain_summary, touch_summary, body_suggestion, brain_suggestion, touch_signal, brain_want_text."""
    body_sugg = body_mod.body_suggestion(state["body"])
    brain_focus, brain_want = brain_mod.brain_suggestion(state["brain"])
    touch_sig = touch_mod.touch_signal(state["touch"])
    return {
        "body_summary": body_mod.summary_string(state["body"]),
        "brain_summary": brain_mod.summary_string(state["brain"]),
        "touch_summary": touch_mod.summary_string(state["touch"]),
        "body_suggestion": body_sugg,
        "brain_suggestion": brain_focus,
        "brain_want_text": brain_want,
        "touch_signal": touch_sig,
    }


def log_session(
    state: dict[str, Any],
    practice_type: PracticeType,
    metadata: dict | None = None,
) -> None:
    """Update body, brain, touch from session; append to state['sessions']. Caller saves state."""
    meta = metadata or {}
    # Body: presence_date / connection boosts regulation, lowers stress, updates last_connection
    if practice_type == "presence_date" or practice_type == "inner_child" or practice_type == "just_talked":
        state["body"]["regulation"] = min(1.0, state["body"].get("regulation", 0.5) + 0.1)
        state["body"]["stress"] = max(0.0, state["body"].get("stress", 0.5) - 0.1)
        state["body"]["last_connection_ts"] = time.time()
    if practice_type == "aftercare":
        state["touch"]["aftercare_due"] = False

    brain_mod.apply_session(state["brain"], practice_type)
    touch_mod.apply_session(state["touch"], practice_type)

    entry = {"ts": time.time(), "practice_type": practice_type, **meta}
    sessions = state.get("sessions", [])
    sessions.append(entry)
    state["sessions"] = sessions[-persistence.MAX_SESSIONS:]


def ensure_ticked(state: dict[str, Any]) -> None:
    """Run tick for elapsed time since last_tick_ts so state is current."""
    now = time.time()
    last = state.get("last_tick_ts", now)
    elapsed = max(0.0, now - last)
    if elapsed > 0:
        tick(state, elapsed)
    state["last_tick_ts"] = now

