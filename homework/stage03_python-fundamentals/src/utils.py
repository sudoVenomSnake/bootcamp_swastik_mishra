import pandas as pd

def get_summary_stats(df : pd.DataFrame) -> pd.DataFrame:
    describe = df.describe().reset_index()
    return describe