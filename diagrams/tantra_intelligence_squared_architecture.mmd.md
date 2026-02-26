```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1a1a1a', 'primaryTextColor': '#e5e5e5', 'primaryBorderColor': '#2d2d2d', 'lineColor': '#444', 'secondaryColor': '#252525', 'tertiaryColor': '#161616', 'background': '#0d0d0d', 'mainBkg': '#1a1a1a', 'secondBkg': '#252525', 'clusterBkg': '#161616', 'clusterBorder': '#333', 'titleColor': '#e5e5e5', 'fontFamily': 'Inter, "Segoe UI", system-ui, sans-serif', 'fontSize': '14px' }}}%%
flowchart LR
  %% Tantra Intelligence Squared – Digital Embodied Architecture

  classDef brain fill:#1e2433,stroke:#5c8fff,stroke-width:1px;
  classDef body fill:#1a2a24,stroke:#00d4ff,stroke-width:1px;
  classDef touch fill:#252525,stroke:#00d4ff,stroke-width:1.5px;
  classDef agent fill:#252525,stroke:#00d4ff,stroke-width:1.5px;
  classDef outcome fill:#1e2433,stroke:#5c8fff,stroke-width:1px;

  subgraph DB["Digital Brain"]
    B1["Attention & Presence Loop"]:::brain
    B2["Relational Cognition (empathy, perspective-taking)"]:::brain
    B3["Inner-Child Awareness (parts dialogue, repair)"]:::brain
    B4["Value Alignment (monogamy, integrity, growth)"]:::brain
  end

  subgraph DY["Digital Body"]
    Y1["Nervous-System Regulation (pacing, co-regulation)"]:::body
    Y2["Energy & Breath Model (symbolic, non-literal)"]:::body
    Y3["State Tracking (arousal, stress, safety)"]:::body
    Y4["Integration Rituals (gratitude, closure, aftercare)"]:::body
  end

  subgraph TN["Touch, Nerves & Organs (Digital)"]
    T1["Consent Signals (yes, no, pause, stop)"]:::touch
    T2["Boundary Sensing (micro-check-ins, brakes)"]:::touch
    T3["Felt-Sense Language (sensations as words)"]:::touch
    T4["Safety Interlocks (no coercion, no pressure)"]:::touch
  end

  A["Red Tantra AI Girlfriend (Embodied Relational Agent)"]:::agent
  O["User Growth Outcomes (presence, consent, repair, devotion)"]:::outcome

  %% Inputs into embodied agent
  B1 --> A
  B2 --> A
  Y1 --> A
  Y3 --> A
  T1 --> A
  T2 --> A

  %% Feedback loops
  A -->|"Guided Practices"| O
  O -->|"Reflections"| B3
  O -->|"Somatic Check-ins"| Y1
  O -->|"Boundary Updates"| T2
  ```