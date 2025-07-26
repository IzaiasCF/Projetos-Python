# Manipulção de arqivos de texto
# Instale a biblioteca para o Python detectar caracteres latinos:
# pip install chardet


# EXEMPLO 1
# manipulador = open(
#     "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
#     "r",
#     encoding="latin1")

# print(f"\nMétodo read():\n")
# print(manipulador.read())  # read: leitura

# print(f"\nMétodo readline():\n")
# print(manipulador.readline())  # read: leitura em linha

# print(f"\nMétodo readlines():\n")
# print(manipulador.readlines())  # read: leitura do conteúdo dentro de uma lista


# EXEMPLO 2
# try:
#     manipulador = open(
#         "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
#         "r",
#         encoding="latin1")
#     for linha in manipulador:
#         linha = linha.strip()  # remove o último caracter da linha
#         print(linha)

# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()


# EXEMPLO 3
texto = str(input(f"Qual o termo que deseja procurar no arquivo? "))
try:
    manipulador = open(
        "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
        "r",
        encoding="latin1",
    )
    for linha in manipulador:
        linha = linha.rstrip()  # rstrip: remove o último caracter da linha
        if texto in linha:
            print(f"O termo foi encontrado.")
        print(linha)

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()
