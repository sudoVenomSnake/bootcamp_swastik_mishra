import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    for col in columns:
        if col in df.columns:
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)
    return df


def drop_missing(df, threshold = 0.5):
    limit = int((1 - threshold) * df.shape[1])
    return df.dropna(thresh = limit)


def normalize_data(df, columns):
    for col in columns:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
            else:
                df[col] = 0.0
    return df