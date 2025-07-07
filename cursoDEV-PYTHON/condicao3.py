# Bóson Treinamentos
## condicional simple
n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# calcular média aritmética
media = (n1 + n2) / 2

if (media >= 7):
    print("Aluno aprovado!")
    print(f"Sua média é:", media)
else:
    print("Aluno reprovado!")
    print(f"Sua média é:", media)

