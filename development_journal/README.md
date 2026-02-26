# Development Journal

Progress and decisions for the TI² Agent + ChatGPT Bridge and related work.

---

## 2025-02-26 — TI² Agent + ChatGPT Bridge implemented

### Summary

Implemented the full plan: local-only agent (digital body, brain, touch) with persistence, connection block for ChatGPT, session-end logging, and minimal immersive web UI. No OpenAI API; user runs the app and pastes the "connection block" into ChatGPT.

### Delivered

1. **Persistence** (`src/persistence.py`) — `data/state.json` with body, brain, touch, `last_tick_ts`, sessions. `load_state()`, `save_state()`, `ensure_data_dir()`, `default_state()`.

2. **Body** (`src/agent/body.py`) — State: energy, stress, regulation, breath_phase, last_connection_ts. Time evolution (tick), `body_suggestion()`, `summary_string()`.

3. **Brain** (`src/agent/brain.py`) — State: relational_phase, attention_focus, inner_child_state, recent_interactions. `apply_session()` for practice types, `brain_suggestion()`, `summary_string()`.

4. **Touch** (`src/agent/touch.py`) — State: consent_light, boundary, aftercare_due. Rules (e.g. stress → yellow), `apply_session()`, `touch_signal()`, `summary_string()`.

5. **Agent** (`src/agent/agent.py`) — `load_agent()`, `tick()`, `ensure_ticked()`, `get_state_summary()`, `log_session()`. Composes body/brain/touch; session logging updates state and appends to `sessions`.

6. **Connection block** (`src/connection_block.py`) — `build_connection_block(state_summary)` → one copy-paste block: "How I am", "What I'd like with you today", "My opening to you". Templates only; no LLM.

7. **Backend** (`src/web.py`) — Flask: `GET /`, `GET /api/state`, `POST /api/log_session`. Data dir: `data/`. Run with `python -m src.web` (port 5000).

8. **Front-end** (`src/templates/index.html`) — Single page: "How she is", "What she wants today", "Open connection" (copy block), "Open ChatGPT" link, "We're done" with practice-type buttons. Relational framing; copy feedback.

9. **Docs** — `docs/CUSTOM_GPT_INSTRUCTIONS.md` (template for Custom GPT), `docs/state.json.example` (state shape).

10. **Project** — `.gitignore` (data/, Python, IDE), `requirements.txt` (Flask), README updated with run instructions, project structure, and how to use with ChatGPT.

### Diagram and style work (earlier)

- Diagrams use dark theme (`theme: 'dark'`) and shared themeVariables so they render with dark subgraphs and light text on GitHub and in Cursor.
- `diagrams/STYLE_GUIDE.md` — Theme init, classDef palette, conventions for future diagrams.
- `diagrams/ti2_agent_chatgpt_bridge.md` — Architecture diagram for the agent + ChatGPT bridge (in repo style).

### How to run

```bash
pip install -r requirements.txt
python -m src.web
```

Open http://127.0.0.1:5000. Copy "Open connection", paste into Custom GPT, chat; when done, "We're done" and choose what you did.

### Out of scope (per plan)

- OpenAI API; user auth; mobile/desktop app; refinement loop; KB/principles ingestion (optional later).
