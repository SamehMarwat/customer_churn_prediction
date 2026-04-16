-- Overall churn KPI
SELECT
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN churn = 1 THEN monthly_charges ELSE 0 END), 2) AS monthly_revenue_at_risk
FROM telecom_customers;

-- Churn by contract type
SELECT
    contract_type,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_pct,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges
FROM telecom_customers
GROUP BY contract_type
ORDER BY churn_rate_pct DESC;

-- Tenure band risk
SELECT
    CASE
        WHEN tenure_months < 6 THEN '0-5 months'
        WHEN tenure_months < 12 THEN '6-11 months'
        WHEN tenure_months < 24 THEN '12-23 months'
        WHEN tenure_months < 48 THEN '24-47 months'
        ELSE '48+ months'
    END AS tenure_band,
    COUNT(*) AS customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_pct
FROM telecom_customers
GROUP BY
    CASE
        WHEN tenure_months < 6 THEN '0-5 months'
        WHEN tenure_months < 12 THEN '6-11 months'
        WHEN tenure_months < 24 THEN '12-23 months'
        WHEN tenure_months < 48 THEN '24-47 months'
        ELSE '48+ months'
    END
ORDER BY churn_rate_pct DESC;

-- Retention priority list
SELECT
    customer_id,
    contract_type,
    tenure_months,
    monthly_charges,
    support_tickets,
    late_payments,
    ROUND(monthly_charges * 12, 2) AS annual_revenue_at_risk
FROM telecom_customers
WHERE churn = 1
ORDER BY annual_revenue_at_risk DESC, support_tickets DESC;

