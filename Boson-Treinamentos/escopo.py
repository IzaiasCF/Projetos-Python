# Escopo global e local

# exemplo 1
# var_global = "Curso Completo de Python"

# def escreve_texto():
#   var_local = "Fabio dos Reis"   # variável dentro dsa função
#   print(f"Variável Global: {var_global}")
#   print(f"Variável Local: {var_local}")

# if __name__ == "__main__":
#     print(f"Executando a função escreve_texto")
#     escreve_texto()

# var_global = "Curso Completo de Python"
# var_local = "Fabio dos Reis"   # VARIAVEL DENTRO DA FUNÇÃO

# def escreve_texto():
#     print(f"Variável Global: {var_global}")
#     print(f"Variável Local: {var_local}")

# if __name__ == "__main__":
#     print(f"Executando a função escreve_texto")
#     escreve_texto()


# exemplo 2
# var_global = "Curso Completo de Python"
# var_local = "Fabio dos Reis"  # VARIÁVEL FORA DA FUNÇÃO

# def escreve_texto():
#     print(f"Variável Global: {var_global}")
#     print(f"Variável Local: {var_local}")

# if __name__ == "__main__":
#     print(f"Executando a função escreve_texto")
#     escreve_texto()

#     print("Tentando aessar as variáveis diretamente: ")
#     print(f"Variável Global: {var_global}")
#     print(f"Variável Local: {var_local}")   # NÀO seria imprimido na tela, se a variável 'var_local' estivesse dentro da função


# exemplo 3
var_global = "Curso Completo de Python"
var_local = "Fabio dos Reis"  # VARIÁVEL FORA DA FUNÇÃO

def escreve_texto():
    #global var_global

    print(f"Variável Global: {var_global}")
    print(f"Variável Local: {var_local}")

if __name__ == "__main__":
    print(f"Executando a função escreve_texto")
    escreve_texto()

    print("\nTentando aessar as variáveis diretamente: ")
    print(f"Variável Global: {var_global}")
    print(f"Variável Local: {var_local}")
