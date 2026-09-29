select
    o.order_id,
    o.customer_id,
    o.order_date,
    c.country,
    o.total_amount
from "exam"."public"."stg_orders" o
left join "exam"."public"."stg_customers" c on o.customer_id = c.customer_id