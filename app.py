import streamlit as st
import pandas as pd

st.title("📊 Hiring Data Dashboard")

df = pd.read_csv("jobs.csv")

st.dataframe(df)

company = st.selectbox("Select Company", df["company"].unique())
st.dataframe(df[df["company"] == company])
