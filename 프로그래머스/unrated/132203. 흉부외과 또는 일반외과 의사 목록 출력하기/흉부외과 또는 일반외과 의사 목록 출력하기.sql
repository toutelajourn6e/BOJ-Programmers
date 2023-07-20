-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD, '%Y-%m-%d') as hire_ymd
from doctor
where mcdp_cd IN ('CS', 'GS')
order by hire_ymd desc, dr_name