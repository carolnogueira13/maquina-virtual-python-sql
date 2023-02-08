# Programa para pegar entradas de dados do usuário (input) e exportar para um banco de dados 

import lib
import cadastro_cliente
import cadastro_pedido
import conexao

print("-" * 100)
print("Bem vindo ao programa para pedidos de clientes")
print("-" * 100)

print("Inicialmente iremos realizar a sua conexão com o banco de dados!")
coon = conexao.conectar()

print("Conexão bem-sucedida!")


while(True):
    opcao = str(input("""--------------------------------
    [1] Cadastrar de clientes
    [2] Listar clientes
    [3] Cadastrar pedidos
    [4] Listar pedidos 
    [5] Sair
>>>>Insira a sua opção: """))
    

    if opcao == "1":
        cadastro_cliente.cadastrar()
    elif opcao == "2":
        cadastro_cliente.listar()
    elif opcao == "3":
        cadastro_pedido.cadastrar()
    elif opcao == "4":
        cadastro_pedido.listar()
    elif opcao == "5":
        break
    else:
        lib.mensagem("Opcao inválida")
    
    lib.limpar_tela()
    
    
    
        