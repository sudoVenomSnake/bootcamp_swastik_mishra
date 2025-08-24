import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout = "wide")

@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv("train.csv")

def return_figure(df : pd.DataFrame, targets : list):
    fig = go.Figure()
    for x in targets:
        fig.add_trace(go.Scatter(x = df["date_id"], y = df[x], mode = 'lines', name = x))
    st.plotly_chart(fig, use_container_width = True)

st.title("EDA for checking plots")

df = load_data()
targets = st.multiselect(label = "Select Targets - ", options = df.columns[1:])
if targets:
    return_figure(df, targets)