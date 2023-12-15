# Write your MySQL query statement below

select class from Courses
group by class                  #groupby comes under aggregate function contains the max, avg, sum, min, len...             #it will automatically make a group of the classes
having count(class) >= 5;           #count the no. of element in class
