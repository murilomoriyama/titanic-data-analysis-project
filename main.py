from importacao import carregar_dados
from visualizacao import visualizar_cabecalho, visualizar_conteudo
from analise_titanic import contagem_geral, estatisticas, frequencia, sobrevivencia_geral_segmento, idade_por_classe, tarifa_por_porto

cabecalho, dados = carregar_dados()

print("\n===== MENU =====")
print("0. Visualizar dados")
print("1.  Contagem Geral")
print("2.  Estatísticas de Idade e Tarifa")
print("3.  Frequência de Categorias")
print("4. Taxa de Sobrevivência Geral e por Segmento")
print("5. a definir...")
print("6. Estatísticas de Tarifas por Porto de Embarque")
print("7. a definir...")
print("8. Perfil Etário por Classe")
print("9. Encerrar programa.")

while True:
    opcao = int(input("selecione: "))
    if opcao == 0:
        visualizar_cabecalho(cabecalho)
        visualizar_conteudo(dados)
    if opcao == 1:
        contagem_geral(dados)
    if opcao == 2:    
        estatisticas(dados)
    if opcao == 3:
        frequencia(dados)
    if opcao == 4:
        sobrevivencia_geral_segmento(dados)
    if opcao == 6:
        tarifa_por_porto(dados)
    if opcao == 8:
        idade_por_classe(dados)
    if opcao == 9:
        break
