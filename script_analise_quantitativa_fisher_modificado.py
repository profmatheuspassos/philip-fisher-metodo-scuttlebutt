
import pandas as pd

# Função para calcular a pontuação total com base nas respostas
def calcular_pontuacao(df):
    # Somar a pontuação total
    return df['Pontuação (1-5)'].sum()

# Função para exibir as perguntas e coletar as pontuações
def coletar_pontuacao():
    questions = [
        "Potencial de mercado para crescimento futuro",
        "Desenvolvimento contínuo de novos produtos",
        "Eficiência em Pesquisa e Desenvolvimento (P&D)",
        "Organização em vendas eficiente",
        "Margem de lucro considerável",
        "Melhoria das margens de lucro",
        "Boas relações trabalhistas",
        "Relação com executivos",
        "Profundidade gerencial",
        "Controle de custos",
        "Diferenciais competitivos",
        "Estratégia de longo prazo",
        "Necessidade de emissão de ações futura",
        "Transparência da administração",
        "Integridade da administração"
    ]

    # Coletar o ticker da ação
    ticker = input("Digite o ticker do ativo: ")

    # Criar um dataframe para armazenar as perguntas e as pontuações
    df = pd.DataFrame({"Perguntas": questions, "Pontuação (1-5)": [None] * len(questions)})

    # Coletar a pontuação do usuário para cada pergunta
    for i, question in enumerate(questions):
        while True:
            try:
                score = int(input(f"Digite a pontuação para '{question}' (1-5): "))
                if 1 <= score <= 5:
                    df.loc[i, 'Pontuação (1-5)'] = score
                    break
                else:
                    print("Por favor, insira um valor entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 5.")
    
    # Retornar o dataframe com as pontuações preenchidas e o ticker da ação
    return df, ticker

# Função principal
def main():
    print("Bem-vindo ao modelo de análise quantitativa de Philip Fisher!")
    df, ticker = coletar_pontuacao()
    total_pontuacao = calcular_pontuacao(df)
    
    print(f"Pontuação total para {ticker}: {total_pontuacao}/75")
    
    # Adicionar o ticker e a pontuação total ao final do dataframe
    df = pd.concat([df, pd.DataFrame([{"Perguntas": "Ticker", "Pontuação (1-5)": ticker}])], ignore_index=True)
    df = pd.concat([df, pd.DataFrame([{"Perguntas": "Pontuação Total", "Pontuação (1-5)": total_pontuacao}])], ignore_index=True)
    
    # Salvar o resultado em um arquivo Excel
    df.to_excel(f"Resultado_Analise_{ticker}.xlsx", index=False)
    print(f"Os resultados foram salvos no arquivo 'Resultado_Analise_{ticker}.xlsx'.")

if __name__ == "__main__":
    main()
