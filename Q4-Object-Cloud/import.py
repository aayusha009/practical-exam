import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:2213@localhost:5432/postgres")
df = pd.read_csv("orders.csv")
df.to_sql("orders", engine, if_exists="replace", index=False)

