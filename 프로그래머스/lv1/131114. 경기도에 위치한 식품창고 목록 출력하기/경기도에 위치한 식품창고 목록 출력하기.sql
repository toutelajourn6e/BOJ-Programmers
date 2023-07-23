-- 코드를 입력하세요
SELECT warehouse_id,
        warehouse_name,
        address,
        case 
        when freezer_yn is NULL then "N"
        else freezer_yn end as freezer_yn
from food_warehouse
where left(address, 3) = '경기도'
order by warehouse_id
                                        