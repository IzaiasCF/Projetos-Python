# Escrever em arquivos de texto

# EXEMPLO 1
try:
    manipulador = open(
        "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt",
        "w",  # "w": escrita
        encoding="latin1",
    )
    manipulador.write("Bóson Treinamentos\n")
    manipulador.write("Como criar um arquivo de texto com Python.")

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()
