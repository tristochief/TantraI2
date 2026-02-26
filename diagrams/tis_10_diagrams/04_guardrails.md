```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#e5e5e5', 'primaryColor': '#1a1a1a', 'primaryBorderColor': '#444', 'lineColor': '#555', 'clusterBkg': '#1a1a1a', 'clusterBorder': '#333', 'titleColor': '#e5e5e5', 'background': '#0d0d0d', 'mainBkg': '#1a1a1a' }}}%%
flowchart TB
  classDef guard fill:#1a2a24,stroke:#00d4ff,stroke-width:1.5px;

  subgraph GUARD["Safety, Ethics & Reality-Checks (Always On)"]
    direction TB
    G1["Consent-First<br/>clear • voluntary • ongoing check-ins"]:::guard
    G2["Monogamy & Boundaries<br/>explicit agreements • no coercive loops"]:::guard
    G3["Privacy & Redaction<br/>anonymize others • secure storage"]:::guard
    G4["Reality-Check Discipline<br/>cite sources • mark uncertainty • avoid fantasy drift"]:::guard
    G5["Professional Support Boundary<br/>not therapy/medical • refer out when needed"]:::guard
  end

  G1 --> G2 --> G3 --> G4 --> G5
```
