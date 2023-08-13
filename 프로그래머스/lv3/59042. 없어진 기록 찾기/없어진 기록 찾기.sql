-- 코드를 입력하세요
SELECT O.animal_id, O.name
from animal_outs O
    left join animal_ins I on O.animal_id = I.animal_id
where I.animal_id is Null
order by O.animal_id