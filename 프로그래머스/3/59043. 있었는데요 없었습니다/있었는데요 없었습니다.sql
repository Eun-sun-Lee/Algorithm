-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.NAME
from ANIMAL_INS i, ANIMAL_OUTS o
where i.ANIMAL_ID = o.ANIMAL_ID and i.datetime > o.datetime
order by i.datetime 