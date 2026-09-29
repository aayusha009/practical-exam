import os
import time
import logging

import psycopg2

from extract import ExtractConfig, extract_orders
from transform import transform_orders
from load import load_orders

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.environ["DATABASE_URL"]
EXTRACT_URL = os.environ.get("EXTRACT_URL", "https://api.example.com/orders")

CREATE_TABLE_SQL = """
create table if not exists orders (
    order_id integer primary key,
    customer_id integer not null,
    total_amount numeric not null,
    status text not null
)
"""


class PgConnection:
    """Thin wrapper so load.py's connection.execute(sql, params) works with psycopg2,
    which normally needs a cursor rather than executing directly off the connection."""

    def __init__(self, conn):
        self._conn = conn

    def execute(self, sql, params=None):
        with self._conn.cursor() as cur:
            cur.execute(sql, params)
        self._conn.commit()


def wait_for_db(dsn, max_attempts=10, delay=3):
    """docker-compose's depends_on only waits for the postgres CONTAINER to start,
    not for postgres itself to be ready to accept connections. Without this retry
    loop, the pipeline container can crash on startup because it tries to connect
    before postgres has finished initializing."""
    for attempt in range(1, max_attempts + 1):
        try:
            return psycopg2.connect(dsn)
        except psycopg2.OperationalError as e:
            logger.info(f"Database not ready yet (attempt {attempt}/{max_attempts}): {e}")
            time.sleep(delay)
    raise RuntimeError("Could not connect to database after retries")


def main():
    raw_conn = wait_for_db(DATABASE_URL)
    conn = PgConnection(raw_conn)
    conn.execute(CREATE_TABLE_SQL)

    config = ExtractConfig(url=EXTRACT_URL)
    raw_orders = extract_orders(config)
    orders = transform_orders(raw_orders)
    count = load_orders(orders, conn)
    logger.info(f"Pipeline complete: loaded {count} orders")


if __name__ == "__main__":
    main()
