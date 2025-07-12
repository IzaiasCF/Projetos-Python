# Dicionários

# exmplo 1
# elemento = {
#    "Z": 3,
#    "nome": "Lítio",
#    "grupo": "Metais Alcalinos",
#    "densidade": 0.534
# }

# print(elemento)
# print(f"Elemento: {elemento["nome"]}")  # imprime o que está contido em "nome"
# print(f"Densidade: {elemento["densidade"]}")  # imprime o que está contido em "densidade"
# print(f"O dicionário possui {len(elemento)} elementos.")  # imprime a quantidade de elementos de "elemento" (o Dicionário)

# # atualizar uma entrada
# elemento["grupo"] = "Alacalinos"
# print(elemento)

# # adicionar uma entrada
# elemento["período"] = 1
# print(elemento)

# # exclusão de ítens em dicionários
# del elemento["período"]
# print(elemento)

# # deletar todo o conteúdo do dicionário
# elemento.clear()
# print(elemento)

# # deletar todo o dicionário
# del elemento
# print(elemento)


# exemplo 2
elemento = {
   "Z": 3,
   "nome": "Lítio",
   "grupo": "Metais Alcalinos",
   "densidade": 0.534,
   "período": 1
}

print(elemento.items())
for i in elemento.items():
    print(i)  # imprime como lista

print(elemento.keys())
for i in elemento.keys():
    print(i)  # imprime somente as chaves

print(elemento.values())
for i in elemento.values():
    print(i)  # imprime somente os valores das chaves


