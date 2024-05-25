# SELECT date_format(online_sale.SALES_DATE, '%Y-%m-%d') SALES_DATE, online_sale.PRODUCT_ID, online_sale.USER_ID, online_sale.SALES_AMOUNT
# from online_sale left join offline_sale on online_sale.PRODUCT_ID=offline_sale.PRODUCT_ID and online_sale.SALES_DATE=offline_sale.SALES_DATE
# where YEAR(online_sale.SALES_DATE) = 2022 AND MONTH(online_sale.SALES_DATE) = 3
# order by SALES_DATE, PRODUCT_ID, USER_ID 

select date_format(sales_date, '%Y-%m-%d') sales_date, product_id, user_id, sales_amount
from online_sale
where YEAR(sales_date) = 2022 AND MONTH(sales_date) = 3

union all

select date_format(sales_date, '%Y-%m-%d') sales_date, product_id, null as user_id, sales_amount
from offline_sale
where YEAR(sales_date) = 2022 AND MONTH(sales_date) = 3

order by sales_date, product_id, user_id