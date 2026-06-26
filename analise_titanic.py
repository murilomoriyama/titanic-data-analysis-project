from importação import carregar_dados

arquivo = "train.csv"

cabecalho, dados = carregar_dados()
qtdpassageiros = len(dados)

def contagem_geral():
  print(qtdpassageiros)

def estatisticas():
  somaidade = 0
  somatarifa = 0
  for i in range(dados):
    somaidade += dados[5]
    somatarifa += dados[9]
    if i == 0:
      idademinima = dados[5]
      idademaxima = dados[5]
      tarifaminima = dados[9]
      tarifamaxima = dados[9]
    else:
      if dados[5] < idademinima:
        idademinima = dados[5]

      elif dados[5] > idademaxima:
        idademaxima = dados[5]

      if dados[9] < tarifaminima:
        tarifaminima = dados[9]

      elif dados[9] > tarifamaxima:
        tarifamaxima = dados[9]

  

    idademedia = somaidade / qtdpassageiros
    tarifamedia = somatarifa / qtdpassageiros

    print(idademaxima)
    print(idademinima)
    print(idademedia)
    print(tarifaminima)
    print(tarifamaxima)
    print(tarifamedia)
        
  



 
