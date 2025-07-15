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
# var_local = "Fabio dos Reis"   # variával fora da função

# def escreve_texto():
#     print(f"Variável Global: {var_global}")
#     print(f"Variável Local: {var_local}")

# if __name__ == "__main__":
#     print(f"Executando a função escreve_texto")
#     escreve_texto()

var_global = "Curso Completo de Python"
var_local = "Fabio dos Reis"  # variával fora da função

def escreve_texto():
    print(f"Variável Global: {var_global}")
    print(f"Variável Local: {var_local}")

if __name__ == "__main__":
    print(f"Executando a função escreve_texto")
    escreve_texto()

    print("Tentando aessar as variáveis diretamente: ")
    print(f"Variável Global: {var_global}")
    print(f"Variável Local: {var_local}")
