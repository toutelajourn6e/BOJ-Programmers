-- 코드를 입력하세요
SELECT pt_name, pt_no, gend_cd, age, case when tlno is Null then 'NONE'
                                        else tlno end as tlno
from PATIENT
where age <= 12 and gend_cd = 'w'
order by age desc, pt_name
