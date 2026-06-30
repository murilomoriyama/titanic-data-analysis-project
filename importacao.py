
"""
Módulo responsável pela importação dos dados do Titanic.

Realiza a leitura do arquivo CSV contendo os dados dos
passageiros, separando o cabeçalho da matriz de dados para
utilização nas demais etapas do programa.

Módulos utilizados:
- os: Verifica a existência do arquivo informado.
- csv: Realiza a leitura do arquivo CSV.

Retorno:
- Cabeçalho e matriz de dados contendo as informações dos
  passageiros, ou None caso ocorra algum erro na leitura.
"""

import os
import csv

def carregar_dados(caminho_arquivo="train.csv"):
  def carregar_dados(caminho_arquivo="train.csv"):
    """
    Carrega os dados do arquivo CSV do Titanic.

    Verifica se o arquivo informado existe e realiza sua leitura,
    separando o cabeçalho dos demais registros. Em caso de erro,
    informa o problema e retorna valores nulos.

    Parâmetros:
    - caminho_arquivo (str): Caminho para o arquivo CSV a ser lido.
      Por padrão, utiliza "train.csv".

    Retorno:
    - tuple: Uma tupla contendo o cabeçalho e a matriz de dados.
      Caso ocorra algum erro, retorna (None, None).
    """
  if not os.path.exists(caminho_arquivo):
    print("Arquivo não encontrado.")
    return None, None
  try:
    with open(caminho_arquivo, "r", encoding = "utf-8") as f:
      conteudo = csv.reader(f)

      cabecalho = [next(conteudo)]
      matriz_dados = list(conteudo)
      
      return cabecalho, matriz_dados
  except Exception as erro:
    print(f"ocorreu um erro inesperado ao ler o arquivo {erro}")
    return None, None
