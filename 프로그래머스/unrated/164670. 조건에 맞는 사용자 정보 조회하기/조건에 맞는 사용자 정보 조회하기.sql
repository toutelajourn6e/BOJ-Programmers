-- 코드를 입력하세요
SELECT U.user_id, U.nickname, concat(U.city, ' ', street_address1, ' ', street_address2) as '전체주소',
        concat(left(U.tlno, 3), '-', substr(U.tlno, 4, 4), '-', right(U.tlno, 4)) as '전화번호'
from used_goods_board B
    inner join used_goods_user U on B.writer_id = U.user_id
group by U.user_id
having count(*) >= 3
order by U.user_id desc