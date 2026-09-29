import logging
from transform import Order

logger = logging.getLogger(__name__)

def load_orders(orders: list[Order], connection) -> int:
    count = 0
    for order in orders:
        connection.execute(
            """
            insert into orders (order_id, customer_id, total_amount, status)
            values (%s, %s, %s, %s)
            on conflict (order_id)
            do update set total_amount = excluded.total_amount, status = excluded.status
            """,
            (order.order_id, order.customer_id, order.total_amount, order.status)
        )
        count += 1
    logger.info(f"Inserted {count} orders")
    return count