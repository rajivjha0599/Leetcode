CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
       with cte as(
       select *,DENSE_RANK() OVER(ORDER BY salary desc) AS rnk from 
       Employee
        )
       select distinct IFNULL(salary,null) from cte where rnk = N
);
END