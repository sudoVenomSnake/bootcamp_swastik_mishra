# Stock Forecasting with Yahoo Finance & Scikit-Learn
**Stage:** COMPLETED

## Problem Statement
Build a reproducible, end‑to‑end workflow to fetch equities data from Yahoo Finance, engineer predictive features, train a machine learning model, and deliver interactive predictions.

## Stakeholder & User
- **Stakeholders:** Data science team, product managers, retail investing group.
- **Primary Users:** Analysts and technically minded investors who want quick model-driven signals without running notebooks.

## Useful Answer & Decision
- Provide a trained model that predicts **next-day % return** from recent technical indicators.
- Allow a user to type a ticker in a Streamlit app and instantly see the model’s predicted next‑day return, recent features, and backtest metrics.

## Assumptions & Constraints
- Uses `yfinance` for price data (subject to Yahoo TOS and rate limits).
- Modeling target is next-day arithmetic return from adjusted close.
- Baseline model uses scikit‑learn (RandomForestRegressor) with simple technical features.
- This project takes a very naive approach to prediction, results might not be the best.
- Project is Python 3.13.4; notebooks run locally.

## Known Unknowns / Risks
- Data quality drifts (splits/dividends adjustments) may affect reproducibility.
- Predictive power may be low.
- Yahoo endpoints and ticker symbols can change.

## Repo Plan
```
data/
  raw/
  preprocessed/
notebooks/
  data_fetching.ipynb
  data_eda.ipynb
  feature_engineering.ipynb
  model_building.ipynb
  results_analysis.ipynb
src/
  config.py
reports/
  {ticker}_metrics.json
model/
  {ticker}_model.pkl
README.md
```