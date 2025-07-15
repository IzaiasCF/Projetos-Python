# Funções - Modularização, Reuso de código, Legibilidade

# exemplo 1
# def mensagem():
#   print("Bóson treinamenrtos em Tecnologia")
#   print("Curso Completo de Python")
# mensagem()


# exemplo 2
# def soma(a, b):
#   print(a + b)
# soma(12,7)


# exemplo 3
# def mult(x, y):
#   return x * y

# a = 5
# b = 8
# c = mult(a, b)
# print(f"O produto de {a} e {b} é {c}.")


# exemplo 4
def div(k, j):
    return k / j

if __name__ == "__main__":
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))

    r = div(a, b)
    print(f"{a} dividido por {b} é igul a {r}.")

