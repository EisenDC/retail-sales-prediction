SELECT category,
       ROUND(AVG(ABS(sales - sales_prediction)), 2) AS avg_error
FROM sales_predictions
GROUP BY category
ORDER BY avg_error DESC;
