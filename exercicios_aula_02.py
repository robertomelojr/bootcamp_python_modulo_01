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


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
