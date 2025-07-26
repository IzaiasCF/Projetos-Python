# Manipulção de arqivos de texto


# EXEMPLO 1
# manipulador = open(
#     "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-treinamentos\\arquivos\\arquivo.txt",
#     "r",
#     encoding="latin1")

# print(f"\nMétodo read():\n")
# print(manipulador.read())  # read: leitura

# print(f"\nMétodo readline():\n")
# print(manipulador.readline())  # read: leitura em linha

print(f"\nMétodo readlines():\n")
print(manipulador.readlines())  # read: leitura do conteúdo dentro de uma lista


# EXEMPLO 2
try:
    manipulador = open("C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-treinamentos\\arquivos\\arquivo.txt", "r", encoding="latin1")
    for linha in manipulador:
        print(linha)

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()

