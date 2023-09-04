-- 코드를 입력하세요
SELECT year(O.sales_date) year, month(O.sales_date) month, I.gender gender, 
        count(distinct I.user_id) as users
from user_info I
inner join online_sale O on I.user_id = O.user_id
where I.gender is not Null
group by 1, 2, 3
order by 1, 2, 3