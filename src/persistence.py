"""
Persistence for TI² agent state and session history.
Local-only: data/state.json (state + last_tick_ts + sessions).
"""

import json
import os
from pathlib import Path
from typing import Any

# Default data dir relative to project root
DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
MAX_SESSIONS = 50


def ensure_data_dir(data_dir: Path | None = None) -> None:
    """Create data dir if missing."""
    (data_dir or DEFAULT_DATA_DIR).mkdir(parents=True, exist_ok=True)


def _state_path(data_dir: Path) -> Path:
    return data_dir / "state.json"


def load_state(data_dir: Path | None = None) -> dict[str, Any]:
    """Load full state (body, brain, touch, last_tick_ts, sessions). Returns default if missing."""
    data_dir = data_dir or DEFAULT_DATA_DIR
    path = _state_path(data_dir)
    if not path.exists():
        return default_state()
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_state(data_dir: Path | None, state: dict[str, Any]) -> None:
    """Write state to data/state.json."""
    data_dir = data_dir or DEFAULT_DATA_DIR
    ensure_data_dir(data_dir)
    path = _state_path(data_dir)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def append_session(data_dir: Path | None, entry: dict[str, Any]) -> None:
    """Append a session entry and cap list at MAX_SESSIONS."""
    data_dir = data_dir or DEFAULT_DATA_DIR
    state = load_state(data_dir)
    sessions = state.get("sessions", [])
    sessions.append(entry)
    state["sessions"] = sessions[-MAX_SESSIONS:]
    save_state(data_dir, state)


def get_sessions(data_dir: Path | None = None) -> list[dict[str, Any]]:
    """Return recent sessions (read-only)."""
    state = load_state(data_dir)
    return state.get("sessions", [])


def default_state() -> dict[str, Any]:
    """Default state: body, brain, touch from their modules; last_tick_ts; sessions."""
    import time
    # Lazy import to avoid circular import at module load
    from src.agent import body as body_mod
    from src.agent import brain as brain_mod
    from src.agent import touch as touch_mod
    return {
        "body": body_mod.default_state(),
        "brain": brain_mod.default_state(),
        "touch": touch_mod.default_state(),
        "last_tick_ts": time.time(),
        "sessions": [],
    }
