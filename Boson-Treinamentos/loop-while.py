# laço de repetição simples
# num = 1

# while (num <= 10):
#   num += 1  # incremento
  #print(num)
#print("Laço encerrado!")

# laço de repetição com if
nome = None

while True:
  print("Digite seu nome, ou x para parar:")
  nome = input()
  if nome == "x" or nome == "X":
    break  # fim do laço
  print(f"Bem-vindo, {nome}")

print("Até logo!")  # mensage de saída do laço

