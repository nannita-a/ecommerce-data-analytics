from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

CSV_FILES = [
    "customer_dim.csv",
    "fact_table.csv",
    "item_dim.csv",
    "store_dim.csv",
    "time_dim.csv",
    "Trans_dim.csv",
]

def main():
    for file_name in CSV_FILES:
        file_path = DATA_DIR / file_name

        if not file_path.exists():
            print(f"No se encontró: {file_path}")
            continue

        inspect_csv(file_path)

    validate_keys()
    validate_business_rules()


def inspect_csv(file_path: Path):
    print("=" * 80)
    print(f"ARCHIVO: {file_path.name}")
    print("=" * 80)

    df = pd.read_csv(file_path, encoding="latin-1")

    print(f"\nFilas: {len(df):,}")
    print(f"Columnas: {len(df.columns)}")

    print("\nCOLUMNAS:")
    for column in df.columns:
        print(f"- {column}")

    print("\nTIPOS DE DATOS:")
    print(df.dtypes)

    print("\nVALORES NULOS:")
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]

    if nulls.empty:
        print("No se encontraron valores nulos.")
    else:
        print(nulls)

    print("\nFILAS DUPLICADAS:")
    print(df.duplicated().sum())

    print("\nPRIMEROS 5 REGISTROS:")
    print(df.head())

    print("\n")


def validate_keys():
    print("=" * 80)
    print("VALIDACIÓN DE CLAVES E INTEGRIDAD REFERENCIAL")
    print("=" * 80)

    customers = pd.read_csv(
        DATA_DIR / "customer_dim.csv",
        encoding="latin-1"
    )

    facts = pd.read_csv(
        DATA_DIR / "fact_table.csv",
        encoding="latin-1"
    )

    items = pd.read_csv(
        DATA_DIR / "item_dim.csv",
        encoding="latin-1"
    )

    stores = pd.read_csv(
        DATA_DIR / "store_dim.csv",
        encoding="latin-1"
    )

    times = pd.read_csv(
        DATA_DIR / "time_dim.csv",
        encoding="latin-1"
    )

    payments = pd.read_csv(
        DATA_DIR / "Trans_dim.csv",
        encoding="latin-1"
    )

    dimensions = [
        ("customer_dim", customers, "coustomer_key"),
        ("item_dim", items, "item_key"),
        ("store_dim", stores, "store_key"),
        ("time_dim", times, "time_key"),
        ("Trans_dim", payments, "payment_key"),
    ]

    print("\nUNICIDAD DE CLAVES:")

    for name, df, key in dimensions:
        duplicated_keys = df[key].duplicated().sum()
        null_keys = df[key].isnull().sum()

        print(
            f"{name}.{key}: "
            f"duplicadas={duplicated_keys}, "
            f"nulas={null_keys}"
        )

    relationships = [
        ("coustomer_key", customers["coustomer_key"]),
        ("item_key", items["item_key"]),
        ("store_key", stores["store_key"]),
        ("time_key", times["time_key"]),
        ("payment_key", payments["payment_key"]),
    ]

    print("\nINTEGRIDAD REFERENCIAL:")

    for fact_key, dimension_keys in relationships:
        missing = ~facts[fact_key].isin(dimension_keys)
        missing_count = missing.sum()

        print(
            f"fact_table.{fact_key}: "
            f"{missing_count} referencias inexistentes"
        )

        if missing_count > 0:
            examples = (
                facts.loc[missing, fact_key]
                .drop_duplicates()
                .head(10)
                .tolist()
            )

            print(f"  Ejemplos: {examples}")


def validate_business_rules():
    print("\n" + "=" * 80)
    print("VALIDACIÓN DE REGLAS DE NEGOCIO")
    print("=" * 80)

    facts = pd.read_csv(
        DATA_DIR / "fact_table.csv",
        encoding="latin-1"
    )

    times = pd.read_csv(
        DATA_DIR / "time_dim.csv",
        encoding="latin-1"
    )

    expected_total = facts["quantity"] * facts["unit_price"]

    invalid_totals = (
        (facts["total_price"] - expected_total)
        .abs()
        .gt(0.01)
        .sum()
    )

    invalid_quantity = (facts["quantity"] <= 0).sum()
    invalid_unit_price = (facts["unit_price"] < 0).sum()
    invalid_total_price = (facts["total_price"] < 0).sum()

    invalid_month = (~times["month"].between(1, 12)).sum()

    valid_quarters = ["Q1", "Q2", "Q3", "Q4"]
    invalid_quarter = (~times["quarter"].isin(valid_quarters)).sum()

    print(f"Totales inconsistentes: {invalid_totals}")
    print(f"Cantidad <= 0: {invalid_quantity}")
    print(f"Precio unitario negativo: {invalid_unit_price}")
    print(f"Precio total negativo: {invalid_total_price}")
    print(f"Meses fuera de 1-12: {invalid_month}")
    print(f"Quarters inválidos: {invalid_quarter}")


if __name__ == "__main__":
    main()

    