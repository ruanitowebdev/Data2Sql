from sqlalchemy import Integer, String, Float, Boolean, DateTime, Numeric , Date

# Dicionário que mapeia strings do JSON para instâncias de tipos do SQLAlchemy
TYPE_MAPPING = {
    "int": Integer(),
    "integer": Integer(),
    "bigint": Integer(),
    "varchar": String(),
    "text": String(),
    "string": String(),
    "float": Float(),
    "numeric": Numeric(),
    "decimal": Numeric(),
    "bool": Boolean(),
    "boolean": Boolean(),
    "datetime": DateTime(),
    "date": Date()
}
def dtype_columns(element_table):
    columns_type = element_table.get("dtype",{})
    sql_dtype ={}
    

    for col_name , str_type in columns_type.items() :
        clean_type = str(str_type).lower().strip()
        sql_dtype[col_name] = TYPE_MAPPING.get(clean_type) 
    return sql_dtype

