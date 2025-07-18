# FUNÇÕES LAMBDA (anônimas)
#   Sintaxe:
#   lambda argumentos: expressão

# EXEMPLO 1
# quadrado = lambda x: x**2

# for i in range(1, 11):
#   print(quadrado(i))


# EXEMPLO 2  # verificação se número e par
# par = lambda x : x %2 == 0
# print(par(8))
# print(par(9))


# EXEMPLO 3  # converção de temperatura
# f_c = lambda f: (f - 32) * 5/9
# print(f_c(212))


# EXEMPLO 4 - FUNÇÃO MAP()
# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)


# EXEMPLO 5
# palavras = ["python", "é", "uma", "linguagem", "de", "programação"]
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)


# EXEMPLO 6
# def numeros_pares(n):
#   return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_par = list(filter(numeros_pares, numeros))
# print(num_par)


# EXEMPLO 7
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(numeros)
# print(num_impar)


# EXEMPLO 8 - Função reduce()
# Sintaxe: reduce(função, sequência, valor_inicial)
# from functools import reduce

# def mult(x,y):
#   return x * y

# numeros = [1,2,3,4,5,6]

# total = reduce(mult, numeros)
# print(total)


# EXEMPLO 9 - Soma cumulativa dos quadrados dos valores, usando expressão lambda
from functools import reduce

numeros = [1, 2, 3, 4]

# intenção: ((1² + 2²)² + 3²)² + 4²
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)
