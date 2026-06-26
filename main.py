from importacao import carregar_dados
from visualizacao import visualizar_cabecalho, visualizar_conteudo

cabecalho, matriz_dados = carregar_dados()

visualizar_cabecalho(cabecalho)
visualizar_conteudo(matriz_dados)
