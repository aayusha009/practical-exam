import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class Order:
    order_id: int
    customer_id: int
    total_amount: float
    status: str

def transform_orders(raw_orders: list[dict]) -> list[Order]:
    clean = []
    for row in raw_orders:
        try:
            clean.append(Order(
                order_id=int(row["order_id"]),
                customer_id=int(row["customer_id"]),
                total_amount=float(row["total_amount"]),
                status=str(row["status"]),
            ))
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Skipping bad row: {e}")
    return clean