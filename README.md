# Project 01: Customer Churn Prediction & Retention Analytics

## Objective

Predict telecom customer churn and explain which customer groups need retention action. The project is built as a business-facing analytics case study: SQL creates the operational view, Python trains a churn model, and Power BI communicates the retention story.

## Business Questions

- What is the overall churn rate?
- Which contracts, tenure bands, and support segments have the highest churn?
- Which customers should the retention team contact first?
- What estimated revenue is at risk?

## Contents

- `data sample telecom_customers.csv`: Sample customer data.
- `sql schema.sql`: Table definition.
- `sql analysis_queries.sql`: KPI, segmentation, and retention queries.
- `train_model.py`: Python classification model.
- `dashboards powerbi_dashboard_guide.md`: Power BI page layout.
- `dashboards dax_measures.txt`: Suggested DAX measures.

## Model

The Python pipeline trains a logistic regression model and a random forest model, compares ROC-AUC, and exports customer churn scores for dashboard use.

## Dashboard Pages

1. Executive Summary
2. Churn Drivers
3. Customer Risk List
4. Retention Actions

