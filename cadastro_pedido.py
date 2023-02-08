import lib
import csv_sistema
import cadastro_cliente
import uuid
import conexao

nome_do_arquivo = "pedidos.csv"

def listar():
    lib.limpar_tela();

    conn = conexao.conectar()
    cursor = conn.cursor()

    table_name = 'pedidos'
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

    cliente = cadastro_cliente.localiza_cliente()
    
    conn = conexao.conectar() 
    cursor = conn.cursor()

    table_name = 'pedidos'

    create_table = (f"""
    IF OBJECT_ID('{table_name}', 'U') IS NULL
    BEGIN
        CREATE TABLE {table_name} (
            id INT IDENTITY(1,1) PRIMARY KEY,
            id_cliente INT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes (id),
            produto VARCHAR(50),
            quantidade INT,
            valor FLOAT,
            valor_total FLOAT 
            );
    END
        """)

    cursor.execute(create_table)

    produto = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade: ")
    valor = float(input("Digite o valor: "))
    valor_total = float(quantidade) * valor

    conn.execute("INSERT INTO pedidos (id_cliente, produto, quantidade, valor, valor_total) VALUES (?, ?, ?, ?, ?)", cliente, produto, quantidade, valor, valor_total)

    conn.commit()
        
    lib.mensagem("Pedido cadastrado com sucesso")
    input("Digite enter para continuar...")
    lib.limpar_tela()
    
    