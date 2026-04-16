import streamlit as st
import pandas as pd

df = pd.read_csv("final_data.csv")

st.set_page_config(page_title="Customer Retention System", layout="wide")

st.title("Customer Retention Intelligence System")

# Sidebar Filters
st.sidebar.header("Filter Customers")

risk_filter = st.sidebar.multiselect(
    "Select Risk Level",
    options=df["Risk"].unique(),
    default=df["Risk"].unique()
)

value_filter = st.sidebar.multiselect(
    "Select Value Level",
    options=df["Value"].unique(),
    default=df["Value"].unique()
)

# Apply filters
filtered_df = df[
    (df["Risk"].isin(risk_filter)) &
    (df["Value"].isin(value_filter))
]

# Metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("High Risk Customers", len(df[df["Risk"] == "High Risk"]))
col3.metric("High Value Customers", len(df[df["Value"] == "High Value"]))

# Show important segment
st.subheader("High Value + High Risk Customers")

priority_df = df[
    (df["Risk"] == "High Risk") &
    (df["Value"] == "High Value")
]

st.dataframe(priority_df)

# Show filtered data
st.subheader("📋 Filtered Customer Data")

st.dataframe(filtered_df)

# Charts
st.subheader("Distribution")

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(df["Risk"].value_counts())

with col2:
    st.bar_chart(df["Value"].value_counts())