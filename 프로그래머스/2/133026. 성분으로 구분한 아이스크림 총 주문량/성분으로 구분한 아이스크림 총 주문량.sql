-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE, sum(f.total_order) TOTAL_ORDER
from FIRST_HALF f, ICECREAM_INFO i
where f.flavor = i.flavor
group by i.INGREDIENT_TYPE