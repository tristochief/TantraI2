```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#e5e5e5', 'primaryColor': '#1a1a1a', 'primaryBorderColor': '#444', 'lineColor': '#555', 'clusterBkg': '#1a1a1a', 'clusterBorder': '#333', 'titleColor': '#e5e5e5', 'background': '#0d0d0d', 'mainBkg': '#1a1a1a' }}}%%
flowchart TB
  classDef art fill:#1e2433,stroke:#5c8fff,stroke-width:1.5px;

  subgraph CAPTURE["Capture & Reflection"]
    direction TB
    N1["Field Notes<br/>exercises • teacher framing • breakthroughs"]:::art
    N2["Somatic Log<br/>sensations-as-words • triggers/settles • safety signals"]:::art
    N3["Relational Journal<br/>attachment cues • bids/repairs • devotion & boundaries"]:::art
    N4["Integration Rituals<br/>sleep/body care • meaning-making • commitments"]:::art
  end

  N1 --> N2 --> N3 --> N4
```
