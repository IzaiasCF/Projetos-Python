# Escrever em arquivos de texto

# EXEMPLO 1
try:
    manipulador = open(
        "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
        "r",
        encoding="latin1")

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()
