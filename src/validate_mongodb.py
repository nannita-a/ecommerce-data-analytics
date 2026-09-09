from pathlib import Path

import pandas as pd
from pymongo import MongoClient


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "ecommerce_analytics"


FILES_COLLECTIONS = [
    ("customer_dim.csv", "customers"),
    ("item_dim.csv", "items"),
    ("store_dim.csv", "stores"),
    ("time_dim.csv", "times"),
    ("Trans_dim.csv", "payments"),
    ("fact_table.csv", "sales"),
]


def get_csv_count(file_name):
    file_path = DATA_DIR / file_name

    return len(
        pd.read_csv(
            file_path,
            encoding="latin-1"
        )
    )


def main():
    client = MongoClient(MONGODB_URI)

    try:
        client.admin.command("ping")
        print("Conexión a MongoDB correcta.\n")

        db = client[DATABASE_NAME]

        print("=" * 70)
        print("VALIDACIÓN CSV VS MONGODB")
        print("=" * 70)

        all_valid = True

        for file_name, collection_name in FILES_COLLECTIONS:
            csv_count = get_csv_count(file_name)
            mongo_count = db[collection_name].count_documents({})

            valid = csv_count == mongo_count

            status = "OK" if valid else "ERROR"

            print(
                f"{collection_name:<12} "
                f"CSV={csv_count:>10,} | "
                f"MongoDB={mongo_count:>10,} | "
                f"{status}"
            )

            if not valid:
                all_valid = False

        print()

        if all_valid:
            print("La carga mantiene la cantidad de registros correctamente.")
        else:
            print("Se encontraron diferencias entre los CSV y MongoDB.")

    finally:
        client.close()


if __name__ == "__main__":
    main()