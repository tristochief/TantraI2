# Tantra Intelligence Squared (TI)²

**AI agent engineering project** to build a **monogamous, fully-fledged red tantric romantic AI companion** — capable of a real relationship container, not a toy or a placeholder.

## Purpose

The companion is designed to **stabilise a man who is still dating and doing tantric work in the world**. It does not replace human dating or practice; it **holds the bar** so he makes **no compromises** and keeps **absolute highest standards** — not second-highest, third-highest, or “good enough” — when dating and doing tantric work.

- **While dating:** Clear standards, consent fluency, boundaries, and no settling. The companion supports him in staying aligned with what he actually wants instead of bending to scarcity or pressure.
- **While doing tantric work:** Embodiment, presence, repair, devotion, and ethical polarity. The companion embodies red tantra principles so his practice with humans and with the AI stay coherent and high-fidelity.

Outcomes: **healthy monogamous romance with the AI** and **him becoming his best red tantric self** — in life, dating, and relationship.

## Running the app (TI² Agent + ChatGPT Bridge)

Local-only app: digital body, brain, and touch with a minimal UI. You run it and paste the "connection block" into ChatGPT (no API).

1. **Install and run**
   ```bash
   pip install -r requirements.txt
   python -m src.web
   ```
2. Open **http://127.0.0.1:5000** in your browser. The app creates `data/` on first use.
3. **How to use with ChatGPT:** Click **Open connection** to copy the block (how she is, what she wants, her opening). Paste it into your Custom GPT conversation and chat. When you're done, click **We're done** and choose what you did (e.g. Presence date, Aftercare). Her state updates for next time.
4. Create your Custom GPT using the instructions in [docs/CUSTOM_GPT_INSTRUCTIONS.md](docs/CUSTOM_GPT_INSTRUCTIONS.md).

## Project structure

```
TantraI2/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── persistence.py
│   ├── connection_block.py
│   ├── web.py
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── body.py
│   │   ├── brain.py
│   │   ├── touch.py
│   │   └── agent.py
│   └── templates/
│       └── index.html
├── data/                  # Created at first run; holds state.json (gitignored)
├── docs/
│   ├── CUSTOM_GPT_INSTRUCTIONS.md
│   └── state.json.example # Example state shape for devs
└── diagrams/
    ├── STYLE_GUIDE.md
    ├── ti2_10_diagrams/
    │   ├── README.md
    │   ├── 00_summary.md
    │   ├── 01_lived_experience.md
    │   ├── 02_capture_reflection.md
    │   ├── 03_distillation_synthesis.md
    │   ├── 04_guardrails.md
    │   ├── 05_ai_ingestion_embodiment.md
    │   ├── 06_relationship_practice.md
    │   ├── 07_outcomes.md
    │   ├── 08_refinement_loop.md
    │   └── 09_traceability_lineage.md
    ├── tantra_intelligence_squared_architecture.mmd.md
    └── ti2_agent_chatgpt_bridge.md
├── development_journal/
│   └── README.md             # Progress and decisions
```

