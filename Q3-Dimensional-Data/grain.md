### State the grain of every fact table and identify additive/semi-additive measures where relevant.

- Fact table : fact_orders
The grain of this table is (ONE ROW PER ORDER). At the moment, every row represents a single order.

- Fact table : fact_order_items
The grain of this table is (ONE ROW PER LINE WITHIN AN ORDER). 
One row can represent multiple lines within an order.

- Additive measure 
fact_orders.total_amount: fully additive (sum across any rows)
fact_order_items.price: fully additive (sum across any rows)

There is no semi additive measure in this table because both are transaction fact tables.

