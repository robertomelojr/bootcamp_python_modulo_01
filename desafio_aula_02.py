import re

try:
    nome = input("Digite seu nome: ").strip()
    
  
    if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
        print("Insira um nome válido!")
    else:
       
        try:
            salario = float(input("Digite seu salário: "))
        except ValueError:
            print("Insira um salário válido!")
            salario = None

        if salario is not None and salario >= 0:
           
            try:
                percent_bonus = float(input("Digite o seu percentual de bônus (em formato decimal, ex: 0.10): "))
                if percent_bonus < 0 or percent_bonus > 1:
                    print("ERROR: Digite um número positivo válido entre 0 e 1.")
                else:
                    bonus = salario * (1 + percent_bonus)
                    print(f'{nome}, o seu bônus é de R${bonus:.2f}')
            except ValueError:
                print("Por favor, insira um valor válido para o percentual de bônus.")
        else:
            print("Insira um salário válido!")

except KeyboardInterrupt:
    print("\nInteração interrompida pelo usuário.")
