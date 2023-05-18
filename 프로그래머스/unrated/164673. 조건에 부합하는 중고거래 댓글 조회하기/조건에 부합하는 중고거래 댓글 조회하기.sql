select
        B.TITLE,
        B.BOARD_ID,
        R.REPLY_ID,
        R.WRITER_ID,
        R.CONTENTS,
        DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
        
from USED_GOODS_BOARD B

inner join USED_GOODS_REPLY R

on B.BOARD_ID = R.BOARD_ID

where YEAR(B.CREATED_DATE) = 2022 and MONTH(B.CREATED_DATE) = 10
order by R.CREATED_DATE, B.TITLE