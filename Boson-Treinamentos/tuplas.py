# tuplas são IMUTÁVEIS!!!
# tupla = (2,4,6,7,9)
# print(tupla)

# exemplo 1
# halogenios = ("F","Cl","Br","I","At")
# print(len(halogenios))  # len: descobrir quantos elementos tem em "halogenios"
# print(halogenios[3])  # [3]: visualizar posição 3 da tupla halogenios
# print(halogenios[-1])  # [-1]: visualizar último ítem de halogenios

# exemplo 2
halogenios = ("F", "Cl", "Br", "I", "At")
gases_nobres = ("He", "Ne", "Ar", "Xe", "Kr", "Rn")
elementos = halogenios + gases_nobres
# print(elementos)

# t1 = (5, 2, 6, 8, 4, 5, 6, 4, 4, 0, 12, 223, 4, 5)
# print(t1.count(5))  # contar quantas vezes o elemento "5" aparece na lista

# print(halogenios[0:2])  # printar 02 elementos da lista a partir da posição zero(0)
# print(halogenios[:3])  # printar elemento do começo à posição 3
# print("F" in halogenios)  # perguntar se um elemento (no caso, "F") está na lista
# print("Fe" in halogenios)  # perguntar se um elemento (no caso, "Fe") está na lista

# exemplo 3
t1 = (5, 2, 6, 8, 4, 5, 6, 4, 4, 0, 12, 22, 4, 5)
# print(sum(t1))  # somar elemntos quando números
# print(min(t1))  # mostrar menor valor
# print(max(t1))  # mostrar maior valor

# OPERAÇÕES NAO DISPONÍVEIS EM TUPLAS: .sort(), .append(), .reverse(), .pop()
### TUPLAS SÃO IMUTÁVEIS ###

# exemplo 4
# for elemento in elementos:
#    print(f"Elemento químico: {elemento}")

# criar uma lista a partir de uma tupla
# grupo17 = list(halogenios)
# print(grupo17)

# grupo17 = list(halogenios)
# grupo17[0] = "H"
# print(grupo17)

# exemplo 5
# grupo1 = ["Li", "Na", "K", "Rb", "Cs", "Fr"]
# alcalinos = tuple(grupo1)
# alcalinos[0] = "H"  # não é possível inserir o ítem "H" na tupla alacalinos
# print(alcalinos)

grupo1 = ["Li", "Na", "K", "Rb", "Cs", "Fr"]
alcalinos = tuple(grupo1)  # TUPLE: transformar uma lista em tupla
# alcalinos[0] = "H"  # não é possível inserir o ítem "H" na tupla alacalinos
print(alcalinos)

## descobrir que tipo é uma lista
print(type(alcalinos))

## ordenar na tela o conteúdo de uma tupla
print(sorted(alcalinos))

## esta opção não é possóvel com uma tupla
print(alcalinos.sort())

