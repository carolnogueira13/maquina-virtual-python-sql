import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def espera(segundos = 3):
    time.sleep(segundos)

def mensagem(mensagem):
    limpar_tela()
    print(mensagem)

def tuple_to_dict(tup):
    # função para transformar uma lista de tupla em uma lista de dicionários
    return {'id': tup[0], 'nome': tup[1], 'telefone': tup[2], 'email': tup[3]}