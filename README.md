# Repositório para teste de máquina virtual Azure e conexão com banco de dados SQL Server Azure

#### Por questões de segurança a conexão com o banco de dados foi realizada em outro arquivo conexao.py que não foi colocado no repositório, mas a conexão foi feita 
#### através da  API PYODBC usando os seguintes comandos:

```
import pyodbc

def conectar():
    server = <servidor>
    database = <banco-de-dados>
    username = <username>
    password = <senha>
    return pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
```

###### Os arquivos ainda precisam de melhoras, posteriormente pretendo adicionar a biblioteca pandas e o SQLAlchemy que é uma API de mapeamento objeto-relacional e ###### permite trabalhar com os bancos relacionais e Python de melhor forma e se relaciona muito bem com o pandas. 
    
