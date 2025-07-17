# Exceção é um objeto que representa um erro que ocorreu ao executar um programa
# Blocos try ... except

# EXEMPLO 1
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))  # se dividir por zero, vai dar erro!

# r = round(n1 / n2, 2)

# print(f"Resulado: {r}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

# tratando exceções de erros com try .. except
try:
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print(f"Não é possível dividir por ZERO!")
else:
    print(f"Resulado: {r}")
