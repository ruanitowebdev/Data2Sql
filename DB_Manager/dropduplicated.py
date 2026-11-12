
from sqlalchemy import text
import pandas as pd

def drop_duplicated(df, engine, element_table):

    key_column = element_table.get("Keycolumn")
    schema = element_table.get("schema_db")
    table = element_table.get("Tablename")

    # Montagem dos identificadores SQL
    table_name = f"[{schema}].[{table}]"
    column_name = f"[{key_column}]"

    # Conversão das datas
    df[key_column] = pd.to_datetime(
        df[key_column],
        errors="coerce"
    )

    date_min = df[key_column].min()
    date_max = df[key_column].max()

    if pd.isna(date_min) or pd.isna(date_max):
        raise ValueError("Não existem datas válidas no DataFrame.")

    print("Data mínima:", date_min)
    print("Data máxima:", date_max)

    # Consulta SQL
    sql_drop_duplicated = text(f"""
        DELETE FROM {table_name}
        WHERE {column_name} >= :data_min
          AND {column_name} < :data_max
    """)

    with engine.begin() as conn:
        result = conn.execute(
            sql_drop_duplicated,
            {
                "data_min": date_min.to_pydatetime(),
                "data_max": (
                    date_max + pd.Timedelta(days=1)
                ).to_pydatetime()
            }
        )
        conn.commit()

    print(f"Registros removidos: {result.rowcount}")
