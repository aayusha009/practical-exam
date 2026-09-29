select
    o.order_id,
    o.customer_id,
    o.order_date,
    c.country,
    o.total_amount
from {{ ref('stg_orders') }} o
left join {{ ref('stg_customers') }} c on o.customer_id = c.customer_id
