"""
Módulo responsável pela visualização dos dados do conjunto Titanic.
Contém funções para exibir o cabeçalho e visualizar parte do conteúdo
da base de dados.
"""

def visualizar_cabecalho(cabecalho):
    """
    Exibe o cabeçalho da tabela de dados.

    Parâmetros:
    - cabecalho (list): Lista contendo os nomes das colunas do arquivo CSV.

    Retorno:
    - None: Exibe o cabeçalho na tela.
    """

    print(cabecalho)


def visualizar_conteudo(dados):
    """
    Exibe os primeiros registros da base de dados.

    Solicita ao usuário a quantidade de passageiros que deseja visualizar.
    Caso o valor informado seja maior que a quantidade de registros,
    exibe todos os passageiros disponíveis.

    Parâmetros:
    - dados (list): Lista de listas contendo os dados dos passageiros.

    Retorno:
    - None: Exibe os registros solicitados na tela.
    """

    N = int(input("Insira quantos passageiros quer ver: "))

    if N > len(dados):
        N = len(dados)

    for i in range(N):
        print(dados[i])
