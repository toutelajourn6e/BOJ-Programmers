-- 코드를 입력하세요
SELECT concat('/home/grep/src/', B.board_id, '/', F.file_id, F.file_name, F.file_ext) as FILE_PATH
from used_goods_board B
inner join used_goods_file F on B.board_id = F.board_id
where B.board_id = (select board_id
                   from used_goods_board
                   order by views desc limit 1)
order by F.file_id desc