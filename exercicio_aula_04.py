    #Exercícios de Listas e Dicionários

#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista_de_numeros = list(range(1,11))

for numero in lista_de_numeros:
    print(numero**2)

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".


lista_de_linguagens : list = ["Python", "Java", "C++", "JavaScript"]

lista_de_linguagens_copy : list = lista_de_linguagens.copy()
print(lista_de_linguagens_copy)
lista_de_linguagens_copy.remove("C++")
print(lista_de_linguagens_copy)
lista_de_linguagens_copy.append("Ruby")
print(lista_de_linguagens_copy)

#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {"titulo": "teste_de_titulo", "autor": "autor teste", "ano": 2024}

for chave, valor in livro.items():
    print(f"{chave}: {valor}")
    
#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contagem_de_caracteres (s) :
    contagem ={}
    for caractere in s: 
        contagem[caractere] = contagem.get(caractere,0)+1
    return contagem 

print(contagem_de_caracteres("contagem de teste de caractere"))


#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.


lista_de_compras : list = ["maçã", "banana", "cereja"]

dicionario_de_compras : dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total_de_compras = sum(dicionario_de_compras[item] for item in lista_de_compras)

print(f"O preço das compras foi de: R${total_de_compras}")

##  Eliminação de Duplicatas e filtragem de dados 
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

lista_de_emails : list = ["roberto@email.com", "user@email.com", "user_0123@email.com","roberto@email.com"]

lista_de_emails_unicos :list = list(set(lista_de_emails))

dicionario_de_emails : dict = {"roberto@email.com": 26, "user@email.com": 18, "user_0123@email.com": 17} ## por convencao vamos assumir que ele é único

emails_validos_filtrados = list(
    email for email in lista_de_emails_unicos
    if dicionario_de_emails.get(email, 0) >= 18)

print(emails_validos_filtrados)

## Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas_ordenadas = {pessoa["nome"]: pessoa["idade"] for pessoa in sorted(pessoas, key=lambda pessoa: pessoa["nome"])}


print(pessoas_ordenadas)

# Objetivo: Dado um conjunto de números, calcular a média.

dados = [1,20,40,55,100]

media = sum(dados)/len(dados)
print(f"A média do conjunto de dados é de: {media}")

# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

pares: list = []
impares: list = []

for valor in dados:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Pares:", pares)
print("Ímpares:", impares)

# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100.00},
    {"id": 2, "nome": "Mouse", "preço": 80.32},
    {"id": 3, "nome": "Monitor", "preço": 300.99}
]

opcoes_id = [produto["id"] for produto in produtos]

id_atualidado = int(input(f"Digite o id do produto que será atualizado. Opções: {opcoes_id} "))

preco_atualizado = float(input("Digite o novo valor que será atualizado: "))

for produto in produtos:
    if produto["id"] == id_atualidado:
        produto["preço"] = preco_atualizado

print(produtos)

# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.


dicionario_de_emails_novos = {"roberto_1234@email.com": 29, "user_123_mudar@email.com": 15, "user_mudar@email.com": 19}

dicionario_de_emails_fundido = {**dicionario_de_emails, **dicionario_de_emails_novos}

print(dicionario_de_emails_fundido)

# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


estoque =  {"Monitor": 1, "Mouse": 0,"Teclado": 2, "GPU": 0, "CPU": 0}

estoque_disponivel = {produto : quantidade 
                      for produto, quantidade in estoque.items() if quantidade >0}

print(f"Os seguintes estão disponíveis: {estoque_disponivel}")

# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

produtos : list = list(estoque_disponivel.keys())
quantidades : list = list(estoque_disponivel.values())

print(f"Os seguintes estão disponíveis: {produtos}")


## Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = input("Digite aqui um texto: ")

texto_minusculo = texto.lower()

frequencia = {}

for caractere in texto_minusculo:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)


#Exercícios de Funções

#Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def soma_numeros(lista):
    
    return sum(lista)


numeros = [1, 2, 3, 4, 5]
resultado = soma_numeros(numeros)
print(f"A soma dos números é: {resultado}")

#Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def varifica_numero_primo(numero):
  
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print(varifica_numero_primo(7))  
print(varifica_numero_primo(10))  


#Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverte_string(s):
 
    return s[::-1]

texto_str = input("Digite uma palavra: ")

print(reverte_string(texto_str)) 
#Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def encontrar_numeros_pares(lista, alvo):
  
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares


print(encontrar_numeros_pares([1, 2, 3, 4, 5], 6))  
#Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def ordena_chaves(dicionario):
 
    return sorted(dicionario.keys())


d = {"c": 3, "a": 1, "b": 2}
print(ordena_chaves(d)) 
