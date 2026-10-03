SELECT "Sub-Category", SUM(Profit) AS down_7
FROM superstore 
WHERE Discount >= 0.3
GROUP BY "Sub-Category"
HAVING SUM(Profit) < 0
ORDER BY SUM(Profit)
