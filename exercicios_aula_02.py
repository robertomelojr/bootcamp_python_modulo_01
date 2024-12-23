# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

try:
    valor_1 = int(input("Digite o primeiro número:"))
    valor_2 = int(input("Digite o segundo número:"))
    soma = valor_1 + valor_2
    
## Possíveis erros nessa operação: 
# Digitar uma letra em algum momento ou alguma string;
# Cancelar sem querer o cursor teclando algo no meio da execução;
# Digitar um número que não seja inteiro
 
 
except ValueError :
 print(" Um dos dois valores não é um número inteiro, tente novamente e digite um valor válido!") ## ValueError resolve para números diferentes de inteiros e strings

except KeyboardInterrupt:
    print(" Acho que você não quis inserir um número, vamos finalizar a interação.")  ## KeyboardInterrupt trata casos de ctrl + c, por exemplo 

else :
    print('A soma dos dois valores é: {0}'.format(soma)) 
    


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

try:
    n_usuario = int(input("Digite um número inteiro: ")) # para facilitar vamos considerar apenas números inteiros

    resto_div = n_usuario % 5 
   
except ValueError :
 print(" Um dos dois valores não é um número inteiro, tente novamente e digite um valor válido!") ## ValueError resolve para números diferentes de inteiros e strings

except KeyboardInterrupt:
    print(" Acho que você não quis inserir um número, vamos finalizar a interação.")  ## KeyboardInterrupt trata casos de ctrl + c, por exemplo 
if n_usuario < 5:
        print(f"O número {n_usuario} é menor do que 5, insira um número válido.")
elif resto_div == 0 :
        print("O resto do número inserido é 0")     
else :
    print('O resto da divisão por 5 é:'.format(resto_div)) 
  


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try:
    valor_1_mult = float(input("Digite o primeiro múltiplo: ")) # para facilitar vamos considerar apenas números inteiros
    
    valor_2_mult = float(input("Digite o segundo múltiplo: "))
    
    result = round(valor_1_mult*valor_2_mult,2)
 
    
except ValueError:
    print("Um dos valores não é um número válido. Tente novamente e digite um valor válido!")
    result = None  # Define o resultado como None em caso de erro

except KeyboardInterrupt:
    print("Você interrompeu a interação. Vamos finalizar.")
    result = None  # Define o resultado como None em caso de interrupção

