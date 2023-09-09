-- 코드를 입력하세요
SELECT A.author_id, A.author_name, B.category, sum(B.price * S.sales) as total_sales
from book_sales S
inner join book B on S.book_id = B.book_id
inner join author A on B.author_id = A.author_id
where year(S.sales_date) = 2022 and month(S.sales_date) = 1
group by A.author_id, B.category
order by A.author_id, B.category desc