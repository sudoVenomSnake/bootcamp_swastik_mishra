import pandas as pd
import numpy as np

def format_date(date_like) -> str:
    """Coerce to YYYY-MM-DD string."""
    return pd.to_datetime(date_like).strftime("%Y-%m-%d")

def train_test_split_time(df : pd.DataFrame, split : float = 0.8):
    n = len(df)
    cut = int(n * split)
    return df.iloc[:cut].copy(), df.iloc[cut:].copy()
