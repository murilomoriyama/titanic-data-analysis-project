'''
Exibir o cabeçalho com os nomes das colunas (ex: Name, Age, Survived).
Permitir visualizar os primeiros N passageiros (ex: as 5 primeiras linhas).
Listar todos os dados de forma organizada. FEITO
'''

def visualizar_cabecalho(cabecalho):
    print(cabecalho)

def visualizar_conteudo(dados):
    N = int(input("Insira quantos passageiros quer ver: "))

    if N > len(dados):
        N = len(dados)

    for i in range (N):
        print(dados[i])
