CREATE TABLE telecom_customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    gender VARCHAR(20),
    senior_citizen INTEGER,
    tenure_months INTEGER,
    contract_type VARCHAR(50),
    payment_method VARCHAR(50),
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(12,2),
    support_tickets INTEGER,
    late_payments INTEGER,
    internet_service VARCHAR(50),
    churn INTEGER
);

