# EXEMPLO 1  -  CRIA-SE LISTAS COM COLCHETES
# numeros = [1,4,7,9,10,12,21]

# quadrados = list(map(lambda num: num**2, numeros))
# print(quadrados)

# EXEMPLO 2 - MELHOR MÉTODO ABAIXO:
# numeros = [1, 4, 7, 9, 10, 12, 21]

# quadrados = [num**2 for num in numeros]
# print(quadrados)


# EXEMPLO 3  -  CRIAR LISTA DE PARES DE 0 A 10
# pares = [num for num in range(120) if num % 2 == 0]
# print(pares)


# EXEMPLO 4  -  DESCOBRINDO UMA OLISTA DE VOGAIS
# frase = "A lógica e apenas o princípio da sabedoria, e não o seu fim."
# vogais = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

# lista_vogais = [v for v in frase if v in vogais]
# print(f"A frase possui {len(lista_vogais)} vogais.")
# print(lista_vogais)


# EXEMPLO 5  -  DISTRIBUTIVA ENTRE VALORES DE 02 LISTAS
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)

