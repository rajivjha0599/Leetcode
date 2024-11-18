# Write your MySQL query statement below

select worker.name as Employee  from Employee as worker inner join Employee as manager 
    on worker.managerId = manager.id
    where worker.salary>manager.salary