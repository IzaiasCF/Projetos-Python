# Manipulção de arqivos de texto

manipulador = open(
    "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-treinamentos\\arquivos\\arquivo.txt",
    "r",
    encoding="latin1")

# print(f"Método read():\n")
# print(manipulador.read())  # read: leitura

# print(f"Método readline():\n")
# print(manipulador.readline())  # read: leitura em linha

print(f"Método readlines():\n")
print(manipulador.readlines())  # read: leitura do conteúdo dentro de uma lista

