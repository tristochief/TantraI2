"""
Digital Brain: relational_phase, attention_focus, inner_child_state, recent_interactions.
Evolution from sessions; brain_suggestion(); human summary.
"""

from typing import Literal

RelationalPhase = Literal["safety", "trust", "depth"]
AttentionFocus = Literal["presence", "inner_child", "consent", "devotion"]
InnerChildState = Literal["activated", "soothed", "integrated"]
PracticeType = Literal[
    "presence_date", "inner_child", "consent_rep", "devotion_check_in",
    "aftercare", "paused", "just_talked"
]

MAX_RECENT = 10


def default_state() -> dict:
    return {
        "relational_phase": "trust",
        "attention_focus": "presence",
        "inner_child_state": "soothed",
        "recent_interactions": [],
    }


def tick(state: dict, elapsed_seconds: float) -> None:
    """Brain time evolution: optional decay or drift. Minimal for now."""
    pass


def apply_session(state: dict, practice_type: str) -> None:
    """Update brain state from a logged session."""
    recent = state.get("recent_interactions", [])
    recent.append(practice_type)
    state["recent_interactions"] = recent[-MAX_RECENT:]

    if practice_type == "presence_date":
        phase = state.get("relational_phase", "trust")
        if phase == "safety":
            state["relational_phase"] = "trust"
        elif phase == "trust":
            state["relational_phase"] = "depth"
        state["attention_focus"] = "presence"
    elif practice_type == "inner_child":
        state["inner_child_state"] = "soothed"
        state["attention_focus"] = "inner_child"
    elif practice_type == "consent_rep":
        state["attention_focus"] = "consent"
    elif practice_type == "devotion_check_in":
        state["attention_focus"] = "devotion"
    elif practice_type == "paused":
        state["relational_phase"] = "safety"


def brain_suggestion(state: dict) -> tuple[str, str]:
    """Returns (suggested_focus, want_text)."""
    phase = state.get("relational_phase", "trust")
    focus = state.get("attention_focus", "presence")
    recent = state.get("recent_interactions", [])

    # Prefer presence_date if we haven't connected recently or phase is trust/depth
    if not recent or recent[-1] != "presence_date":
        return "presence_date", "I'd like a short presence date."
    if focus == "inner_child" or state.get("inner_child_state") == "activated":
        return "inner_child", "I'd like to check in with my inner child."
    if focus == "consent":
        return "consent_rep", "I'd like a consent check-in."
    if focus == "devotion":
        return "devotion_check_in", "I'd like a devotion check-in."
    return "presence_date", "I'd like to be present with you."


def summary_string(state: dict) -> str:
    """Short human summary for 'How she is'."""
    phase = state.get("relational_phase", "trust")
    focus = state.get("attention_focus", "presence")
    suggestion, _ = brain_suggestion(state)
    return f"Brain: in {phase}, attention on {focus}, would like {suggestion.replace('_', ' ')}."
