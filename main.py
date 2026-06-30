"""
Alunos: GUILHERME DA SILVA DE MENEZES, MURILO EIDY MORIYAMA,
ARTHUR RAMOS RODRIGUES SILVA, YAN SEVY GARCIA BELANGER
"""

"""
Programa principal para análise dos dados do Titanic.

Este módulo realiza a importação dos dados do arquivo CSV,
apresenta um menu interativo ao usuário e direciona a execução
das diferentes análises estatísticas disponíveis no sistema,
como contagem de passageiros, estatísticas de idade e tarifa,
frequência de categorias, taxas de sobrevivência, composição
familiar, detalhamento de dados faltantes e perfil etário por
classe.

Módulos utilizados:
- importacao: Responsável pela leitura do arquivo CSV.
- visualizacao: Responsável pela exibição do cabeçalho e dos dados.
- analise_titanic: Contém as funções responsáveis pelas análises
  estatísticas realizadas sobre o conjunto de dados.

Retorno:
- None: Executa o menu principal até que o usuário escolha a
  opção de encerramento do programa.
"""

from importacao import carregar_dados
from visualizacao import visualizar_cabecalho, visualizar_conteudo
from analise_titanic import contagem_geral, estatisticas, frequencia, sobrevivencia_geral_segmento, composicao_familiar, idade_por_classe, detalhamento_dados_faltantes, tarifa_por_porto

cabecalho, dados = carregar_dados()

while True:
    print("\n===== MENU =====")
    print("0. Visualizar dados")
    print("1.  Contagem Geral")
    print("2.  Estatísticas de Idade e Tarifa")
    print("3.  Frequência de Categorias")
    print("4. Taxa de Sobrevivência Geral e por Segmento")
    print("5. Análise de Composição Familiar")
    print("6. Estatísticas de Tarifas por Porto de Embarque")
    print("7. Detalhamento de dados faltantes de passageiros (Data Cleaning)")
    print("8. Perfil Etário por Classe")
    print("9. Encerrar programa.")
    opcao = int(input("selecione: "))
    if opcao == 0:
        visualizar_cabecalho(cabecalho)
        visualizar_conteudo(dados)
    elif opcao == 1:
        contagem_geral(dados)
    elif opcao == 2:    
        estatisticas(dados)
    elif opcao == 3:
        frequencia(dados)
    elif opcao == 4:
        sobrevivencia_geral_segmento(dados)
    elif opcao == 5:
        composicao_familiar(dados)
    elif opcao == 6:
        tarifa_por_porto(dados)
    elif opcao == 7:
        detalhamento_dados_faltantes(dados) 
    elif opcao == 8:
        idade_por_classe(dados)
    elif opcao == 9:
        print("Programa finalizado com sucesso.")
        break
    else:
        print("Opção inválida. Insira uma opção listada!")
