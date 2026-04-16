import streamlit as st
import pandas as pd

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Customer Retention System", layout="wide")

st.title("Customer Retention Intelligence System")
st.markdown("---")
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
# ----------------------------
# Alerts & Insights
# ----------------------------
high_risk = len(filtered_df[filtered_df["Risk"] == "High Risk"])
total = len(filtered_df)
if total > 0:
    churn_rate = high_risk / total

    # Alert based on percentage
    if churn_rate > 0.4:
        st.error("Critical Alert: Very high churn risk! Immediate action required.")
    elif churn_rate > 0.25:
        st.warning("Warning: Moderate churn risk. Focus on retention strategies.")
    else:
        st.success("Customer churn is under control.")

    # Show metrics
    st.write(f"**High Risk Customers:** {high_risk}")
    st.write(f"**Churn Rate:** {churn_rate:.2%}")

else:
    st.info("No data available for selected filters.")

st.subheader("Key Insight")
if total == 0:
    st.info("No insights available.")
elif churn_rate > 0.3:
    st.error("""
A significant portion of customers are at high risk of churn.
Focus on retention strategies like discounts and engagement campaigns.
""")
else:
    st.success("""
Customer base is relatively stable.
Focus on maintaining engagement and loyalty programs.
""")

# ----------------------------
# Priority Customers
# ----------------------------
st.subheader("Priority Customers (High Value + High Risk)")
priority_df = filtered_df[
    (filtered_df["Risk"] == "High Risk") &
    (filtered_df["Value"] == "High Value")
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
st.markdown("---")

st.dataframe(filtered_df)

# ----------------------------
# Charts
# ----------------------------
st.subheader("Customer Distribution")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.write("Risk Distribution")
    risk_counts = filtered_df["Risk"].value_counts(normalize=True) * 100
    st.bar_chart(risk_counts)

with col2:
    st.write("Value Distribution")
    st.bar_chart(filtered_df["Value"].value_counts())

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
