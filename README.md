# Customer Retention Intelligence System

An end-to-end data science project that analyzes customer behavior, predicts churn, and recommends targeted retention strategies using machine learning and business-driven insights.

**Live App:** [https://customer-retention-system-tft6vwyh7cirfzhiaadzfj.streamlit.app/](https://customer-retention-system-tft6vwyh7cirfzhiaadzfj.streamlit.app/)

---

## Problem Statement

Customer churn is one of the biggest challenges for subscription-based businesses. Losing high-value customers directly impacts revenue.

This project aims to:
- Identify customers likely to churn
- Segment users based on behavior
- Recommend actionable retention strategies

---

## Solution Approach

The system combines:
- Data Analysis (EDA)
- Customer Segmentation (RFM)
- Machine Learning (Churn Prediction)
- Business Strategy Engine
- Interactive Dashboard (Streamlit)

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## Key Features

### 1️⃣ Data Cleaning & Preprocessing
- Handled missing values
- Converted categorical features
- Fixed inconsistent data types

---

### 2️⃣ Exploratory Data Analysis (EDA)
- Identified key churn drivers:
  - Tenure
  - Monthly Charges
  - Contract Type
- Visualized customer behavior patterns

---

### 3️⃣ RFM-Based Customer Segmentation

Customers were segmented using:
- **Recency (Tenure)**
- **Frequency (Service Usage)**
- **Monetary (Total Charges)**

Segments identified:
- High Value Customers
- At Risk Customers
- Inactive Users
- Potential Loyal Customers

---

### 4️⃣ Churn Prediction Model

Built and compared:
- Logistic Regression (Baseline)
- Random Forest (Improved Model)

**Results:**
- Accuracy: ~80%
- Recall improved from **58% → 76%**

---

### 5️⃣ Retention Strategy Engine

Customers are categorized based on:
- Risk Level (Churn Probability)
- Value Level (Spending)

Example Actions:
- High Risk + High Value → Priority retention (discounts/offers)
- Low Risk + High Value → Loyalty rewards
- High Risk + Low Value → Minimal intervention

---

### 6️⃣ Interactive Dashboard

Built using Streamlit:
- Filter customers by Risk & Value
- View high-priority customers
- Analyze key metrics
- Visualize distributions

---

## Sample Output

- Identifies high-value customers at risk of churn
- Provides actionable insights for retention
- Supports business decision-making

---

## How to Run Locally

```bash
git clone https://github.com/LuckyG05/customer-retention-system.git
cd customer-retention-system
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements
- Add real-time prediction input
- Deploy using cloud services
- Improve UI/UX design
- Use advanced models (XGBoost)

---

## Key Learnings
- Importance of recall in imbalanced datasets
- Feature engineering using RFM
- Business-driven ML decision making
- End-to-end deployment of ML systems

---

## Author

Lucky Gautam
