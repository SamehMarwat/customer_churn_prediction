# Power BI Dashboard Guide

## Data Sources

- `data/sample/telecom_customers.csv`
- `outputs/customer_churn_scores.csv` after running the Python model

## Recommended Pages

### 1. Executive Summary

- KPI cards: Total Customers, Churn Rate, Monthly Revenue at Risk, High-Risk Customers
- Bar chart: Churn Rate by Contract Type
- Column chart: Churn Rate by Tenure Band
- Slicer: Contract Type, Payment Method, Internet Service

### 2. Churn Drivers

- Matrix: Contract Type x Payment Method with churn rate
- Scatter plot: Monthly Charges vs Tenure, colored by churn
- Bar chart: Average Support Tickets by Churn Status

### 3. Customer Risk List

- Table: Customer ID, Churn Probability, Risk Segment, Monthly Charges, Support Tickets
- Conditional formatting for high-risk customers

### 4. Retention Actions

- KPI: Estimated Annual Revenue at Risk
- Table of recommended retention targets
- Filter to High and Medium risk segments

## Dashboard Story

Month-to-month customers with higher support tickets, late payments, and fiber internet plans show higher churn risk. Retention actions should prioritize high monthly charge customers with high predicted churn probability.

