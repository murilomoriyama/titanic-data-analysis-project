import os
import csv

def carregar_dados(caminho_arquivo = "train.csv"):

  if not os.path.exists(caminho_arquivo):
    print("Arquivo não encontrado.")
    return None, None
  try:
    with open("train.csv", "r", encoding = "utf-8") as f:
      conteudo = csv.reader(f)

      cabeçalho = [next(conteudo)]
      matriz_dados = list(conteudo)
      return cabeçalho, matriz_dados
  except Exception as erro:
    print(f"ocorreu um erro inesperado ao ler o arquivo {erro}")
    return None, None
