# Write your MySQL query statement below
with cte as (
    select num as ConsecutiveNums,lag(num) over (order by id) as previous,lead(num) over (order by id) as forward from Logs
)

select distinct(ConsecutiveNums) from cte where ConsecutiveNums = previous and previous = forward