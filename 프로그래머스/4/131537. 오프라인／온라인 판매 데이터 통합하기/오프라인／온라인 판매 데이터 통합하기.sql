# select f.SALES_DATE, PRODUCT_ID, USER_ID, f.SALES_AMOUNT
# from ONLINE_SALE n right join OFFLINE_SALE f using (PRODUCT_ID)
# # where MONTH(SALES_DATE) = 3
# order by f.SALES_DATE asc, PRODUCT_ID asc, USER_ID asc

select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE n 
where YEAR(SALES_DATE) = 2022 and MONTH(SALES_DATE) = 3
# order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc
UNION ALL
select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') , PRODUCT_ID, null USER_ID, SALES_AMOUNT
from OFFLINE_SALE f
where YEAR(SALES_DATE) = 2022 and MONTH(SALES_DATE) = 3
order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc