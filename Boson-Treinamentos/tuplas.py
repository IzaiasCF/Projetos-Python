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

print(halogenios[0:2])  # printar 02 elementos da lista a partir da posição zero(0) 
