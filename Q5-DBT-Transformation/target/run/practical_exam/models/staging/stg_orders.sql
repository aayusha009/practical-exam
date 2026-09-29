
  create view "exam"."public"."stg_orders__dbt_tmp"
    
    
  as (
    select
    order_id,
    customer_id,
    order_date,
    order_status,
    total_amount
from "exam"."ecommerce"."orders"
  );