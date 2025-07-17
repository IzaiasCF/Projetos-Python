# Exceção é um objeto que representa um erro que ocorreu ao executar um programa
# Blocos try ... except

# EXEMPLO 1: se dividir por zero, vai dar erro!
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))

# r = round(n1 / n2, 2)

# print(f"Resulado: {r}")


# EXEMPLO 2: tratando exceções de erros com try .. except
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

try:
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print(f"Não é possível dividir por ZERO!")
else:
    print(f"Resulado: {r}")
