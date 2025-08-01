# Escrever em arquivos de texto

# EXEMPLO 1
# try:
#     manipulador = open(
#         "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
#         "w",  # "w": escrita
#         encoding="latin1"
#     )
#     manipulador.write("Bóson Treinamentos\n")
#     manipulador.write("Como criar um arquivo de texto com Python.")

# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()


# EXEMPLO 2
# try:
#     manipulador = open(
#         "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
#         "a",  # "a": append - acrescentar
#         encoding="latin1",
#     )
#     manipulador.write("\nPython é muito empregado em I.A.\n")
#     manipulador.write("A Inteligência Artificial veio para ficar!")

# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()

# print(manipulador)


# EXEMPLO 3
# texto = "\nPython é usado em ciência de dados extensivamente."  # com variavel
# try:
#     manipulador = open(
#         "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
#         "a",  # "a": append - acrescentar
#         encoding="latin1",
#     )
#     manipulador.write(texto)

# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()

# print(manipulador)


# EXEMPLO 4
frutas = ["Morango\n", "Uva\n", "Caju\n", "Amora\n", "Framboesa\n", "Graviola"]  # lista e  writelines
try:
    manipulador = open(
        "frutas.dat",
        "w",  # "a": append - acrescentar
        encoding="latin1",
    )

    manipulador.writelines(frutas)

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()

# Ler o arquivo criado
try:
    manipulador = open("frutas.dat", "r",encoding="latin1")
    print(manipulador.read())

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()
