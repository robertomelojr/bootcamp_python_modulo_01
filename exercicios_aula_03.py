### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.


import re
qtd_valida = False
preco_valido = False

while not qtd_valida or not preco_valido:
    try:
        quantidade = float(input("Digite a quantidade: "))
        
        if quantidade < 0:
            print("Por favor, digite um valor positivo para a quantidade.")
        else: 
            print("Quantidade válida.")
    
            qtd_valida = True
    except ValueError:
        
        print("Entrada inválida para o salário. Por favor, digite um número.")
        exit()
        
    try:
        preco = float(input("Digite o valor do preço: "))
        if preco < 0:
            print("Por favor, digite um valor positivo para o preço.")
        
        else: 
            print("Preço válido.")
            preco_valido = True

    except ValueError:
        print("Entrada inválida para o preço. Por favor, digite um número.")
        exit()

print (quantidade)
print(preco)


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa Temperatura >= 18°C e <= 26°C é 'Normal' e Temperatura > 26°C é 'Alta'

temp_valida = False

while not temp_valida:
    try:
        # Solicita ao usuário a temperatura
        temperatura = float(input("Digite a temperatura em graus Celsius: "))
        temp_valida = True  # Se chegar aqui, a entrada é válida
    except ValueError:
        print("Entrada inválida para a temperatura. Por favor, digite um número.")
        exit()
# Classificação da temperatura
if temperatura < 18:
    status = "Baixa"
elif 18 <= temperatura <= 26:
    status = "Normal"
else:
    status = "Alta"

# Exibe o resultado
print(f"A temperatura é de {temperatura}°C e está classificada como {status}.")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log : dict = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] =='ERROR':
    print(log['message'])
    
    
### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

from typing import Dict 

usuario_dict : dict[str,int]= {}

usuario_dict = {
    'Roberto': 26,
    'João': 80,
    'Ana': 18,
    'Paulo': 65,
    'Alex': 17,
   'Maria': 18}


for user, age in usuario_dict.items():
     if not 18 <= age <= 65:
        print(f"Error: O usuário {user} não tem idade para utilizar a plataforma!")
     else: 
        print(f"Dados válidos!")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

usuartransacaoio_dict : dict[float,any]= {}

transacao = {12000: 20,
             10:10,
             1000:23}


for valor, hour in transacao.items():
    
     if not 9 <= hour <= 18 or valor >= 10000  :
         
        print(f"Atenção: a transação de {valor} às {hour} pode ser uma fraude!")
 

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = input("Digite a frase desejada: ") 

lista_de_texto = texto.split()

dicionario_lista_palavras = {}

for item in lista_de_texto:
    dicionario_lista_palavras[item] = dicionario_lista_palavras.get(item, 0) + 1

print(dicionario_lista_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
    {"nome": "", "email": "usuario@example.com"}
]

try:
    for usuario in usuarios:
        nome = usuario.get("nome", "Desconhecido")  
        email = usuario.get("email", "")  
        
       
        if len(email) < 10:
            print(f"O usuário {nome if nome else 'Sem Nome'} tem dados de email inválidos, verificar os dados!")
     
        if not nome:
            print("Há um usuário sem nome definido, verificar os dados!")
            
except Exception as e:
    print(f"Ocorreu um erro: {e}")

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

num = range(5, 17)
pares = [x for x in num if x % 2 == 0]

print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "papelaria", "valor": 1000},
    {"categoria": "utilitarios", "valor": 350},
    {"categoria": "papelaria", "valor": 325}
]


tot_por_categoria = {}

for venda in vendas:
    
    categoria = venda["categoria"]
    valor = venda["valor"]
    
    tot_por_categoria[categoria] = tot_por_categoria.get(categoria, 0) + valor

print("Total de vendas por categoria:")
for categoria, total in tot_por_categoria.items():
    print(f"- {categoria}: {total}")    

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
dados = []
entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
    if entrada.lower() != "sair":
        dados.append(entrada)
    else:
        print("Valores inseridos:")
        for valor in dados:
            print(f"- {valor}")
        exit()
        
### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
lista = list(range(1, 11))

try:
    numero = int(input("Digite um número entre 1 e 10: "))
except ValueError:
    print("Erro: O valor inserido precisa ser um número inteiro.")
    exit()

while numero not in lista:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))
print("Número válido!")


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
pagina_atual = 1
paginas_totais = 5 

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais} ...")
    
    pagina_atual += 1

print("Todas as páginas foram processadas com sucesso!")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    
    if True:  # supondo que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1