# Commodity Prediction
**Stage:** Problem Framing & Scoping (Stage 01)

### Updates
- Added eda.py in /src/, an interactive app to check plots and potential feature relationships

## Problem Statement
Developing a model capable of predicting future commodity returns using historical data from London Metal Exchange (LME), Japan Exchange Group (JPX), US Stock, and Forex markets. Getting these predictions right has significant implications for both businesses and the global economy. Inaccurate forecasts can lead to suboptimal trading strategies, poor investment decisions, and increased financial risk for companies involved in commodity markets.

## Stakeholder & User
Accurate commodity price prediction is crucial for reducing financial risk and ensuring stability in the global market. Currently, the inherent volatility and unpredictability of commodity prices create several problems - resource allocation, budgeting, and investment planning, often resulting in financial losses and inefficient operations

## Useful Answer & Decision
Useful Answer - **Predictive**
Metric is a variant of the Sharpe ratio, computed by dividing the mean Spearman rank correlation between the predictions and targets by the standard deviation.

## Assumptions & Constraints
 - Historical market data is available, accurate and sufficient for modeling.
 - Past price patterns contain useful predictive information for future returns.

## Known Unknowns / Risks
Advanced AI algorithms and high-precision models are currently employed for commodity market prediction, utilizing historical price datasets from LME, JPX, US Stock, and Forex. While these models show promise, they often encounter limitations in consistently achieving high accuracy across diverse market conditions and over extended time horizons. Existing models may exhibit over-reliance on specific data patterns, lacking the adaptability required to navigate the dynamic and constantly evolving nature of financial markets.

## Repo Plan
Paths for these are in .env
/data/ - Kaggle competition data, will have to add to .gitignore
/data/raw/ - for raw data
/data/processed/ - for validated/verified processed data
- Formats used -> CSV (most common storage type) and Parquet (compressed storage)
/src/ - Production app code
/notebooks/ - Primary code-base
/docs/ - Documenting steps