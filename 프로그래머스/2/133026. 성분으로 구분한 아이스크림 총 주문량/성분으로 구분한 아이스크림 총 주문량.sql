select INGREDIENT_TYPE, sum(TOTAL_ORDER)
from ICECREAM_INFO i join FIRST_HALF f using (FLAVOR)
group by INGREDIENT_TYPE
order by 1 desc, 2