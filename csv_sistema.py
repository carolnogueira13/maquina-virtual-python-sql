import csv

def ler(nome_do_arquivo):
    dados = []
    with open(nome_do_arquivo, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados.append(dict(row))
    return dados

def salvar(lista, nome_do_arquivo):
    with open(nome_do_arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista[0].keys())
        writer.writeheader()
        for item in lista:
            writer.writerow(item)

def busca_por_id(id, nome_do_arquivo):
    dados = ler(nome_do_arquivo)
    return next((item for item in dados if item['id'] == id), None)
