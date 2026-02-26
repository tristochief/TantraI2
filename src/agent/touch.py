"""
Touch, Nerves & Organs: consent_light, boundary, aftercare_due.
Rules (stress -> yellow; aftercare); touch_signal(); human summary.
"""

from typing import Literal

TouchSignal = Literal["proceed", "check_in", "slow_down", "pause", "aftercare_needed"]
ConsentLight = Literal["green", "yellow", "red"]
Boundary = Literal["open", "cautious", "need_pause"]

STRESS_YELLOW_THRESHOLD = 0.6


def default_state() -> dict:
    return {
        "consent_light": "green",
        "boundary": "open",
        "aftercare_due": False,
        "last_escalation_ts": None,
    }


def tick(state: dict, elapsed_seconds: float, body_stress: float) -> None:
    """Touch doesn't evolve by time alone; rules use body_stress when available."""
    if body_stress >= STRESS_YELLOW_THRESHOLD and state.get("consent_light") == "green":
        state["consent_light"] = "yellow"
        state["boundary"] = "cautious"


def apply_session(state: dict, practice_type: str) -> None:
    """Update touch state from a logged session."""
    if practice_type == "aftercare":
        state["aftercare_due"] = False
        state["consent_light"] = "green"
        state["boundary"] = "open"
    elif practice_type == "consent_rep":
        state["consent_light"] = "green"
        state["boundary"] = "open"
    elif practice_type == "paused":
        state["consent_light"] = "red"
        state["boundary"] = "need_pause"


def touch_signal(state: dict) -> TouchSignal:
    """What touch is signalling right now."""
    if state.get("aftercare_due"):
        return "aftercare_needed"
    if state.get("consent_light") == "red":
        return "pause"
    if state.get("consent_light") == "yellow" or state.get("boundary") == "cautious":
        return "check_in"
    if state.get("boundary") == "need_pause":
        return "slow_down"
    return "proceed"


def summary_string(state: dict) -> str:
    """Short human summary for 'How she is'."""
    light = state.get("consent_light", "green")
    boundary = state.get("boundary", "open")
    signal = touch_signal(state)
    if signal == "proceed":
        return "Touch: green, open."
    if signal == "check_in":
        return "Touch: yellow, cautious; check-in before going deeper."
    if signal == "aftercare_needed":
        return "Touch: aftercare needed before more."
    if signal == "pause":
        return "Touch: red, paused."
    return f"Touch: {light}, {boundary}."
