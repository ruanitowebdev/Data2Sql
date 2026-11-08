
'''seleciona o objeto Json que estamos referenciando 
para atualizar a tabela'''

def getbase(tablename, config):
    

    for  i in config:
        if i["Tablename"] == tablename:
            return i
    print("tabela não encontrada")
    
