-- 코드를 입력하세요
SELECT animal_id, name
from ANIMAL_INS
where name like('%el%') and animal_type = 'Dog'
order by upper(name)