SELECT SUM(
    (CASE WHEN Discount < 0.3 THEN Sales ELSE 0 END)*1.0
) / SUM(Sales) AS up_7_sales, 
SUM(
    (CASE WHEN Discount >= 0.3 THEN Sales ELSE 0 END)*1.0
) / SUM(Sales) AS down_7_sales,
SUM(
    (CASE WHEN Discount < 0.3 THEN Profit ELSE 0 END)*1.0
) / SUM(Profit) AS up_7_profit,
SUM(
    (CASE WHEN Discount >= 0.3 THEN Profit ELSE 0 END)*1.0
) / SUM(Profit) AS down_7_profit
FROM superstore

