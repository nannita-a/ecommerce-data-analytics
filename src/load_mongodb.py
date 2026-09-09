from pathlib import Path
import pandas as pd
from pymongo import MongoClient


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "ecommerce_analytics"


def read_csv(file_name):
    file_path = DATA_DIR / file_name
    return pd.read_csv(file_path, encoding="latin-1")


def dataframe_to_records(df):
    return df.where(pd.notnull(df), None).to_dict("records")


def load_collection(db, collection_name, df, batch_size=10000):
    collection = db[collection_name]

    collection.delete_many({})

    total_rows = len(df)

    for start in range(0, total_rows, batch_size):
        end = start + batch_size

        batch = df.iloc[start:end]
        records = dataframe_to_records(batch)

        if records:
            collection.insert_many(records)

        print(
            f"{collection_name}: "
            f"{min(end, total_rows):,}/{total_rows:,}"
        )

    print(f"{collection_name}: carga completada")


def main():
    client = MongoClient(MONGODB_URI)

    try:
        client.admin.command("ping")
        print("Conexión a MongoDB correcta.")

        db = client[DATABASE_NAME]

        customers = read_csv("customer_dim.csv")
        items = read_csv("item_dim.csv")
        stores = read_csv("store_dim.csv")
        times = read_csv("time_dim.csv")
        payments = read_csv("Trans_dim.csv")
        sales = read_csv("fact_table.csv")

        customers = customers.rename(
            columns={
                "coustomer_key": "customer_key"
            }
        )

        items = items.rename(
            columns={
                "desc": "description",
                "man_country": "manufacturing_country"
            }
        )

        payments = payments.rename(
            columns={
                "trans_type": "transaction_type"
            }
        )

        sales = sales.rename(
            columns={
                "coustomer_key": "customer_key"
            }
        )

        times["date"] = pd.to_datetime(
            times["date"],
            format="%d-%m-%Y %H:%M"
        )

        load_collection(db, "customers", customers)
        load_collection(db, "items", items)
        load_collection(db, "stores", stores)
        load_collection(db, "times", times)
        load_collection(db, "payments", payments)
        load_collection(db, "sales", sales)

        print("\nCarga completada correctamente.")

    finally:
        client.close()


if __name__ == "__main__":
    main()