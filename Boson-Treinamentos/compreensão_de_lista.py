# EXEMPLO 1  -  cria-se listas sempre com colchetes
# numeros = [1,4,7,9,10,12,21]

# quadrados = list(map(lambda num: num**2, numeros))
# print(quadrados)

# EXEMPLO 2 - MELHOR MÉTODO ABAIXO:
numeros = [1, 4, 7, 9, 10, 12, 21]

quadrados = [num**2 for num in numeros]
print(quadrados)
