import lib
import csv_sistema
import conexao
import uuid
import pyodbc


def localiza_cliente():
    lib.limpar_tela()
    
    conn = conexao.conectar()
    cursor = conn.cursor()

    indice = input("Digite o indice de qual cliente você deseja selecionar:\n")
    query = f"SELECT id FROM clientes WHERE id = ?"
    
    cursor.execute(query, indice)
    
    id = cursor.fetchone()[0]
    
    conn.close()

    return id
    



def listar():
    lib.limpar_tela();

    conn = conexao.conectar()
    cursor = conn.cursor()

    table_name = 'clientes'
    select_all = f"SELECT * FROM {table_name}"

    cursor.execute(select_all)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

    input("Digite enter para continuar...")
    lib.limpar_tela()
    
def cadastrar():
    lib.limpar_tela()
    conn = conexao.conectar() 
    cursor = conn.cursor()

    table_name = 'clientes'

    create_table = (f"""
    IF OBJECT_ID('{table_name}', 'U') IS NULL
    BEGIN
        CREATE TABLE {table_name} (
            id INT IDENTITY(1,1) PRIMARY KEY,
            nome VARCHAR(50),
            telefone VARCHAR(50),
            email VARCHAR(50)
            );
    END
        """)

    cursor.execute(create_table)
    
    nome = input("Digite o nome do cliente:")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    
    
    conn.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", nome, telefone, email)
    

    conn.commit()
    lib.mensagem("Cliente cadastrado com sucesso")
    conn.close()
    input("Digite enter para continuar...")
    lib.limpar_tela()
        
        