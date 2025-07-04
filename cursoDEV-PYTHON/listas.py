# LISTAA
vendas = [100, 50, 130, 80, 120, 200]

# print(vendas[2])  # vai mostrar na tela o ítem 2 da lista, no caso 130 (porque começa a contar do zero)
# print(vendas[-1])  # vai mostrar o último ítem da lista
# print(vendas[-2])  # vai mostrar o penúltimo ítem da lista
# print(vendas[-0])  # vai mostrar o primeiro ítem da lista

total_vendas = sum(vendas)  #  somar o tstoal do conteúdo da lista
print(total_vendas)  #  printa na tela o resultado

quantidade = len(vendas)  # quantidade de ítens na lista
print(quantidade)

valor_max = max(vendas)  # valor máximo
valor_min = min(vendas)  # vlalor mínimo
print(valor_max, valor_min)

posicao = vendas.index(130)  # indexação do ítem na lista
print(posicao)

