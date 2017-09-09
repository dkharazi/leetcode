/*
184. Department Highest Salary

The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
*/

/*
create database leetcode;
use leetcode;

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
Create table If Not Exists Department (Id int, Name varchar(255));
Truncate table Employee;
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1');
Truncate table Department;
insert into Department (Id, Name) values ('1', 'IT');
insert into Department (Id, Name) values ('2', 'Sales');
*/

/* 
http://www.cnblogs.com/zhangyunhao/p/4896055.html

See below queries.

mysql> select *  from Department join Employee  on Department.Id = Employee.DepartmentId;
+------+-------+------+-------+--------+--------------+
| Id   | Name  | Id   | Name  | Salary | DepartmentId |
+------+-------+------+-------+--------+--------------+
|    1 | IT    |    1 | Joe   |  70000 |            1 |
|    2 | Sales |    2 | Henry |  80000 |            2 |
|    2 | Sales |    3 | Sam   |  60000 |            2 |
|    1 | IT    |    4 | Max   |  90000 |            1 |
+------+-------+------+-------+--------+--------------+

mysql> select DepartmentId, max(Salary) from Employee group by DepartmentId;
+--------------+-------------+
| DepartmentId | max(Salary) |
+--------------+-------------+
|            1 |       90000 |
|            2 |       80000 |
+--------------+-------------+
*/
select Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary 
from Department join Employee 
on Department.Id = Employee.DepartmentId
where (Department.Id, Employee.Salary) in 
(select DepartmentId, max(Salary) from Employee group by DepartmentId);

/* Wrong answer
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Joe      |  90000 |
| Sales      | Henry    |  80000 |
+------------+----------+--------+
 */
select Department.Name as Department, Employee.Name as Employee, max(Salary) as Salary from Employee, Department where Employee.DepartmentId = Department.Id group by Department.Id;


