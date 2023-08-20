-- 코드를 입력하세요
SELECT B.category, sum(S.sales) as total_sales
from book B
    inner join book_sales S on B.book_id = S.book_id
where year(S.sales_date) = 2022 and month(S.sales_date) = 1
group by B.category
order by B.category