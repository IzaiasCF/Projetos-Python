# Escrever em arquivos de texto

# EXEMPLO 1
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
        else:
            print(f"Termo não encontrado!")
        print(linha)

except IOError:
    print(f"Não foi possível abrir o arquivo.")
else:
    manipulador.close()
