# input para faturamento

# definindo o float após o input
# vendas1 = input("Digite suas vendas do dia: ")
# vendas1 = float(vendas1)
# bonus1 = vendas1 * 0.01
# print(bonus1)

# definindo o float antes do input
# vendas2 = float(input("Digite suas vendas do dia: "))
# bonus2 = vendas2 * 0.01
# print(bonus2)
# vendas3 = float(input("Digite o valor de suas vendas do dia: "))
# bonus3 = vendas3 * 0.01
# print(vendas3)
# print(bonus3)

# Atenção ao concatenar variáveis
vendas_dia1 = input("Vendas do dia 1: ")
vendas_dia2 = input("Vendas do dia 2: ")
print(f"Total das Vendas: R$ {float(vendas_dia1) + float(vendas_dia2)}")
