-- 코드를 입력하세요
SELECT I.ingredient_type, sum(total_order) as total_order
from first_half F
    inner join icecream_info I on F.flavor = I.flavor
group by I.ingredient_type
order by total_order