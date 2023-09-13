-- 코드를 입력하세요
set @total = (SELECT count(distinct user_id)
              from user_info
              where year(joined) = 2021);
              
select year(sales_date), month(sales_date), count(distinct user_id) as puchased_users,
       round(count(distinct user_id) / @total, 1) as puchased_ratio
from online_sale
where user_id in (SELECT distinct user_id
                  from user_info
                  where year(joined) = 2021)
group by 1, 2