# Garante que apenas valores válidos sejam processados
if result is not None:
    if valor_1_mult == 0 or valor_2_mult == 0:
        print("O resultado da multiplicação é: Zero")
    else:
        print(f"O resultado da multiplicação é: {result}")
    

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    divisor = int(input("Digite o divisor inteiro: ")) # para facilitar vamos considerar apenas números inteiros
    dividendo = int(input("Digite o dividendo inteiro: "))
    divisao = (divisor // dividendo)
    
except ValueError:
    print("Um dos valores não é um número válido. Tente novamente e digite um valor válido!")
    divisao = None  # Define o resultado como None em caso de erro

except KeyboardInterrupt:
    print("Você interrompeu a interação. Vamos finalizar.")
    divisao = None  # Define o resultado como None em caso de interrupção

except ZeroDivisionError :
    print("Não é possível realizar uma divisão por Zero, insira um dividendo diferente de Zero.")
    divisao = None

if divisao is not None:
        print(f"O resultado da multiplicação é: {divisao}")
    
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
try:
    base = int(input("Digite a base: ")) # para facilitar vamos considerar apenas números inteiros
    pot = (base ** 2)
    
except ValueError:
    print("O valor fornecido não é um número válido. Tente novamente e digite um valor válido!")
    pot = None 
except KeyboardInterrupt:
    print("Você interrompeu a interação. Vamos finalizar.")
    pot = None  

if pot is not None:
        print(f"O quadrado de {base} é: {pot}")
        
# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

try:
    n_1_soma = float(input("Digite o primeiro número da soma:"))

    n_2_soma = float(input("Digite o segundo número da soma:")) 

    resultado_soma = n_1_soma + n_2_soma

except ValueError:
    print("Um dos valores não é um número válido. Tente novamente e digite um valor válido!")
    resultado_soma = None 
except KeyboardInterrupt:
    print("Você interrompeu a interação. Vamos finalizar.")
    resultado_soma = None  

if resultado_soma is not None:
    if n_1_soma <= 0 or n_2_soma <=0 :
        print("Error: Essa soma precisa ser de números poisivos!")
    else :
        print(f"O resultado da potência é: {resultado_soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

try:
    n_1_soma = float(input("Digite o primeiro número:"))

    n_2_soma = float(input("Digite o segundo número:")) 

    media_result = (n_1_soma + n_2_soma)/2

except ValueError:
    print("Um dos valores não é um número válido. Tente novamente e digite um valor válido!")
    media_result = None 
except KeyboardInterrupt:
    print("Você interrompeu a interação. Vamos finalizar.")
    media_result = None  

if media_result is not None:
    
        print(f"O resultado da potência é: {media_result}")
        

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

try:
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    pot = (base ** expoente)
    
except ValueError:
    print("Um dos valores não é um número válido. Tente novamente e digite um valor válido!")
    pot = None 
except KeyboardInterrupt:
    print("Você interrompeu a interação. Vamos finalizar.")
    pot = None  

if pot is not None:
        print(f"O resultado da potência é: {pot}")
        
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

try:
    celsius = float(input("Digite a temperatura em graus Celsius: ")) 
    fahrenheit = (celsius * 9/5) + 32
except ValueError:
    print("O valor fornecido não é um número válido. Tente novamente e digite um valor válido!")
    celsius = None  
    fahrenheit = None
except KeyboardInterrupt:
    print("\nVocê interrompeu a interação. Vamos finalizar.")
    celsius = None  
    fahrenheit = None

if fahrenheit is not None and celsius is not None:
    print(f"{celsius} graus Celsius corresponde a {fahrenheit} Fahrenheit.")

 
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

try:

    raio = float(input("Digite o raio do círculo: "))

  
    if raio < 0:
        print("Erro: O raio não pode ser negativo.")
    else:
       
        area = math.pi * (raio ** 2)

        print(f"A área do círculo com raio {raio:.2f} é: {area:.2f}")

except ValueError:
    print("Erro: Por favor, insira um número válido para o raio.")
except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
import re

try:

    texto = input("Digite um texto: ")

    if re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", texto):
    
        print(f"Texto em maiúsculas: {texto.upper()}")
    
    else:
        print("O texto deve conter apenas letras. Não são permitidos números ou caracteres especiais.")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
try:

    texto_min = input("Digite o seu nome e sobrenome: ")

    if re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", texto_min):
    
        print(f"Seu nome e sobrenome em letras minúsculas é: {texto_min.lower()}")
    
    else:
        print("O texto deve conter apenas letras. Não são permitidos números ou caracteres especiais.")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")
    
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

try:

    frase = input("Digite uma frase: ")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")
    
else:
    print(f"Texto em maiúsculas:{frase.strip()}")


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

try:
    
    data = input("Digite a data no formato dd/mm/aaaa: ")

   
    dia, mes, ano = data.split("/")

    if re.fullmatch(r"\d{2}", dia) and re.fullmatch(r"\d{2}", mes) and re.fullmatch(r"\d{4}", ano):
        print(f"Dia: {dia}")
        print(f"Mês: {mes}")
        print(f"Ano: {ano}")
    else:
        print("O formato da data deve conter apenas números. Não são permitidos letras ou caracteres especiais.")
    
except ValueError:
    print("Erro! O formato da data deve ser dd/mm/aaaa.")
except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

try:
   
    string1 = input("Digite a primeira string: ")
    
    string2 = input("Digite a segunda string: ")

    if re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", string1) and re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", string2):
       
        resultado = string1 + string2
        print(f"A concatenação das duas strings é: {resultado}")
    else:
        print("Cada string deve conter apenas letras e espaços. Não são permitidos números ou caracteres especiais.")
    
except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

try:
    boll_valor_1 = input("Digite o primeiro valor booleano (True ou False): ")
    boll_valor_2 = input("Digite o segundo valor booleano (True ou False): ")


    if boll_valor_1.lower() not in ["true", "false"] or boll_valor_2.lower() not in ["true", "false"]:
        print("Digite um bool válido, apenas é aceito True ou False")
    else:
        valor1 = boll_valor_1.strip().lower() == "true"
        valor2 = boll_valor_2.strip().lower() == "true"

        resultado = valor1 and valor2

        print(f"O resultado da operação AND é: {resultado}")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
try:
    boll_or_valor_1 = input("Digite o primeiro valor booleano (True ou False): ")
    boll_or_valor_2 = input("Digite o segundo valor booleano (True ou False): ")


    if boll_or_valor_1.lower() not in ["true", "false"] or boll_or_valor_2.lower() not in ["true", "false"]:
        print("Digite um bool válido, apenas é aceito True ou False")
    else:
        or_valor1 = boll_or_valor_1.strip().lower() == "true"
        or_valor2 = boll_or_valor_2.strip().lower() == "true"

        resultado = or_valor1 or or_valor2

        print(f"O resultado da operação OR é: {resultado}")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
try:
    boll_invert = input("Digite o primeiro valor booleano (True ou False): ")


    if boll_invert.lower() not in ["true", "false"] :
        print("Digite um bool válido, apenas é aceito True ou False")
    else:
        boll_invert_min = boll_invert.strip().lower() == "true"
     
        resultado_inversao = not boll_invert_min

        print(f"O resultado da operação de inversão é: {resultado_inversao}")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
try:
    comp_val_1 = input("Digite o primeiro valor booleano (True ou False): ")
    comp_val_2 = input("Digite o segundo valor booleano (True ou False): ")


    if comp_val_1.lower() not in ["true", "false"] or comp_val_2.lower() not in ["true", "false"]:
        print("Digite um bool válido, apenas é aceito True ou False")
    else:
        low_comp_val_1 = comp_val_1.strip().lower() == "true"
        low_comp_val_2 = comp_val_2.strip().lower() == "true"

        resultado = low_comp_val_1 == low_comp_val_2
        
        if resultado == True:
            print("Os dois resultados são iguais:")
        else: 
            print("Os dois trsultados são diferentes")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
try:
    comp_val_1 = input("Digite o primeiro valor booleano (True ou False): ")
    comp_val_2 = input("Digite o segundo valor booleano (True ou False): ")


    if comp_val_1.lower() not in ["true", "false"] or comp_val_2.lower() not in ["true", "false"]:
        print("Digite um bool válido, apenas é aceito True ou False")
    else:
        low_comp_val_1 = comp_val_1.strip().lower() == "true"
        low_comp_val_2 = comp_val_2.strip().lower() == "true"

        resultado = low_comp_val_1 == low_comp_val_2
        
        if resultado == True:
            print("Os dois resultados são iguais:")
        else: 
            print("Os dois trsultados são diferentes")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")

# #### try-except e if

# 21: Conversor de Temperatura

try:
    celsius = float(input("Digite a temperatura em graus Celsius: ")) 
    fahrenheit = (celsius * 9/5) + 32
except ValueError:
    print("O valor fornecido não é um número válido. Tente novamente e digite um valor válido!")
    celsius = None  
    fahrenheit = None
except KeyboardInterrupt:
    print("\nVocê interrompeu a interação. Vamos finalizar.")
    celsius = None  
    fahrenheit = None

if fahrenheit is not None and celsius is not None:
    print(f"{celsius} graus Celsius corresponde a {fahrenheit} Fahrenheit.")

# 22: Verificador de Palíndromo
try:
    texto = input("Digite uma palavra ou frase: ").strip().lower()

    texto_limpo = ''.join(e for e in texto if e.isalnum())


    if texto_limpo == texto_limpo[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")

# 23: Calculadora Simples

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ").strip()

    # Verificação de números válidos e operações
    if re.fullmatch(r"^[+-]?(\d+(\.\d*)?|\.\d+)$", str(num1)) and re.fullmatch(r"^[+-]?(\d+(\.\d*)?|\.\d+)$", str(num2)) and operacao in ("+", "-", "*", "/"):
        
      
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: Divisão por zero não permitida.")
                resultado = None
            else:
                resultado = num1 / num2
    else:
        print("Entrada inválida. Certifique-se de que os números e a operação sejam válidos.")
        resultado = None

  
    if resultado is not None:
        print(f"O resultado da operação é: {resultado}")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")

except ValueError:
    print("Por favor, insira números válidos.")

# 24: Classificador de Números
try:
    numero = float(input("Digite um número: "))
    
    if re.fullmatch(r"^[+-]?(\d+(\.\d*)?|\.\d+)$", str(numero)):
   
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")
except ValueError:
    print("Por favor, insira um número válido.")
    
# 25: Conversão de Tipo com Validação
try:
 
    numero_str = input("Digite um número inteiro: ")

    if numero_str.isdigit():
        numero = int(numero_str)
        print(f"O número convertido para inteiro é: {numero}")
    else:
        print("Valor inválido! Por favor, digite um número inteiro.")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")
except ValueError:
    print("Por favor, insira um número válido.")
    