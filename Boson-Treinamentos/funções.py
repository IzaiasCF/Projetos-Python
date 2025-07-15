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
# def div(k, j):
#     return k / j

# if __name__ == "__main__":
#     a = int(input("Digite um número: "))
#     b = int(input("Digite outro número: "))

#     r = div(a, b)
#     print(f"{a} dividido por {b} é igul a {r}.")


# exemplo 5
# def div(k, j):
#     if j != 0:   # tratamento de erro, caso o usuário digite ZERO
#         return k / j
#     else:
#         return "Impossível dividir por zero!"

# if __name__ == "__main__":
#     a = int(input("Digite um número: "))
#     b = int(input("Digite outro número: "))

#     r = div(a, b)
#     print(f"{a} dividido por {b} é igual a {r}.")


# exemplo 6
# def quadrado(val):
#   quadrados = []
#   for x in val:
#     quadrados.append(x ** 2)  # "x" com "**" e "2" está elevado ao quadrado
#   return quadrados

# if __name__ == "__main__":
#   valores = [2,5,7,9,12]
#   resultados = quadrado(valores)
#   for g in resultados:
#     print(g)


# exemplo 7
# def contar(num=11, caractere="+"):
#   for i in range(1, num):
#     print(caractere)

# if __name__ == "__main__":
#     contar(caractere="|")
#     contar(num=5)
#     contar(6, "@")


# exemplo 8
# def contar(caractere, num=11):
#     for i in range(1, num):
#         print(caractere)

# if __name__ == "__main__":
#     contar("#")


# exemplo 9
x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
  if c == 0:
    return a * b
  else:
    return a + b + c

if __name__ == "__main__":
    res = soma_mult(x, y)
    print(res)
