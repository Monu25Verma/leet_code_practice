# Write your MySQL query statement below

select  s.name
from salesPerson s
    where s.name not in
    (select s.name
    from salesPerson s
    LEFT JOIN orders o on s.sales_id = o.sales_id
    LEFT JOIN company c on o.com_id = c.com_id
    where c.name = 'red');
