import pandas as pd
import os

os.makedirs("output", exist_ok=True)

orders = pd.read_csv("orders.csv", parse_dates=["order_purchase_timestamp"])
orders["order_year"] = orders["order_purchase_timestamp"].dt.year
orders["order_month"] = orders["order_purchase_timestamp"].dt.month

orders.to_parquet(
    "output/orders.parquet",
    engine="pyarrow",
    index=False
)

