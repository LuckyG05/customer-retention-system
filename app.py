import streamlit as st
import pandas as pd

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Customer Retention System", layout="wide")

st.title("Customer Retention Intelligence System")

# ----------------------------
# Load Data
# ----------------------------
df = pd.read_csv("final_data.csv")

# ----------------------------
# Sidebar Filters
# ----------------------------
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

filtered_df = df[
    (df["Risk"].isin(risk_filter)) &
    (df["Value"].isin(value_filter))
]

# ----------------------------
# Key Metrics
# ----------------------------
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("High Risk Customers", len(df[df["Risk"] == "High Risk"]))
col3.metric("High Value Customers", len(df[df["Value"] == "High Value"]))

# ----------------------------
# Alerts & Insights
# ----------------------------
high_risk_count = len(df[df["Risk"] == "High Risk"])

st.warning(f"{high_risk_count} customers are at high risk of churn!")

st.subheader("Key Insight")

st.info("""
High-value customers with high churn risk should be prioritized for retention strategies 
such as discounts, personalized offers, and engagement campaigns.
""")

# ----------------------------
# Priority Customers
# ----------------------------
st.subheader("Priority Customers (High Value + High Risk)")

priority_df = df[
    (df["Risk"] == "High Risk") &
    (df["Value"] == "High Value")
]

st.write(f"Total Priority Customers: {len(priority_df)}")

st.dataframe(priority_df)

# ----------------------------
# Recommended Action
# ----------------------------
st.subheader("Recommended Action")

st.success("""
Focus on high-value, high-risk customers first.

Suggested strategies:
- Offer discounts
- Provide personalized recommendations
- Improve service experience
- Increase engagement through notifications
""")

# ----------------------------
# Filtered Data
# ----------------------------
st.subheader("Filtered Customer Data")

st.dataframe(filtered_df)

# ----------------------------
# Charts
# ----------------------------
st.subheader("Customer Distribution")

col1, col2 = st.columns(2)

with col1:
    st.write("Risk Distribution")
    st.bar_chart(df["Risk"].value_counts())

with col2:
    st.write("Value Distribution")
    st.bar_chart(df["Value"].value_counts())

# ----------------------------
# Download Button
# ----------------------------
st.subheader("Download Data")

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Full Dataset",
    data=csv,
    file_name='customer_data.csv',
    mime='text/csv',
)
st.dataframe(filtered_df)

# Charts
st.subheader("Distribution")

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(df["Risk"].value_counts())

with col2:
    st.bar_chart(df["Value"].value_counts())
