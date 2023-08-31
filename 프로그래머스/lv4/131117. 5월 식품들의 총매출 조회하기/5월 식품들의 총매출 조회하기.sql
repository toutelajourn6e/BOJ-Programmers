-- 코드를 입력하세요
SELECT P.product_id, P.product_name, P.price * sum(O.amount) as total_sales
from food_product P
inner join food_order O on P.product_id = O.product_id
where year(O.produce_date) = 2022 and month(O.produce_date) = 5
group by P.product_id
order by total_sales desc, P.product_id
