-- 코드를 입력하세요
SELECT title, reply.board_id, reply.reply_id, reply.writer_id, reply.contents, reply.created_date
from Used_Goods_Reply as reply
    join Used_Goods_Board as board
        on board.board_id = reply.board_id
where board.created_date between '2022-10-01' and '2022-10-30'
order by reply.created_date, title