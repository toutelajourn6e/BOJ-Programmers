-- 코드를 입력하세요
SELECT C1.cart_id
from (select cart_id
     from cart_products
     where name = 'Milk') as C1
inner join (select cart_id
           from cart_products
           where name = 'Yogurt') as C2 on C1.cart_id = C2.cart_id
order by C1.cart_id