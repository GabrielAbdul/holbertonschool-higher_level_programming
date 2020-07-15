-- displays the avg temp by city ordered by temperature
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY AVG(VALUE) DESC;
