import pandas as pd 
import sqlite3 as sql # DOC: https://docs.python.org/3/library/sqlite3.html

# CONECTAR AO BD
connectDB = sql.connect('new.db')

# IMPORTAR A TABELA CSV + MODIFICAÇÕES
df = pd.read_csv("bd_data.csv", sep=',').drop("Unnamed: 0", axis=1)
df.index.name = "Index"

# INSIRA COMANDOS NO TERMINAL-INTERATIVO:



