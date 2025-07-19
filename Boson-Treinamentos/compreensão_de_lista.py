# EXEMPLO 1  -  CRIA-SE LISTAS COM COLCHETES
# numeros = [1,4,7,9,10,12,21]

# quadrados = list(map(lambda num: num**2, numeros))
# print(quadrados)

# EXEMPLO 2 - MELHOR MÉTODO ABAIXO:
# numeros = [1, 4, 7, 9, 10, 12, 21]

# quadrados = [num**2 for num in numeros]
# print(quadrados)


# EXEMPLO 3  -  CRIAR LISTA DE PARES DE 0 A 10
pares = [num for num in range(120) if num % 2 == 0]
print(pares)
