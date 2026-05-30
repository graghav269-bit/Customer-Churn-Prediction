-- ==========================================
-- CUSTOMER CHURN ANALYSIS SQL QUERIES
-- ==========================================

-- 1. Overall Churn Rate

SELECT
    ROUND(
        100.0 *
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percentage
FROM customer_churn;


-- 2. Revenue Loss Due To Churn

SELECT
    ROUND(
        SUM(MonthlyCharges),
        2
    ) AS Monthly_Revenue_Loss
FROM customer_churn
WHERE Churn = 'Yes';


-- 3. Contract Wise Churn

SELECT
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 *
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;


-- 4. Payment Method Analysis

SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 *
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;


-- 5. Tenure Analysis

SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '48+ Months'
    END AS Tenure_Group,

    COUNT(*) AS Total_Customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate

FROM customer_churn

GROUP BY Tenure_Group

ORDER BY Churn_Rate DESC;


-- 6. Monthly Charges Analysis

SELECT
    CASE
        WHEN MonthlyCharges < 30 THEN 'Low'
        WHEN MonthlyCharges < 70 THEN 'Medium'
        ELSE 'High'
    END AS Charge_Category,

    COUNT(*) AS Total_Customers,

    ROUND(
        AVG(MonthlyCharges),
        2
    ) AS Avg_Monthly_Charge,

    ROUND(
        100.0 *
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate

FROM customer_churn

GROUP BY Charge_Category

ORDER BY Churn_Rate DESC;