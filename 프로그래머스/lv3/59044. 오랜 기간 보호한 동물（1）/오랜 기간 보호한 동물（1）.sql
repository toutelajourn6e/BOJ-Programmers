-- 코드를 입력하세요
SELECT I.name, I.datetime
from animal_ins I
    left join animal_outs O on I.animal_id = O.animal_id
where O.animal_id is Null
order by I.datetime limit 3