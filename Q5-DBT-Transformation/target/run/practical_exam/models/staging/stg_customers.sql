
  create view "exam"."public"."stg_customers__dbt_tmp"
    
    
  as (
    select
    customer_id,
    first_name,
    last_name,
    email,
    country
from "exam"."ecommerce"."customers"
  );