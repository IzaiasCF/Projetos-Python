# Trocar valores entre duas variáveis

# EXEMPLO 1

# var1 = 12
# var2 = 31

# var2, var1 = var1, var2

# print(f"var1: {var1}, var2: {var2}")


# EXEMPLO 2 - operador condicional ternário

# var1 = 12
# var2 = 31

# menor = var1 if var1 < var2 else var1
# print(f"Menor valor: {menor}")


# EXEMPLO 3 - generators
valores = [1,3,5,7,9,11,13,15]
quadrados = (item**2 for item in valores)
print(quadrados)

for valor in quadrados:
    print(valor)
