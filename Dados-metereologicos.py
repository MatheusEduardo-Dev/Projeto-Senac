# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados(nome_arquivo): #Carrega os dados do arquivo CSV
    
    try:
        dados = pd.read_csv(nome_arquivo)
        dados['data'] = pd.to_datetime(dados['data'], format='%d/%m/%Y', errors='coerce')
        dados = dados.dropna(subset=['data'])
        dados['ano'] = dados['data'].dt.year
        dados['mes'] = dados['data'].dt.month

        print("Dados carregados com sucesso:")
        print(dados.head())
        return dados

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def visualizar_dados(dados, mes_inicial, ano_inicial, mes_final, ano_final, tipo): #visualizar dados em um intervalo de tempo
    
    dados_filtrados = dados[
        ((dados['ano'] > ano_inicial) | ((dados['ano'] == ano_inicial) & (dados['mes'] >= mes_inicial))) &
        ((dados['ano'] < ano_final) | ((dados['ano'] == ano_final) & (dados['mes'] <= mes_final)))
    ]
    
    if dados_filtrados.empty:
        print("Nenhum dado encontrado para o intervalo fornecido.")
        return
    
    print("\n--- Dados Filtrados ---")  #1-Todos os dados 2-Precipitação 3-0Temperatura 4-Umidade e Vento
    if tipo == 1:  
        print(dados_filtrados)
    elif tipo == 2:  
        print(dados_filtrados[['data', 'precip']])
    elif tipo == 3: 
        print(dados_filtrados[['data', 'minima', 'maxima']])
    elif tipo == 4:  
        print(dados_filtrados[['data', 'um_relativa', 'vel_vento']])
    else:
        print("Tipo de dado inválido.")



def mes_mais_chuvoso(dados): #Encontra o mês com maior precipitação.
    
    mes_mais_chuvoso = dados.groupby(['ano', 'mes'])['precip'].sum().idxmax()
    max_precip = dados.groupby(['ano', 'mes'])['precip'].sum().max()

    print(f"\nMês mais chuvoso: {mes_mais_chuvoso[1]}/{mes_mais_chuvoso[0]} com {max_precip} mm")


def media_temp_min(dados, mes): #Calcula a média da temperatura mínima para um mês específico entre 2006 e 2016.
    
    dados_filtrados = dados[(dados['mes'] == mes) & (dados['ano'] >= 2006) & (dados['ano'] <= 2016)]
    medias = dados_filtrados.groupby('ano')['minima'].mean()

    for ano, media in medias.items():
        print(f"{mes}/{ano}: {media:.2f} °C")

    return medias


def exibir_grafico_temp(medias, mes): #Exibe um gráfico de barras das médias de temperatura mínima.
    medias.plot(kind='bar', color='blue', legend=False)
    plt.title(f"Média de Temperaturas Mínimas - Mês {mes}")
    plt.xlabel("Ano")
    plt.ylabel("Temperatura Mínima (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    nome_arquivo = "dados.csv"
    dados = carregar_dados(nome_arquivo)

    if dados is None or dados.empty:
        print("Nenhum dado foi carregado. Encerrando o programa.")
        return

    while True:
        print("\n--- Menu ---")
        print("1. Visualizar intervalo de dados")
        print("2. Mês mais chuvoso")
        print("3. Média da temperatura mínima de um mês específico")
        print("4. Gráfico de médias de temperatura mínima")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mes_inicial = int(input("Digite o mês inicial (1-12): "))
            ano_inicial = int(input("Digite o ano inicial: "))
            mes_final = int(input("Digite o mês final (1-12): "))
            ano_final = int(input("Digite o ano final: "))
            tipo = int(input("Digite o tipo de dado (1-Todos, 2-Precipitação, 3-Temperatura, 4-Umidade e Vento): "))
            visualizar_dados(dados, mes_inicial, ano_inicial, mes_final, ano_final, tipo)
        elif opcao == "2":
            mes_mais_chuvoso(dados)
        elif opcao == "3":
            mes = int(input("Digite o mês (1-12): "))
            medias = media_temp_min(dados, mes)
        elif opcao == "4":
            mes = int(input("Digite o mês (1-12): "))
            medias = media_temp_min(dados, mes)
            exibir_grafico_temp(medias, mes)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")




if __name__ == "__main__":
    main()