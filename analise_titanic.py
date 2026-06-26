# Contagem Geral: Retornar o total de passageiros listados.
def contagem_geral(dados):
    print(f"O total de passageiros no titanic eram de: {len(dados)} pessoas.")

# Estatísticas de Idade e Tarifa: Calcular a idade mínima, máxima e média dos passageiros, assim como os valores das passagens (Fare).
def estatisticas(dados):
    qtdpassageiros = len(dados)

    somaidade = 0
    somatarifa = 0
    qtd_idades = 0

    idademinima = None
    idademaxima = None
    tarifaminima = None
    tarifamaxima = None

    for i in range(len(dados)):

        if dados[i][5] != "":
            idade = float(dados[i][5])
            somaidade += idade
            qtd_idades += 1

            if idademinima is None or idade < idademinima:
                idademinima = idade

            if idademaxima is None or idade > idademaxima:
                idademaxima = idade

        tarifa = float(dados[i][9])
        somatarifa += tarifa

        if tarifaminima is None or tarifa < tarifaminima:
            tarifaminima = tarifa

        if tarifamaxima is None or tarifa > tarifamaxima:
            tarifamaxima = tarifa

    idademedia = somaidade / qtd_idades
    tarifamedia = somatarifa / qtdpassageiros

    print("Idade máxima:", idademaxima)
    print("Idade mínima:", idademinima)
    print(f"Idade média: {idademedia:.0f}")
    print("Tarifa mínima:", tarifaminima)
    print("Tarifa máxima:", tarifamaxima)
    print(f"Tarifa média: {tarifamedia:.0f}")
# 3. Frequência de Categorias: Contar valores distintos em colunas escolhidas, como a classe do passageiro (Pclass) ou o porto de embarque (Embarked).
def frequencia(dados):
    primeira_classe = 0
    segunda_classe = 0
    terceira_classe = 0

    porto_s = 0
    porto_c = 0
    porto_q = 0
    print("1. classes")
    print("2. embarque")
    selecionar_frequencia = int(input("insira qual frequencia vc quer ver: "))
    for i in range(len(dados)):
        if selecionar_frequencia == 1:
            classe = float(dados[i][2])
            if classe == 1:
                primeira_classe += classe
            elif classe == 2:
                segunda_classe += classe
            elif classe == 3:
                terceira_classe += classe
        if selecionar_frequencia == 2:
            embarque = dados[i][11]
            if embarque == "C":
                porto_c += 1
            elif embarque == "S":
                porto_s += 1
            elif embarque == "Q":
                porto_q += 1
    if selecionar_frequencia == 1:
        print(f"na primeira classe: {primeira_classe:.0f}")
        print(f"na segunda classe: {segunda_classe:.0f}")
        print(f"na terceira_classe: {terceira_classe:.0f}")
    if selecionar_frequencia == 2:
        print(porto_c, "c")
        print(porto_q, "q")
        print(porto_s, "s")
# fazendo o 7
