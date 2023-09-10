-- 코드를 입력하세요
set @var7 = (select replace(discount_rate, '%', '')
                       from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                       where car_type = '트럭' and left(duration_type, 1) = '7');
set @var30 = (select replace(discount_rate, '%', '')
                       from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                       where car_type = '트럭' and left(duration_type, 2) = '30');
set @var90 = (select replace(discount_rate, '%', '')
                       from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                       where car_type = '트럭' and left(duration_type, 2) = '90');
                       
                       
SELECT H.history_id,
       case when datediff(H.end_date, H.start_date) + 1 >= 90
       then floor((C.daily_fee - (C.daily_fee * (0.01 * @var90))) * (datediff(H.end_date, H.start_date) + 1))
       when datediff(H.end_date, H.start_date) + 1 >= 30
       then floor((C.daily_fee - (C.daily_fee * (0.01 * @var30))) * (datediff(H.end_date, H.start_date) + 1))
       when datediff(H.end_date, H.start_date) + 1 >= 7
       then floor((C.daily_fee - (C.daily_fee * (0.01 * @var7))) * (datediff(H.end_date, H.start_date) + 1))
       else C.daily_fee * (datediff(H.end_date, H.start_date) + 1) end as fee
from CAR_RENTAL_COMPANY_CAR C
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY H on C.car_id = H.car_id
where C.car_type = '트럭'
order by fee desc, H.history_id desc