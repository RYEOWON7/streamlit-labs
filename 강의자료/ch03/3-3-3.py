import streamlit as st
import pandas as pd

# 데이터 준비
df = pd.read_csv("../data/titanic.csv")
df = df[["Age", "Survived"]]
chart_df = df.groupby(["Age"]).sum()
chart_df["Age"] = chart_df.index

st.dataframe(df)
st.dataframe(chart_df)
