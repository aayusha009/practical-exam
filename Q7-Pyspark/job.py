

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

ORDERS_PATH = "orders.parquet"
CUSTOMERS_PATH = "customers.csv"
OUTPUT_PATH = "output/orders_by_state_month"


def main():
    spark = (
        SparkSession.builder
        .appName("q7-orders-aggregation")
        .master("local[*]")
       
    )

    orders = spark.read.parquet(ORDERS_PATH)

    customers = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(CUSTOMERS_PATH)
        .select("customer_id", "customer_state")
    )

   