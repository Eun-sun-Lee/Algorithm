# select WRITER_ID, sum(PRICE)
# from USED_GOODS_BOARD
# where STATUS = 'DONE'

select u.USER_ID, u.NICKNAME, b.TOTAL_SALES
from USED_GOODS_USER u join 
(select WRITER_ID, sum(PRICE) TOTAL_SALES
# case when sum(PRICE) >= 700000 then sum(PRICE) end TOTAL_SALES
from USED_GOODS_BOARD
where STATUS = 'DONE'
group by WRITER_ID
) b
on u.USER_ID = b.WRITER_ID
where b.TOTAL_SALES >= 700000
order by b.TOTAL_SALES asc