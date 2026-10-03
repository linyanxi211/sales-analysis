SELECT Discount, SUM(Sales) AS Sales, COUNT(*) AS dis_count
FROM superstore 
GROUP BY Discount
ORDER BY Discount