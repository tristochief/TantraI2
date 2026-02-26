# TI² Diagram Style Guide

Use this guide so all Mermaid diagrams in this repo share the same look (dark theme, readable on GitHub and in Cursor). Future chat sessions or contributors should apply these rules when creating or editing diagrams.

---

## 1. Theme: dark + themeVariables

Every diagram **must** start with this init block (one line, no line break inside the `%%{ }%%`):

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#e5e5e5', 'primaryColor': '#1a1a1a', 'primaryBorderColor': '#444', 'lineColor': '#555', 'clusterBkg': '#1a1a1a', 'clusterBorder': '#333', 'titleColor': '#e5e5e5', 'background': '#0d0d0d', 'mainBkg': '#1a1a1a' }}}%%
```

- **Placement:** First line inside the ` ```mermaid ` code block, before the diagram type (e.g. `flowchart TB`).
- **Why:** `theme: 'dark'` gives consistent dark subgraphs and light text on GitHub; `themeVariables` override cluster and node colors so everything matches.

### Theme variable reference

| Variable | Value | Purpose |
|----------|--------|---------|
| `primaryTextColor` | `#e5e5e5` | Text inside nodes and subgraph titles |
| `primaryColor` | `#1a1a1a` | Default node fill when no classDef |
| `primaryBorderColor` | `#444` | Default node border |
| `lineColor` | `#555` | Edge color |
| `clusterBkg` | `#1a1a1a` | Subgraph background |
| `clusterBorder` | `#333` | Subgraph border |
| `titleColor` | `#e5e5e5` | Subgraph title text |
| `background` | `#0d0d0d` | Diagram background |
| `mainBkg` | `#1a1a1a` | Default node background |

---

## 2. ClassDef palette (node styling)

Use these **classDef** names and values when you want semantic coloring. Define only the ones you use in that diagram.

| Class name | Fill | Stroke | Stroke width | Notes |
|------------|------|--------|--------------|--------|
| `glow` | `#252525` | `#00d4ff` | 1.5px | Lived experience, relationship practice, outcomes |
| `core` | `#1a1a1a` | `#444` | 1px | Distillation, AI ingestion, neutral/structural nodes |
| `guard` | `#1a2a24` | `#00d4ff` | 1.5px | Safety, ethics, guardrails |
| `loop` | `#161616` | `#555` | 1px, dashed 4 4 | Refinement loop, cyclic/process nodes |
| `art` | `#1e2433` | `#5c8fff` | 1.5px | Capture, reflection, outcomes (art layer) |
| `brain` | `#1e2433` | `#5c8fff` | 1px | Digital brain, cognition, attention |
| `body` | `#1a2a24` | `#00d4ff` | 1px | Digital body, regulation, somatics |
| `touch` | `#252525` | `#00d4ff` | 1.5px | Touch, nerves, organs, consent, boundaries |
| `agent` | `#252525` | `#00d4ff` | 1.5px | Central agent / embodied agent node |
| `outcome` | `#1e2433` | `#5c8fff` | 1px | User outcomes, growth |

**Apply with** `:::className` on the node, e.g. `N["My Node"]:::core`.

### Copy-paste classDef block (use only what you need)

```text
classDef glow fill:#252525,stroke:#00d4ff,stroke-width:1.5px;
classDef core fill:#1a1a1a,stroke:#444,stroke-width:1px;
classDef guard fill:#1a2a24,stroke:#00d4ff,stroke-width:1.5px;
classDef loop fill:#161616,stroke:#555,stroke-width:1px,stroke-dasharray: 4 4;
classDef art fill:#1e2433,stroke:#5c8fff,stroke-width:1.5px;
classDef brain fill:#1e2433,stroke:#5c8fff,stroke-width:1px;
classDef body fill:#1a2a24,stroke:#00d4ff,stroke-width:1px;
classDef touch fill:#252525,stroke:#00d4ff,stroke-width:1.5px;
classDef agent fill:#252525,stroke:#00d4ff,stroke-width:1.5px;
classDef outcome fill:#1e2433,stroke:#5c8fff,stroke-width:1px;
```

---

## 3. Conventions

- **Diagram type:** Prefer `flowchart TB` or `flowchart LR`; use `flowchart` (not `graph`).
- **Subgraphs:** Use explicit ID and label, e.g. `subgraph id [Label]`. No spaces in the ID (e.g. `agent`, `persistence`).
- **Node labels:** Use `["Label text"]`. For line breaks use `<br/>`, e.g. `["Line one<br/>line two"]`. Use `•` for bullet-style lists in labels.
- **Edge labels:** Put in double quotes, e.g. `A -->|"label"| B`.
- **Comments:** Use `%% comment` for notes; keep them short.
- **File format:** Each diagram in a `.md` file, fenced with ` ```mermaid ` and ` ``` `. Optional: a short title or caption in markdown above the block.

---

## 4. File location and naming

- **Location:** All diagram sources live under `diagrams/` (e.g. `diagrams/tis_10_diagrams/`, `diagrams/ti2_agent_chatgpt_bridge.md`).
- **Naming:** Use lowercase, underscores for multiword names; e.g. `ti2_agent_chatgpt_bridge.md`, `00_summary.md`.

---

## 5. Checklist for new or edited diagrams

1. First line of the mermaid block is the full `%%{init: {'theme': 'dark', 'themeVariables': { ... }}}%%` block from section 1.
2. If the diagram has nodes that map to brain/body/touch/guard/core/loop/art/glow/agent/outcome, add the corresponding classDef and apply with `:::className`.
3. Subgraph IDs have no spaces; labels can have spaces and punctuation.
4. Edge labels are in double quotes.
5. File is under `diagrams/` and is valid markdown with a single mermaid code block (or multiple blocks if the doc has several diagrams).

---

## 6. Reference diagrams in this repo

- **Theme + classDef (summary):** [tis_10_diagrams/00_summary.md](tis_10_diagrams/00_summary.md)
- **Theme + classDef (architecture):** [tantra_intelligence_squared_architecture.mmd.md](tantra_intelligence_squared_architecture.mmd.md)
- **Theme + classDef (bridge):** [ti2_agent_chatgpt_bridge.md](ti2_agent_chatgpt_bridge.md)
- **Theme + classDef (guardrails):** [tis_10_diagrams/04_guardrails.md](tis_10_diagrams/04_guardrails.md)

Use these as visual and structural references when adding or changing diagrams.
