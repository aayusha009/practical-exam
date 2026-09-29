/* monthly revenue*/

SELECT date_trunc('month', o.order_purchase_timestamp) as month,
sum(oi.price) as revenue from orders o
join order_items oi on o.order_id = oi.order_id
group by 1
order by 1;

/* top five products */

SELECT order_items.product_id, product_category_name, sum(order_items.price) as total_revenue
from order_items 
inner join products p on order_items.product_id = p.product_id
group by order_items.product_id, p.product_category_name
order by total_revenue desc
limit 5;

/* latest order per customer (used customer_unique_id) */

SELECT c.customer_unique_id, o.* from orders o 
JOIN customers c on o.customer_id = c.customer_id
order by o.order_purchase_timestamp desc;

/* rank customer ( on the basis of spending ) */

SELECT c.customer_unique_id, sum(order_items.price) as total_spending 
from orders o
inner join order_items on o.order_id = order_items.order_id
inner join customers c on o.customer_id = c.customer_id
group by c.customer_unique_id
order by total_spending desc;


/* deduplication */

SELECT distinct on (order_id)* from orders
order by order_id;

/* running totals */

SELECT o.order_id, c.customer_id, sum(oi.price) as order_total from 
orders o
inner join order_items oi on o.order_id = oi.order_id
join customers c on o.customer_id = c.customer_id
group by o.order_id, c.customer_id

/* sessionization, window functions */

WITH sess AS (
select c.customer_unique_id, o.order_purchase_timestamp FROM orders o 
    join customers c ON o.customer_id = c.customer_id
),
gaps AS (
SELECT customer_unique_id, order_purchase_timestamp, 
CASE 
when lag (order_purchase_timestamp) OVER(PARTITION BY customer_unique_id ORDER BY order_purchase_timestamp) is null
OR order_purchase_timestamp - LAG(order_purchase_timestamp) OVER(PARTITION BY customer_unique_id ORDER BY order_purchase_timestamp) > INTERVAL '15 days'
then 1 
else 0
end as new_sess_has_started
    from sess
)
SELECT * from gaps;


/* explain / analyze */

explain analyze 
select o.order_id from orders o 
join
order_items oi on o.order_id = oi.order_id;