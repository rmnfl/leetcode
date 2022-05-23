# Write your MySQL query statement below
SELECT name as Customers
FROM Customers
WHERE id not in (SELECT DISTINCT customerId from Orders)