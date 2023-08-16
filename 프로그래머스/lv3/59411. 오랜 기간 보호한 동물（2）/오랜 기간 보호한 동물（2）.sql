-- 코드를 입력하세요
SELECT I.animal_id, I.name
from animal_ins I
    inner join animal_outs O on I.animal_id = O.animal_id
order by datediff(O.datetime, I.datetime) desc limit 2