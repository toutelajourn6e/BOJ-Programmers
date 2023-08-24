-- 코드를 입력하세요
SELECT B.writer_id, U.nickname, sum(price) as total_sales
from (
    select * 
    from used_goods_board
    where status = 'DONE'
) as B
inner join used_goods_user U on B.writer_id = U.user_id
group by user_id
having sum(B.price) >= 700000
order by total_sales