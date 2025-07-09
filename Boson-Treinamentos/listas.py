# Lisa: representa uma sequência de valorers
# Sintaxe: nome_lista = [valores]

# exemplo 1
notas = [5, 7, 8, 6, 9]
print(notas)

# exemplo 2
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]
valores = n1 + n2
# print(valores)
# print(type(valores))

# exemplo 3
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]
valores = n1 + n2

# print(valores[0])  # print do primeiro valor na lista
# print(valores[6])  # print do sexto valor da
# print(valores[-1])  # print do último valor
# print(valores[-2])  # print do penúltimo valor

# exemplo 4
# valores[0] = 9  # Alterar valores em alguma posição
# print(valores[0])

# exemplo 5
# print(valores[0:2])  # imprime os valores de 0 a 2, na posição
# print(valores[:4])  # imprime os 04 primeros valores, na posição

# exemplo 5
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]
valores = n1 + n2
valores[0]= 9
print(len(valores))  # imprime a quantidade de elementos em ujma lista
print(sorted(valores))  # versão ordenada da lista
print(sorted(valores, reverse=True))  # imprime a lista em lrdem inversa

print(sum(valores))  # soma todos os valores dentro da lista
print(min(valores))  # mostra valor mínimo
print(max(valores))  # mostra valor máximo



