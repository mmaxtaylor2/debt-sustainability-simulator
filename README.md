# Debt Sustainability Simulator

https://debt-sustainability-simulator-e9ubg42isrnqpa33nylg9a.streamlit.app

## Overview

A Python-based analytical project that models medium-term sovereign debt sustainability under different macroeconomic and fiscal policy assumptions. The project mirrors how economists and sovereign risk analysts evaluate sovereign debt trajectories by linking growth, interest rates, and primary balances into a unified debt dynamics framework.

The objective is to quantify how interest-growth differentials, fiscal consolidation paths, and macro shocks influence debt-to-GDP ratios and interest burdens over time.

## Problem Context

Debt sustainability is often discussed qualitatively, but formal assessment requires quantifying the mechanics of debt accumulation. Rising interest costs, weak growth, and persistent deficits compound over time, producing nonlinear debt dynamics that are sensitive to both policy choices and macro conditions.

This project introduces a structured simulation framework for analyzing how different macro-fiscal environments propagate through sovereign balance sheets.

## Key Questions

- How does the debt-to-GDP ratio evolve under different macro assumptions?
- What primary balance is required to stabilize debt over a chosen horizon?
- How sensitive is debt sustainability to shocks in growth, rates, and fiscal behavior?
- Under what conditions do interest costs outpace GDP growth, generating “snowball effects”?

## Economic Framework

The model applies the standard sovereign debt dynamics identity:

\[
d_{t+1} = \left(\frac{1+r}{1+g}\right)d_t - pb_t
\]

Where:

- \(d_t\) = Debt-to-GDP ratio  
- \(r\) = Effective interest rate on outstanding debt  
- \(g\) = Real GDP growth rate  
- \(pb_t\) = Primary balance (surplus = positive)

This formulation highlights the interest-growth differential \((r - g)\), a central driver of sovereign debt sustainability frameworks.

## Data Inputs

The system accepts two structured input layers:

### Baseline Macro Path

Includes observed historical values for:
- Debt-to-GDP
- Interest-to-GDP
- Starting year anchor

### Scenario Layer

Defines alternative macro-fiscal environments:
- Growth shocks
- Interest rate shocks
- Primary balance adjustments

All inputs are provided as transparent, reproducible CSV artifacts.

## Methodology

### 1. Baseline Projection

Constructs a no-policy-change debt trajectory from the baseline dataset.

### 2. Scenario Application

Applies user-defined macro-fiscal shocks to evaluate sensitivity and stress outcomes.

### 3. Sustainability Metrics

Computes:
- Required primary balance for stabilization
- Interest burden as percent of GDP
- Scenario comparison statistics

### 4. Visualization Layer

Generates charts and tables suitable for sovereign risk and fiscal policy analysis.

## Outputs

The simulator produces the following outputs:
- Debt-to-GDP projection time series
- Interest burden time series (% of GDP)
- Stabilization primary balance requirement
- Multi-scenario comparison tables
- Exportable underlying data

Outputs align with formats used in policy analysis, sovereign research, and fiscal surveillance.

## Analytical Applications

Relevant analytical use cases include:
- Sovereign credit risk assessment
- Fiscal policy and budget analysis
- Macro scenario evaluation
- Public finance research
- Think tank and academic applications

## Prototype Insights

Initial simulations indicate:
- Debt sustainability is highly sensitive to the interest-growth differential
- Higher effective rates significantly increase stabilization primary surpluses
- Fiscal deficits are sustainable only when growth outpaces interest costs
- Under persistent deficits, stabilization may require politically challenging adjustments

## Technical Architecture

**Language:** Python  
**Interface:** Streamlit  

**Core Libraries:**
- pandas
- numpy
- plotly
- streamlit

**Repository Structure:**
```
data/               # baseline and scenario CSV inputs
models/             # debt dynamics logic and scenario engine
ui/                 # visualization and dashboard components
streamlit_app.py    # application entry point
```

## Scope

The project is designed for analytical demonstration and macro-fiscal research. It is not a forecasting model and does not constitute investment advice, credit rating opinion, or policy recommendation.

## Future Extensions

Planned enhancements include:
- Stochastic fan chart simulations
- Maturity structure and rollover risk modeling
- FX vs. domestic debt segmentation
- IMF-style DSA risk thresholds
- Adjustment vs. market-access scenario modes
