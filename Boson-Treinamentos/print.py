# Bóson Treinamentos

## condicional simple
# n1 = n2 = 0.0
# media = 0.0

# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# calcular média aritmética
# media = (n1 + n2) / 2

# if (media >= 7):
#     print("Aluno aprovado!")
#     print(f"Sua média é:", media)
# else:
#     print("Aluno reprovado!")
#     print(f"Sua média é:", media)

# Sintaxe
#  print(objetos, argumentos)

# nome = input("Digite seu nome: ")
# print("Olá, " + nome + ". Bem vindo ao curso de Python!")
# Ou: 
# nome = input("Digite seu nome: ")
# msg = "Olá, " + nome + ". Bem vindo ao curso de Python!"
# print(msg)

# Quebra de linha
# print("Imprime a mensagem e muda de linha.")
# print("Imprime a mensagem e permanece na linha.", end="")
# print(" Continuo na mesma linha.")

# Outras formas de concatebar mensagens
nome = "Maria"
idade = 30
#msg_formatada = "O noem dela é {0} e ela tem {1} anos.".format(nome,idade)
msg_formatada = "O noem dela é {0} e ela tem {1} anos.".format(nome,idade)
# print(msg_formatada)

nome = "Izaias"
peso = 70
msg = f"Olá, meu nome é {nome} e meu peso é {peso} quilos."
# print(msg)
# OU:
# print(f"Olá, meu nome é {nome} e meu peso é {peso} quilos.")

# outras formas de imprimir variáveis com textos
a = 10
b = 5
res = f"A soma de {a} com {b} é igual a {a+b}."
print(res)
