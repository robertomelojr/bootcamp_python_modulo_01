# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as informações corretas

import re

nome_try = 0
salario_try = 0

nome_valido = False
salario_valido = False
percent_bonus :float = 0.84 ## Vamos considerar que é um valor por cargo fixo do sistema

while not nome_valido:
    try:
        nome = input("Digite seu nome: ").strip()
           
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            
            nome_try += 1
            if nome_try == 3:
                print("Atenção:Na próxima tentativa errada o usuário será bloqueado.")
            elif nome_try == 4:
                print("Usuário bloquado, tentar novamente mais tarde.")
                exit()
            else: 
                print("Insira um nome válido!")
        else:
            print("Usuário válido")
            nome_valido = True
     
    except ValueError as e:
        print(e)
    
while not salario_valido:
    try:
        
        salario = float(input("Digite seu salário: "))
        
       
        if salario < 0:
            salario_try += 1
            if salario_try == 3:
                print("Atenção: Na próxima tentativa errada o usuário será bloqueado.")
            elif salario_try >= 4:
                print("Usuário bloqueado. Tente novamente mais tarde.")
                exit()
            else:
                print("O salário não pode ser negativo. Insira um valor válido.")
        else:
            
            print("Salário válido!")
            salario_valido = True
            bonus = salario * (1 + percent_bonus)
            print(f"Seu bônus é de R$ {bonus:.2f}")
    except ValueError:
        
        salario_try += 1
        if salario_try == 3:
            print("Atenção: Na próxima tentativa errada o usuário será bloqueado.")
        elif salario_try >= 4:
            print("Usuário bloqueado. Tente novamente mais tarde.")
            exit()
        else:
            print("Entrada inválida. Digite um número válido para o salário.")
