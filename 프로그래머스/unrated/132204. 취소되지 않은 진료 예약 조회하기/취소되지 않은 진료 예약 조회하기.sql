-- 코드를 입력하세요
SELECT A.apnt_no, P.pt_name, P.pt_no, A.mcdp_cd, D.dr_name, A.apnt_ymd
from appointment A
inner join patient P on A.pt_no = P.pt_no
inner join doctor D on A.mddr_id = D.dr_id
where A.apnt_ymd like "2022-04-13%" and apnt_cncl_yn = "N" and A.mcdp_cd = "CS"
order by A.apnt_ymd