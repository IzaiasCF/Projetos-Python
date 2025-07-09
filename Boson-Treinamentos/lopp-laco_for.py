# lista = [2,6,9,4,0,12,3,7]
# palavra = "Boson"

# for letra in palavra:
#   print(letra)

# função range
# for numero in range(1,11):
#   print(numero)

# OU:
# for numero in range(10):
#   print(numero)

# outro exemplo:
# nome = input("Digite seu nome: ")
# for x in range(10):
#   print(f"{x+1} {nome}")

# outro exemplo:
# for x in range(2,20,2):
#   print(x)

# tuplas
pedras = ("Rubi", "Esmelrada", "Quartzo", "Safira", "Diamante", "Turmalina")
for pedra in pedras:
  if pedra == "Quartzo":
    continue
  print(pedra)

