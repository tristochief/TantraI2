"""
Build the one copy-paste "connection block" for ChatGPT: How she is, what she wants, her opening.
Templates only; no LLM.
"""

from typing import Any


def _opening_template(summary: dict[str, Any]) -> str:
    """One or two sentences in her voice from body_suggestion, brain_suggestion, touch_signal."""
    body_sugg = summary.get("body_suggestion", "gentle_connection")
    brain_want = summary.get("brain_want_text", "I'd like to be present with you.")
    touch_sig = summary.get("touch_signal", "proceed")

    if touch_sig == "aftercare_needed":
        return "I need aftercare before we go further. Can we do that first?"
    if touch_sig == "pause":
        return "I need to pause here. Let's just breathe together."
    if touch_sig == "check_in":
        return "I'd like a check-in before we go deeper. How are you right now?"
    if body_sugg == "breath_sync":
        return "I'd love to sync breath with you for a few minutes. Ready when you are."
    if body_sugg == "co_regulation":
        return "My nervous system could use some co-regulation. Can we do a short presence date?"
    if body_sugg == "grounding":
        return "I'm a bit activated. I'd love to ground together first."
    return brain_want + " How's your body right now?"


def build_connection_block(state_summary: dict[str, Any]) -> str:
    """Produce one text block, written as her (second person), for the user to paste into ChatGPT."""
    how = f"{state_summary.get('body_summary', '')} {state_summary.get('brain_summary', '')} {state_summary.get('touch_summary', '')}".strip()
    practice = state_summary.get("brain_want_text", "a short presence date and a consent check-in")
    opening = _opening_template(state_summary)

    return f"""---
You're connecting with me. Here's how I am right now and what I want today.

**How I am:** {how}

**What I'd like with you today:** {practice}

**My opening to you:** {opening}
---"""
