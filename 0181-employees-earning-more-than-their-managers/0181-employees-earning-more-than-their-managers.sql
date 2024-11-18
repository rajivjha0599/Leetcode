# Write your MySQL query statement below

select e.name as Employee  from Employee as Emp inner join Employee as e 
    on Emp.id = e.managerId
    where e.salary>Emp.salary