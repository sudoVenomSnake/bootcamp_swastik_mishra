## Framework Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Framed the task as predicting next-day returns for equities using Yahoo Finance data. | Defining clear success criteria was tricky, since prediction quality in finance is inherently low. | Scoped the project as an educational demo, not an investment-grade tool. | Next time, tighten scope around a business-relevant decision (e.g., volatility forecasting for risk mgmt). |
| **2. Tooling Setup** | Used Python, Jupyter, scikit-learn, yfinance, matplotlib, and Streamlit. | Dependency mismatches (e.g., yfinance versions). | Standardized environment with requirements file and virtualenv. | -
| **3. Python Fundamentals** | Applied pandas/numpy for data wrangling, functions for features, joblib for saving models. | - | - | Keep strengthening data wragling in Python and read into performance optimization techniques. |
| **4. Data Acquisition / Ingestion** | Pulled daily ticker data from Yahoo Finance via yfinance API. | The column headers came in an unexpected format. | Fixed the formatting using simple Pandas code. | Add a function to not keep writing formatting code again. |
| **5. Data Storage** | Stored CSVs in data/raw/ and data/preprocessed/. | Deliberated between CSV and other storage options. | Decided on CSV as it is the most common file type and aligns with project requirements. | Move to compressed file types when the data becomes larger. |
| **6. Data Preprocessing** | Computed returns, moving averages, RSI, rolling volatility. | Missing values after rolling ops. | Dropped NA rows post-feature creation. | Explore forward/backward fill. |
| **7. Outlier Analysis** | Looked at unusual return spikes, volume shocks. | Loads of outliers but data is genuine. | Kept outliers (since they are part of reality). | Maybe add anomaly detection. |
| **8. Exploratory Data Analysis (EDA)** | Plotted volume by day | Data has lots of noise. | - | Checks for outliers. |
| **9. Feature Engineering** | Built technical indicators: returns, moving averages, RSI, volatility. | Unsure which features actually add predictive power. | Selected small, interpretable set for baseline. | Need to read more on feature transformation in this context. |
| **10. Modeling (Regression / Time Series / Classification)** | Trained RandomForestRegressor on technical features. | Overfitting risk and weak predictive signal. | - | Explore better techniques for this problem. |
| **11. Evaluation & Risk Communication** | Evaluated with MAE and R². | R² was poor, highlighting weak predictive power. | Documented naive approach and that results are not reliable. | - |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Summarized in notebooks, Streamlit dashboard, metrics.json. | Hard to explain poor performance without discouraging stakeholders. | Clearly framed project as educational, not investment-ready. | Improve communication with scenario-based demos.
| **13. Productization** | Wrapped model into Flask app. | - | - | Test deploying this to cloud. |
| **14. Deployment & Monitoring** | Deployed locally via Flask. | - | - | Add more route apart from /predict/. |
| **15. Orchestration & System Design** | Used manual notebooks as pipeline stages. | Lack of automation and error handling. | - | - |
| **16. Lifecycle Review & Reflection** | Learned end-to-end cycle from ingestion to deployment. | Most struggle: feature design and low signal quality. | Pattern: modularizing early helped reuse across notebooks/app. | Focus on more robust data and realistic financial targets. |

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why? - Feature engineering and modeling, because the prediction is weak and results are often disappointing.  
- Which stage was the most **rewarding**? - Building the Flask app — seeing a API come alive interactively.
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  - Poor scoping (naive return prediction) constrained later stages.
- If you repeated this project, what would you **do differently across the lifecycle**? - Choose a more meaningful financial problem (e.g., volatility or risk forecasting) and plan evaluation metrics earlier.
- Which skills do you most want to **strengthen** before your next financial engineering project? - Time Series in a Financial context.

---