select 
order_id, customer_id, 
order_date :: date as order_date,
status,
total_amount
from {{source('ecommerce', 'orders')}}