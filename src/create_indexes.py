from pymongo import MongoClient


MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "ecommerce_analytics"


def main():
    client = MongoClient(MONGODB_URI)

    try:
        client.admin.command("ping")
        print("Conexión a MongoDB correcta.\n")

        db = client[DATABASE_NAME]

        print("Creando índices únicos en dimensiones...")

        db.customers.create_index(
            "customer_key",
            unique=True,
            name="ux_customers_customer_key"
        )

        db.items.create_index(
            "item_key",
            unique=True,
            name="ux_items_item_key"
        )

        db.stores.create_index(
            "store_key",
            unique=True,
            name="ux_stores_store_key"
        )

        db.times.create_index(
            "time_key",
            unique=True,
            name="ux_times_time_key"
        )

        db.payments.create_index(
            "payment_key",
            unique=True,
            name="ux_payments_payment_key"
        )

        print("Índices únicos creados correctamente.\n")

        print("Creando índices en sales...")

        db.sales.create_index(
            "customer_key",
            name="ix_sales_customer_key"
        )

        db.sales.create_index(
            "item_key",
            name="ix_sales_item_key"
        )

        db.sales.create_index(
            "store_key",
            name="ix_sales_store_key"
        )

        db.sales.create_index(
            "time_key",
            name="ix_sales_time_key"
        )

        db.sales.create_index(
            "payment_key",
            name="ix_sales_payment_key"
        )

        print("Índices de sales creados correctamente.")

    finally:
        client.close()


if __name__ == "__main__":
    main()