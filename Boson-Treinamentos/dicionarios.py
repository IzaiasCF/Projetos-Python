# Dicionários

# exmplo 1
elemento = {
   "Z": 3,
   "nome": "Lítio",
   "grupo": "Metais Alcalinos",
   "densidade": 0.534
}
print(elemento)
print(f"Elemento: {elemento["nome"]}")  # imprime o que está contido em "nome"
print(f"Densidade: {elemento["densidade"]}")  # imprime o que está contido em "densidade"
print(f"O dicionário possui {len(elemento)} elementos.")  # imprime a quantidade de elementos de "elemento" (o Dicionário)

# atualizar uma entrada
elemento["grupo"] = "Alacalinos"
print(elemento)

# adicionar uma entrada
elemento["período"] = 1
print(elemento)

# exclusão de ítens em dicionários
del elemento["período"]
print(elemento)

# deletar todo o conteúdo do dicionário
elemento.clear()
print(elemento)

# deletar todo o dicionário
del elemento
print(elemento)


