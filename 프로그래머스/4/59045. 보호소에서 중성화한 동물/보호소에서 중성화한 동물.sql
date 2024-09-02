select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o using (ANIMAL_ID)
where o.SEX_UPON_OUTCOME NOT LIKE 'Intact %' and i.SEX_UPON_INTAKE LIKE 'Intact %'
order by i.ANIMAL_ID

