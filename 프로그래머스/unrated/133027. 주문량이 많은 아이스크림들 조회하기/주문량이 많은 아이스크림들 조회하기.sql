-- 코드를 입력하세요
select F.flavor
from first_half F
group by F.flavor
order by sum(F.total_order + (select sum(J.total_order)
                                            from July J
                                            where J.flavor = F.flavor)) desc limit 3
