```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1a1a1a', 'primaryTextColor': '#e5e5e5', 'primaryBorderColor': '#2d2d2d', 'lineColor': '#444', 'secondaryColor': '#252525', 'tertiaryColor': '#161616', 'background': '#0d0d0d', 'mainBkg': '#1a1a1a', 'secondBkg': '#252525', 'clusterBkg': '#161616', 'clusterBorder': '#333', 'titleColor': '#e5e5e5', 'fontFamily': 'Inter, "Segoe UI", system-ui, sans-serif', 'fontSize': '14px' }}}%%
flowchart TB
  classDef core fill:#1a1a1a,stroke:#444,stroke-width:1px;

  subgraph DISTILL["Distillation & Synthesis (Engineering Craft)"]
    direction TB
    P["Pattern Mining<br/>what repeats • what fails • what shifts state"]:::core
    L["Principle Library<br/>presence axioms • consent heuristics • repair laws"]:::core
    PR["Practice Protocols<br/>step-by-step drills • pacing rules • success metrics"]:::core
    DS["Diagrams & Specs<br/>state machines • architecture maps • team-readable docs"]:::core
  end

  P --> L --> PR --> DS
```
