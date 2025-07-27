# input para faturamento

# definindo o float após o input
# vendas1 = input("Digite suas vendas do dia: ")
# vendas1 = float(vendas1)
# bonus1 = vendas1 * 0.01
# print(bonus1)

# # definindo o float noo input
# vendas2 = float(input("Digite suas vendas do dia: "))
# bonus2 = vendas2 * 0.01
# print(bonus2)

## Atenção ao concatenar variáveis
vendas_dia1 = input("Vendas do dia 1: ")
vendas_dia2 = input("Vendas do dia 2: ")
print(f"Total das Vendas: R$ {float(vendas_dia1) + float(vendas_dia2)}")
