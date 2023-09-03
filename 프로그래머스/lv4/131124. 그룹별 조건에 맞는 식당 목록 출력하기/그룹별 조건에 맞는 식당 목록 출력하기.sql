-- 코드를 입력하세요
SELECT M.member_name, R.review_text, date_format(R.review_date, '%Y-%m-%d') as review_date
from member_profile M
inner join rest_review R on M.member_id = R.member_id
where M.member_id = (select member_id 
                    from rest_review
                    group by member_id
                    order by count(*) desc limit 1)
order by R.review_date, R.review_text