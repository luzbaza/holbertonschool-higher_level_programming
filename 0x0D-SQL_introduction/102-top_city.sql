-- Import in hbtn_0c_0 database
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE mont IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
