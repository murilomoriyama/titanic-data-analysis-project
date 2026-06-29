# 1.  Contagem Geral: Retornar o total de passageiros listados.
def contagem_geral(dados):
    print(f"O total de passageiros no titanic eram de: {len(dados)} pessoas.")

#2.  Estatísticas de Idade e Tarifa: Calcular a idade mínima, 
# máxima e média dos passageiros, assim como os valores das passagens (Fare).
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
    print("Tarifa mínima: U$", tarifaminima)
    print("Tarifa máxima: U$", tarifamaxima)
    print(f"Tarifa média: U${tarifamedia:.0f}")

#3.  Frequência de Categorias: Contar valores distintos em colunas escolhidas,
#como a classe do passageiro (Pclass) ou o porto de embarque (Embarked).

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
                primeira_classe += 1
            elif classe == 2:
                segunda_classe += 1
            elif classe == 3:
                terceira_classe += 1

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

#4. Taxa de Sobrevivência Geral e por Segmento Além da contagem básica de valores
#distintos sugerida, você pode calcular a probabilidade de sobrevivência baseada na coluna Survived:
#Taxa Geral: Porcentagem total de sobreviventes em relação ao total de passageiros.
#Por Sexo: Comparar a taxa de sobrevivência entre male (homens) e female (mulheres)
#Por Classe: Calcular qual a porcentagem de sobreviventes em cada Pclass (1ª, 2ª e 3ª classe).

def sobrevivencia_geral_segmento (dados):
    geral = 0
    muie = 0
    homi = 0
    total = (len(dados))

    S_primeira_classe = 0
    S_segunda_classe = 0
    S_terceira_classe = 0

    print("1. taxa geral")
    print("2. por sexo")
    print("3. por classe")

    sobreviventes = 0

    for i in range(len(dados)):
        if int(dados[i][1]) == 1:
            sobreviventes += 1

    selecionar = int(input("insira aqui qual opção voce deseja: "))

    for i in range(len(dados)):
        sobreviveu = float(dados[i][1])
        if selecionar == 1:
            sobreviveu = float(dados[i][1])
            if sobreviveu == 1:
                geral += 1

        if selecionar == 2:
            genero = dados[i][4]
            
            if (sobreviveu == 1 and genero == "female"):
                muie +=1
            if (sobreviveu == 1 and genero == "male"):
                homi +=1

        if selecionar == 3:
            classe = float(dados[i][2])
            
            if (sobreviveu == 1 and classe == 1):
                S_primeira_classe +=1
            if (sobreviveu == 1 and classe == 2):
                S_segunda_classe +=1
            if (sobreviveu == 1 and classe == 3):
                S_terceira_classe +=1

    primeira_classe = 0
    segunda_classe = 0
    terceira_classe = 0
    for i in range(len(dados)):
        
        classe = float(dados[i][2])
        if classe == 1:
            primeira_classe += 1
        elif classe == 2:
            segunda_classe += 1
        elif classe == 3:
            terceira_classe += 1

    total_mulher = 0
    total_homem = 0
    for i in range(len(dados)):
        if dados[i][4] == "male":
            total_homem +=1
        if dados[i][4] == "female":
            total_mulher +=1
        
    geral_porcentagem = (geral / total) * 100

    mulher_porcentagem = (muie / total_mulher) * 100
    homen_porcentagem = (homi / total_homem) * 100
    S_mulher = (muie / sobreviventes) * 100
    S_homem = (homi / sobreviventes) * 100

    primeira_porcentagem = (S_primeira_classe / primeira_classe) * 100
    segunda_porcentagem = (S_segunda_classe / segunda_classe) * 100
    terceira_porcentagem = (S_terceira_classe / terceira_classe) * 100

    S_primeira = (S_primeira_classe / sobreviventes) * 100
    S_segunda = (S_segunda_classe / sobreviventes) * 100
    S_terceira = (S_terceira_classe / sobreviventes) * 100
    if selecionar == 1:
        print(f"A porcentagem geral de sobreviventes foi de: {geral_porcentagem:.2f}%")
    if selecionar == 2:
        print(f"a porcentagem geral de sobrevivencia de mulheres foi de:{mulher_porcentagem:.2f}%, enquanto a de homens foi de: {homen_porcentagem:.2f}%")
        print("")
        print(f"enquanto a porcentagem geral de sobreviventes mulheres foi de {S_mulher:.2f}%, e a de homens foi de {S_homem:.2f}%")
    if selecionar == 3:
        print(f"a porcentagem geral de sobrevivencia da primeira classe foi de: {primeira_porcentagem:.2f}%")
        print(f"a porcentagem geral de sobrevicencia da segunda classe foi de: {segunda_porcentagem:.2f}%")
        print(f"a porcentagem geral de sobrevivencia da terceira classe foi de: {terceira_porcentagem:.2f}%")
        print("")
        print(f"a porcentagem de sobreviventes da primeira classe foi de: {S_primeira:.2f}%")
        print(f"a porcentagem de sobreviventes da segunda classe foi de: {S_segunda:.2f}%")
        print(f"a porcentagem de sobreviventes da terceira classe foi de: {S_terceira:.2f}%")

