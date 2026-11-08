import pandas as pd

from pathlib import Path

'''aceita csvs e arquivos xlsx'''

def read_dataset(element_table):
    path = Path(element_table.get("localPath"))
    extensao = path.suffix.lower()
    if(extensao == ".csv"):
        
        df = pd.read_csv(path, encoding="utf-8" , low_memory=False)
    if(extensao == ".xls"):
            df = pd.read_excel(path , encoding="utf-8" , low_memory=False)
    return df