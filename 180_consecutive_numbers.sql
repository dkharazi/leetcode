/*
180. Consecutive Numbers

Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

https://my.oschina.net/Tsybius2014/blog/494823
*/

/*
USE LEETCODE;
DROP TABLE IF EXISTS Logs;

Create table If Not Exists Logs (Id int, Num int);
Truncate table Logs;
insert into Logs (Id, Num) values ('1', '1');
insert into Logs (Id, Num) values ('2', '1');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '2');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');
*/

SELECT DISTINCT L1.Num as ConsecutiveNums
FROM Logs L1
JOIN Logs L2 ON L1.Id + 1 = L2.Id
JOIN Logs L3 ON L1.Id + 2 = L3.Id
WHERE L1.Num = L2.Num AND L1.Num = L3.Num
ORDER BY L1.Num;

SELECT DISTINCT L1.Num
FROM Logs L1, Logs L2, Logs L3
WHERE (L1.Id = L2.Id + 1 AND L1.Num = L2.Num) AND
  (L1.Id = L3.Id + 2 AND L1.Num = L3.Num)