# 5 Composição familiar: Utilizando as colunas SibSp (irmãos/cônjuges) e Parch (pais/filhos) para gerar novas métricas:
# Tamanho da Família: Uma análise que soma essas duas colunas para identificar se o passageiro viajava sozinho ou em grupo.
# Média de Familiares: Calculando a média de parentes que os passageiros tinham a bordo.

def composicao_familiar(dados):
    """
    Analisa a composição familiar dos passageiros do Titanic.

    Para cada passageiro, soma as colunas SibSp (irmãos/cônjuges)
    e Parch (pais/filhos) para identificar se viajava sozinho
    ou acompanhado. Ao final, calcula a média de familiares
    presentes a bordo por passageiro.

    Parâmetros:
    - dados (list): Lista de listas contendo os dados dos passageiros.

    Retorno:
    - None: Exibe na tela a situação de cada passageiro e a média
      de familiares a bordo.
    """

    contador = 0

    for i in range(len(dados)):
        sibsp = int(dados[i][6])
        parch = int(dados[i][7])

        total = sibsp + parch
        contador += total

        if total == 0:
            print(f"Passageiro {i + 1}: Sozinho")
        else:
            print(f"Passageiro {i + 1}: Acompanhado de {total} familiar(es)")

    media = contador / len(dados)

    print()
    print(f"Média de familiares a bordo por passageiro: {media:.2f}")

#6. Estatísticas de Tarifas (Fare) por Porto de Embarque Cruzando as colunas Fare e Embarked, o sistema pode informar:
#A tarifa média paga por passageiros que embarcaram em cada porto: C (Cherbourg), Q (Queenstown) e S (Southampton).
#Identificar qual porto teve a passagem mais cara e a mais barata.

def tarifa_por_porto(dados):
    cherbourg = 0
    queenstown = 0
    southampton = 0

    tarifa_c = 0
    tarifa_q = 0
    tarifa_s = 0

    portomax = None
    tarifamax = None
    portomin = None
    tarifamin = None

    for i in range(len(dados)):
        tarifa = float(dados[i][9])
        porto = dados[i][11]
        if porto == "C":
            cherbourg +=1
            tarifa_c += tarifa
            if tarifamax is None or tarifa > tarifamax:
                tarifamax = tarifa
                portomax = porto
            if tarifamin is None or tarifa < tarifamin:
                tarifamin = tarifa
                portomin = porto
        if porto == "Q":
            queenstown += 1
            tarifa_q += tarifa
            if tarifamax is None or tarifa > tarifamax:
                tarifamax = tarifa
                portomax = porto
            if tarifamin is None or tarifa < tarifamin:
                tarifamin = tarifa
                portomin = porto
        if porto == "S":
            southampton += 1
            tarifa_s += tarifa
            if tarifamax is None or tarifa > tarifamax:
                tarifamax = tarifa
                portomax = porto
            if tarifamin is None or tarifa < tarifamin:
                tarifamin = tarifa
                portomin = porto
    media_c = tarifa_c / cherbourg
    media_q = tarifa_q / queenstown
    media_s = tarifa_s / southampton

    print(f"a media de tarifas no porto de Cherbourg foi de: U${media_c:.2f}")
    print(f"a media de tarifas no porto de Queenstown foi de: U${media_q:.2f}")
    print(f"a media de tarifas no porto de Southampton foi de: U${media_s:.2f}")
    print(f"a tarifa mais barata foi no valor de: U${tarifamin:.2f} no porto {portomin}")
    print(f"a tarifa mais cara foi no valor de: U${tarifamax:.2f} no porto {portomax}")

