# Set - conjuntos em Python

# exemplo 1
planeta_anao = {"Plutão", "Ceres", "Eris", "Haumea", "Makemake",}

# print(planeta_anao)  # imprime o conteúdo de "planeta_anão"
# print(len(planeta_anao))  # imprime a quantidade de elementos de "planeta_ana"
# print("Ceres" in planeta_anao)  # IN: pergunta se "Ceres" está em "planeta_anao"

# print("lua" in planeta_anao)
# print("lua" not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper(), end="")  # imprime todo o conteúdo sem mudar de linha
#     print(astro.upper())

# exemplo 2
astros = ["Lua", "Vênus", "Sírius", "Marte", "Lua"]
print(astros, end=" ")
astro_set = set(astros)
print(astro_set)

