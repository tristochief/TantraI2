"""
Digital Body: energy, stress, regulation, breath phase, last_connection_ts.
Time evolution (tick), body_suggestion(), human summary.
"""

import time
from typing import Literal

# Breath phase cycle length in seconds (per phase: inhale/hold/exhale/rest)
BREATH_PHASE_SEC = 4.0
STRESS_DECAY_PER_SEC = 0.02
ENERGY_DECAY_PER_SEC = 0.01
REGULATION_RISE_PER_SEC = 0.015

BodySuggestion = Literal[
    "co_regulation", "breath_sync", "grounding", "aftercare", "gentle_connection"
]


def default_state() -> dict:
    return {
        "energy": 0.7,
        "stress": 0.3,
        "regulation": 0.6,
        "breath_phase": 0.0,
        "last_connection_ts": time.time(),
    }


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def tick(state: dict, elapsed_seconds: float) -> None:
    """Update body state over time: decay stress, optional energy decay, advance breath."""
    state["stress"] = clamp(state["stress"] - STRESS_DECAY_PER_SEC * elapsed_seconds)
    state["energy"] = clamp(state["energy"] - ENERGY_DECAY_PER_SEC * elapsed_seconds)
    state["regulation"] = clamp(state["regulation"] + REGULATION_RISE_PER_SEC * elapsed_seconds)
    # Breath phase cycles 0 -> 1 -> 2 -> 3 -> 0 (inhale, hold, exhale, rest)
    phase_delta = elapsed_seconds / BREATH_PHASE_SEC
    state["breath_phase"] = (state.get("breath_phase", 0) + phase_delta) % 4.0


def body_suggestion(state: dict) -> BodySuggestion:
    """Suggest what the body wants from current state."""
    stress = state.get("stress", 0.5)
    regulation = state.get("regulation", 0.5)
    energy = state.get("energy", 0.5)
    if stress > 0.6:
        return "grounding"
    if regulation < 0.4:
        return "co_regulation"
    if energy < 0.3:
        return "gentle_connection"
    return "breath_sync"


def summary_string(state: dict) -> str:
    """Short human summary for 'How she is'."""
    energy = state.get("energy", 0.5)
    stress = state.get("stress", 0.5)
    suggestion = body_suggestion(state)
    energy_desc = "low" if energy < 0.4 else "steady" if energy < 0.7 else "good"
    stress_desc = "coming down" if stress < 0.5 else "elevated"
    return f"Body: {energy_desc} energy, stress {stress_desc}, wants {suggestion.replace('_', ' ')}."
