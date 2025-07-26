# Manipulção de arqivos de texto


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
#         encoding="windows-1252")
#     for linha in manipulador:
#         print(linha)

# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()


# EXEMPLO 3
import chardet

# Caminho do arquivo
caminho_arquivo = "C:\\Users\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\arquivos\\arquivo.txt"

# Primeiro: detectar a codificação
with open(caminho_arquivo, "rb") as f:
    resultado = chardet.detect(f.read())
    encoding_detectado = resultado["encoding"]
    print(f"Codificação detectada: {encoding_detectado}")

# Segundo: abrir o arquivo com a codificação detectada
try:
    with open(caminho_arquivo, "r", encoding=encoding_detectado) as manipulador:
        for linha in manipulador:
            print(linha)
except IOError:
    print("Não foi possível abrir o arquivo.")

else:
    manipulador.close()
