# Write your MySQL query statement below
select P.firstName, P.lastName ,A.city, A.state
from person P left join  Address A on p.personId = A.personId
