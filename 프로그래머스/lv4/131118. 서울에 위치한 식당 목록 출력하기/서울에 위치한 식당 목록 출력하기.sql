-- 코드를 입력하세요
SELECT I.rest_id, I.rest_name, I.food_type, I.favorites, I.address,
        round(avg(V.review_score), 2) as score
from rest_info I
inner join rest_review V on I.rest_id = V.rest_id
where I.address like '서울%'
group by I.rest_id
order by score desc, I.favorites desc