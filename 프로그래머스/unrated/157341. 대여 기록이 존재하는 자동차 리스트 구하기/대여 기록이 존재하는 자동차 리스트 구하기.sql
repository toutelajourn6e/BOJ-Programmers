-- 코드를 입력하세요
SELECT distinct C.car_id
from car_rental_company_car C
    inner join car_rental_company_rental_history H on C.car_id = H.car_id
where C.car_type = '세단' and month(H.start_date) = 10
order by C.car_id desc
