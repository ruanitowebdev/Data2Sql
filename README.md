# Data2Sql
Automatização da inserção e atualização de dados em bancos SQL Server a partir de arquivos CSV e Excel (XLSX), utilizando configurações centralizadas em JSON para mapear colunas, definir tipos de dados, schemas e estratégias de atualização. Desenvolvido em Python com Pandas, SQLAlchemy e PyODBC.
Data2SQL – Data Ingestion & Database Manager
Sobre o projeto

O Data2SQL é uma ferramenta desenvolvida em Python com o objetivo de simplificar e automatizar os processos de inserção, atualização e gerenciamento de dados em bancos de dados SQL Server, utilizando arquivos CSV e Excel (XLSX) como fontes de dados.

A proposta é centralizar as configurações de cada tabela em arquivos JSON, eliminando a necessidade de implementar códigos específicos para cada conjunto de dados.

Dessa forma, o usuário define as características da tabela, o caminho do arquivo de origem, o mapeamento das colunas e os tipos de dados. A execução é controlada por um arquivo principal (main.py), responsável por identificar e executar o processamento da tabela desejada.

Objetivos
Automatizar a ingestão de dados provenientes de arquivos CSV e XLSX.
Centralizar as configurações de processamento em arquivos JSON.
Facilitar a criação e atualização de tabelas no SQL Server.
Padronizar o mapeamento e a conversão dos tipos de dados.
Reduzir a necessidade de scripts específicos para cada tabela.
Facilitar a manutenção e expansão do processo de ingestão.
Arquitetura

O projeto utiliza uma arquitetura modular, separando as configurações da lógica de processamento.

1. Configuração JSON

Cada tabela possui suas próprias configurações, incluindo:

Nome da tabela e schema de destino.
Caminho do arquivo de origem.
Coluna-chave utilizada no processo de atualização.
Mapeamento das colunas.
Definição dos tipos de dados.

2. Módulos de processamento

Responsáveis pelas diferentes etapas da ingestão:

Leitura dos arquivos CSV e XLSX.
Transformação e padronização dos dados.
Conversão dos tipos de dados.
Conexão com o SQL Server.
Inserção e atualização dos registros.
Remoção de registros duplicados ou existentes no período de atualização.

3. Main.py

Arquivo principal responsável por controlar a execução, selecionar a tabela que será processada e encaminhar suas configurações para os módulos correspondentes.

Exemplo de configuração JSON
json
{
    "Tablename": "vendastech2",
    "Keycolumn": "Data",
    "schema_db": "dt",
    "localPath": "C:/dados/vendas_tech.csv",

    "Coluuns_mapping": {
        "ID_Pedido": "ID_Pedido",
        "Data": "datetime",
        "Loja": "Loja",
        "Produto": "Produto",
        "Preco_Unitario": "Preco_Unitario",
        "Qtd": "Qtd",
        "Cliente": "Cliente",
        "Data_Base": "Data_Base"
    }
}

Tecnologias utilizadas
Python: linguagem principal do projeto.
Pandas: leitura, manipulação e transformação dos dados.
SQLAlchemy: gerenciamento das operações e conexões com o banco de dados.
PyODBC: comunicação com o Microsoft SQL Server.
JSON: armazenamento das configurações de cada tabela.
Fluxo de funcionamento
O usuário define a configuração da tabela no arquivo JSON.
O main.py identifica qual tabela deverá ser processada.
O sistema localiza e lê o arquivo CSV ou XLSX.
Os dados são transformados conforme o mapeamento configurado.
O sistema estabelece conexão com o SQL Server.
Os registros existentes no intervalo de atualização são tratados.
Os novos dados são inseridos na tabela de destino.
Benefícios
Configuração independente da lógica de processamento.
Reutilização dos módulos para diferentes conjuntos de dados.
Facilidade para adicionar novas tabelas e fontes de dados.
Padronização do processo de ingestão.
Redução de código repetitivo.
Maior facilidade de manutenção e escalabilidade.
Público-alvo

O projeto é voltado para profissionais e estudantes de Engenharia de Dados, Análise de Dados e Desenvolvimento Python que precisam automatizar processos de ingestão e atualização de dados em bancos relacionais.

Data2SQL – Simplificando a integração entre arquivos de dados e bancos SQL Server.
