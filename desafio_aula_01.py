nome = str(input("Digite nome: "))

salario = float(input("Digite seu salário: "))

percent_bonus = float(input("Digite o seu percentual de bônus: "))

valor_do_bonus = float(salario*(1+percent_bonus))

if percent_bonus < 0 or percent_bonus > 1: print("ERROR: Digite um número positivo válido")
else: print('{0} o seu bônus é de {1}'.format(nome,valor_do_bonus))

