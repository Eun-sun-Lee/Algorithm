select i.NAME, i.DATETIME
from ANIMAL_INS i left join ANIMAL_OUTS o using (ANIMAL_ID)
# where i.ANIMAL_ID <> o.ANIMAL_ID
where i.ANIMAL_ID NOT IN (select ANIMAL_ID from ANIMAL_OUTS)
order by i.DATETIME
limit 3

