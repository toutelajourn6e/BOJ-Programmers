-- 코드를 입력하세요
SELECT count(*) as users
from user_info
where (age between 20 and 29) and year(joined) = 2021