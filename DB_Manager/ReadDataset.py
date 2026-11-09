import pandas as pd

from pathlib import Path

'''aceita csvs e arquivos xlsx'''

def read_dataset(element_table):
    path = Path(element_table.get("localPath"))
    date_column  = element_table.get("Keycolumn")
    extensao = path.suffix.lower()
    if(extensao == ".csv"):
        
        df = pd.read_csv(path, encoding="utf-8" , low_memory=False)
        df[date_column] = pd.to_datetime(df[date_column])
    if(extensao == ".xls"):
        df = pd.read_excel(path , encoding="utf-8" , low_memory=False)
        df[date_column] = pd.to_datetime(df[date_column])
    return df