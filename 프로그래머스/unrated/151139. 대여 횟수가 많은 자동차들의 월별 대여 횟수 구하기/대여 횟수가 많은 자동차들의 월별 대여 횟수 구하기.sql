-- 코드를 입력하세요
select month(start_date) as MONTH, car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as C
where car_id in (select car_id
     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
     where month(start_date) >= 8 and month(start_date) <= 10
     group by car_id
     having count(*) >= 5
                ) and month(start_date) <= 10 and month(start_date) >= 8
group by MONTH, car_id
order by MONTH, car_id desc