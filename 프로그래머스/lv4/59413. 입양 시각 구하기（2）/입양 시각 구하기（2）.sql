-- 코드를 입력하세요
with recursive cte as (
    select 0 as n
    union all
    select n + 1 from cte where n < 23
)

select cte.n as hour,
        case when O.datetime is Null then 0
        else count(*) end as count
from cte
left join animal_outs O on hour(O.datetime) = cte.n
group by cte.n