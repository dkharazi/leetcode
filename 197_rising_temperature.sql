/*
197. Rising Temperature

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+

For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
*/

select w2.Id from Weather w1 JOIN Weather w2 on datediff(w2.Date, w1.Date) = 1  where w2.Temperature > w1.Temperature;

select w2.Id from Weather w1 JOIN Weather w2 where datediff(w2.Date, w1.Date) = 1 and w2.Temperature > w1.Temperature;

select w2.Id from Weather w1, Weather w2 where datediff(w2.Date, w1.Date) = 1 and w2.Temperature > w1.Temperature;
