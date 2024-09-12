# Modelo de Análise Quantitativa de Philip Fisher

## Visão Geral
Este script em Python é um modelo simples de análise quantitativa baseado nos princípios de investimento de Philip Fisher. O objetivo é avaliar uma ação com base em várias perguntas relacionadas a diferentes aspectos da empresa, fornecendo uma pontuação total que pode ajudar na tomada de decisões de investimento.

O usuário responde a um conjunto de perguntas com uma pontuação de 1 a 5, e o script calcula a pontuação total, salvando o resultado em um arquivo Excel para posterior análise.

## Funcionalidades
- Coleta de pontuação do usuário para 15 perguntas relacionadas à avaliação de ações.
- Cálculo da pontuação total para o ticker da ação inserido.
- Salva as perguntas, respostas e pontuação total em um arquivo Excel com o nome do ticker da ação.
- Tratamento de erros de entrada para garantir que apenas valores entre 1 e 5 sejam aceitos.

## Uso
1. Ao rodar o script, o usuário deve inserir o ticker da ação a ser avaliada.
2. O script faz 15 perguntas sobre diferentes aspectos da empresa.
3. Para cada pergunta, o usuário deve fornecer uma pontuação de 1 a 5.
4. O script calcula a pontuação total e salva os dados em um arquivo Excel, nomeado com o ticker da ação.

## Requisitos
- Python 3.8+
- Pandas 2.0+
- Biblioteca `openpyxl` para salvar o arquivo Excel.

## Instalação
1. Clone este repositório em sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Navegue até o diretório do repositório:
    ```bash
    cd nome-do-repositorio
    ```

3. Instale as dependências:
    ```bash
    pip install pandas openpyxl
    ```

4. Execute o script:
    ```bash
    python script_analise_quantitativa_fisher.py
    ```

## Observações/Pontos para Melhoria
Abaixo estão algumas melhorias que ainda podem ser implementadas no script:

- **Melhoria de tratamento de erros**: Adicionar validação para o nome do ticker, garantindo que seja um código de ação válido (apenas letras maiúsculas, por exemplo).

- **Melhoria na usabilidade**: Oferecer a opção de sair do programa ou revisar as pontuações antes de salvar o arquivo, para evitar erros ou avaliações incorretas.

- **Melhoria de fluxo de inserção**: Incluir a possibilidade de inserir avaliações de múltiplas ações até o usuário pedir para sair, gravando todas as avaliações em um único arquivo Excel.

- **Melhoria de eficiência**: O uso repetido de `pd.concat()` para adicionar linhas ao dataframe pode ser otimizado ao criar e concatenar todas as novas linhas em um único comando ao final da coleta dos dados, reduzindo o overhead.

- **Melhoria na apresentação dos dados**: Formatar a saída no Excel com cabeçalhos destacados, definindo tipos de dados (númerico/texto), ou adicionar uma formatação condicional para destacar pontuações baixas ou altas.

- **Melhoria de clareza**: Separar a lógica de coleta de pontuações e a lógica de cálculo da pontuação total em módulos ou classes distintas para facilitar a manutenção e aumentar a legibilidade.

- **Melhoria na manipulação de exceções**: Incluir um tratamento mais detalhado para exceções durante a criação do arquivo Excel, como garantir que o arquivo não esteja aberto em outro programa ou não tenha permissões insuficientes.

- **Melhoria de modularidade**: A função `main()` poderia ser mais modular, quebrando algumas partes, como a impressão e salvamento de resultados, em funções separadas para facilitar o reuso e testes.

- **Melhoria de segurança**: Remover o uso de `input()` sem validação de entrada, especialmente para o ticker, onde dados incorretos ou maliciosos podem causar comportamentos inesperados no script.

## ISENÇÃO DE RESPONSABILIDADE
Este script foi desenvolvido com propósitos educacionais e não deve ser utilizado como uma ferramenta de análise de investimentos definitiva. As decisões de investimento devem ser tomadas com base em uma análise detalhada e completa, e este script é apenas uma simplificação dos princípios de Philip Fisher. O autor não se responsabiliza por quaisquer decisões tomadas com base nos resultados gerados por este script.