# 7. Detalhamento de Dados Faltantes (Data Cleaning):
# Contabilizando quantos registros de Age estão vazios (células sem valor no CSV).
# Identificando a porcentagem de passageiros sem informação de Cabin (cabine), o que é comum em registros da 3ª classe.

def detalhamento_dados_faltantes(dados):
    """
    Analisa a quantidade de dados faltantes no conjunto de dados do Titanic.

    Contabiliza quantos passageiros não possuem idade registrada
    (Age) e calcula a porcentagem de passageiros que não possuem
    informação da cabine (Cabin).

    Parâmetros:
    - dados (list): Lista de listas contendo os dados dos passageiros.

    Retorno:
    - None: Exibe na tela a quantidade de idades ausentes e a
      porcentagem de passageiros sem informação de cabine.
    """

    idade_vazia = 0
    cabine_vazia = 0

    for i in range(len(dados)):

        if dados[i][5].strip() == "":
            idade_vazia += 1

        if dados[i][10].strip() == "":
            cabine_vazia += 1

    porcentagem_cabine = (cabine_vazia / len(dados)) * 100

    print(f"Passageiros sem idade informada: {idade_vazia}")
    print(f"Passageiros sem cabine informada: {porcentagem_cabine:.2f}%")

#8. Perfil Etário por Classe Calcular a idade média, mínima e máxima (estatísticas numéricas básicas solicitadas)
#especificamente para cada uma das classes (Pclass).
#Isso permite observar se passageiros da 1ª classe eram, em média, mais velhos que os da 3ª classe.

def idade_por_classe(dados):
    primeira_classe = 0
    segunda_classe = 0
    terceira_classe = 0
    
    idade_primeira = 0
    idade_segunda = 0
    idade_terceira = 0

    primeiramin = None
    primeiramax = None
    segundamin = None
    segundamax = None
    terceiramin = None
    terceiramax = None

    for i in range(len(dados)):
        if dados[i][5] != "":
            classe = int(dados[i][2])
            idade = float(dados[i][5])
            if classe == 1:
                primeira_classe += 1
                idade_primeira += idade
                if primeiramin is None or idade < primeiramin:
                    primeiramin = idade
                if primeiramax is None or idade > primeiramax:
                    primeiramax = idade

            if classe == 2:
                segunda_classe += 1
                idade_segunda += idade
                if segundamin is None or idade < segundamin:
                    segundamin = idade
                if segundamax is None or idade > segundamax:
                    segundamax = idade

            if classe == 3:
                terceira_classe +=1
                idade_terceira += idade
                if terceiramin is None or idade < terceiramin:
                    terceiramin = idade
                if terceiramax is None or idade > terceiramax:
                    terceiramax = idade

    media_primeira = idade_primeira / primeira_classe
    media_segunda = idade_segunda / segunda_classe
    media_terceira = idade_terceira / terceira_classe

    print(f"na primeira classe a media de etaria era de: {media_primeira:.2f}, sendo a idade minima {primeiramin} anos e a maxima {primeiramax} anos")
    print(f"na segunda classe a media etaria era de: {media_segunda:.2f}, sendo a idade minima {segundamin} anos e a maxima {segundamax} anos")
    print(f"na terceira classe a media etaria era de: {media_terceira:.2f}, sendo a idade minima {terceiramin} anos e a maxima {terceiramax} anos")
