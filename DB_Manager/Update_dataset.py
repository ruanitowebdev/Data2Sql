from . Connect_database import connect
from . dtypeTransform import dtype_columns
from . getElement import getbase
from . ReadDataset import read_dataset
from . dropduplicated import drop_duplicated

def Update_data(table_name, config):
    element_table = getbase(table_name, config=config)
    schemadb = element_table.get("schema_db")
    print(f"schema: {schemadb}")
    df = read_dataset(element_table)
    dtypes = dtype_columns(element_table)
    engine = connect()
    drop_duplicated(df=df, engine=engine, element_table=element_table)
    with engine.connect() as conn:
        df.to_sql(
            name= element_table.get("Tablename"),
            con= conn,
            schema=schemadb,
            if_exists='append',
            index=False,
            dtype=dtypes
        )