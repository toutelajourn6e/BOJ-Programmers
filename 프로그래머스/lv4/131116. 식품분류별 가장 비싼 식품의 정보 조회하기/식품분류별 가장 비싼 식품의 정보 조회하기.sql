-- 코드를 입력하세요
select F2.category, F2.max_price, F1.product_name
from food_product F1
inner join (
        select category, max(price) as max_price
        from food_product
        where category in ('과자', '식용유', '국', '김치')
        group by category
    ) as F2 on F1.category = F2.category and F1.price = F2.max_price
order by F2.max_price desc