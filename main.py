import json
from DB_Manager.Update_dataset import Update_data  
from  DB_Manager.Connect_database import connect
from  DB_Manager.dtypeTransform import dtype_columns
from  DB_Manager.getElement import getbase
from  DB_Manager.ReadDataset import read_dataset
from DB_Manager.dropduplicated import drop_duplicated
from sqlalchemy import text , select
import dotenv
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import gc  # Garbage Collector para liberar RAM

config = json.load(open("src/config.json" , encoding="utf-8"))



logging.basicConfig()
# (Configurações de log e banco mantidas...)

def processar_base_individual(config):
    """
    Função unitária que processa 1 base inteira.
    Isolada para rodar em thread ou sequencial com segurança.
    """
    logging.info(f"[{config['Tablename']}] Iniciando processamento...")
    
    df_raw = None
    df_clean = None
    
    try:
        # 1. Extração
        table_name = config["Tablename"]
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
            conn.commit()
        logging.info(f"[{config['Tablename']}] Sucesso!")
        return {"id": config["Tablename"], "status": "sucesso"}
        
    except Exception as e:
        # Captura qualquer erro interno da thread e loga explicitamente
        logging.error(f"[{config['Tablename']}] ERRO CRÍTICO: {str(e)}", exc_info=True)
        return {"id": config["Tablename"], "status": "erro", "detalhe": str(e)}
        
    finally:
        # BOA PRÁTICA PARA 17 BASES: Limpeza explícita de memória RAM
        del df_raw
        del df_clean
        gc.collect()


def executar_pipeline_concorrente():
    logging.info("=== INÍCIO DO PIPELINE ===")
    
    # Controla quantas bases rodam em paralelo (ex: max_workers=3 para não explodir a RAM)
    # Se quiser rodar 1 por 1 com segurança, mude max_workers para 1.
    MAX_WORKERS = 3 
    
    resultados = []
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Envia todas as tarefas para o executor
        future_to_base = {
            executor.submit(processar_base_individual, config)
            
        }
        
        # TRAVA DE ESPERA: O as_completed garante que a thread principal 
        # vai esperar cada tarefa terminar antes de prosseguir/encerrar.
        for future in as_completed(future_to_base):
            config = future_to_base[future]
            try:
                res = future.result()
                resultados.append(res)
            except Exception as exc:
                logging.error(f"A base {config.get['Tablename']} gerou uma exceção não tratada: {exc}")

    logging.info(f"=== PIPELINE FINALIZADO. Resumo: {resultados} ===")

if __name__ == "__main__":
    executar_pipeline_concorrente()