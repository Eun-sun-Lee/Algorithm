# select FLAVOR
# from(
# select h.SHIPMENT_ID, h.FLAVOR FLAVOR, h.TOTAL_ORDER + j.TOTAL_ORDER TOTAL_ORDER
# from FIRST_HALF h right join JULY j using (FLAVOR)
# order by TOTAL_ORDER desc
# limit 3
# ) A

select h.FLAVOR FLAVOR
from FIRST_HALF h left join 
(select FLAVOR, sum(TOTAL_ORDER) TOTAL_ORDER
from July 
group by FLAVOR)
j using(FLAVOR)
order by h.TOTAL_ORDER + j.TOTAL_ORDER desc
limit 3



