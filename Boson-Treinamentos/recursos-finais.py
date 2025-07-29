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
# valores = [1,3,5,7,9,11,13,15]
# quadrados = (item**2 for item in valores)
# print(quadrados)

# for valor in quadrados:
#     print(valor)



# EXEMPLO 4 - função enumarate()
# bebidas = ["Café", "Chá", "Água", "Suco", "Vinho"]
# for i, item in enumerate(bebidas):
#     print(f"Índice: {i}, Item: {item}")

# carros = ["Mustang", "Corvett", "Ferrari", "Masseratti", "Lamborghini"]
# for i, item in enumerate(carros):
#     print(f"Índice: {i} - Item: {item}")

# temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         total += 1

# print(f"Há {total} temperaturas negativas na amostra.")

# temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f"A temperatura em {i} e negativa, com {t} graus centigrados.")



# EXEMPLO 5 - gerenciamento de contexto com 'with'
# try:
#     a = open("c:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\frutas.dat", "r", encoding="latin1")
#     print(a.read())
# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# else:
#     a.close()

# esta sequência retorna a mesma coisa, mas com menos código:
with open("c:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\frutas.dat", "r", encoding="latin1") as a:
    for linha in a:
        print(linha, end="")  # (..., end="" ) - não pula linha ao imprimir

