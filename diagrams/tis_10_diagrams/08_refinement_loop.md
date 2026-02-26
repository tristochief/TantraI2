```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#e5e5e5', 'primaryColor': '#1a1a1a', 'primaryBorderColor': '#444', 'lineColor': '#555', 'clusterBkg': '#1a1a1a', 'clusterBorder': '#333', 'titleColor': '#e5e5e5', 'background': '#0d0d0d', 'mainBkg': '#1a1a1a' }}}%%
flowchart TB
  classDef loop fill:#161616,stroke:#555,stroke-width:1px,stroke-dasharray: 4 4;

  subgraph REFINE["Refinement Loop (Weekly / Monthly)"]
    direction TB
    M["Review Metrics<br/>sleep/stress • repair latency • presence minutes"]:::loop
    E["Select Next Edge<br/>one constraint • one relational skill • one embodiment drill"]:::loop
    U["Update Protocols<br/>prune • tighten wording • add safety checks"]:::loop
  end

  M --> E --> U --> M
```
