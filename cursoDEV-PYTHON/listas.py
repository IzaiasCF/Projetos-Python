# LISTAA
vendas = [100, 50, 130, 80, 120, 200]

# print(vendas[2])  # vai mostrar na tela o ítem 2 da lista, no caso 130 (porque começa a contar do zero)
# print(vendas[-1])  # vai mostrar o último ítem da lista
# print(vendas[-2])  # vai mostrar o penúltimo ítem da lista
# print(vendas[-0])  # vai mostrar o primeiro ítem da lista

# total_vendas = sum(vendas)  #  somar o tstoal do conteúdo da lista
# print(total_vendas)  #  printa na tela o resultado

# quantidade = len(vendas)  # quantidade de ítens na lista
# print(quantidade)

# valor_max = max(vendas)  # valor máximo
# valor_min = min(vendas)  # vlalor mínimo
# print(valor_max, valor_min)

# posicao = vendas.index(130)  # indexação do ítem na lista, a partir do zero
# print(posicao)
# print(vendas[2:])  # exclui os primeiros ítens e mostra o restante da esquerda da lista
# print(vendas[:2])  # pega os dois primeiros ítrens da lista e exclui o restante

produtos = ["iphone", "ipad", "airpod", "macbook"]
#print("iPhone" in produtos)  # verifica se condição é verdadeira e rwsponde se TRUE ou FALSE, no caso, é TRUE
#print("Vision Pro" in produtos)  # verifica se condição é verdadeira e rwsponde se TRUE ou FALSE, no caso, é FALSE

produtos = ["iphone", "ipad", "airpod"]
#produto_usuario = input("Digite o nome de um produto: ")
#print(produto_usuario in produtos)
precos = ["4000", "2000", "8000",]

# Atualização de lisats

# edita um ítem
#print("iphone" in produtos)
precos[0] = 4500
precos[0] = precos[0] * 1.1
novo_preco = precos[0] + 1.1
#print(precos)

produtos.append("macbook")  # APPEND - adiciona um ítem à lista.

precos.append(10000)  # 
precos[0] = novo_preco
print(novo_preco)
print(produtos)
print(precos)

# remover um ítem
produtos.remove("macbook")
precos.pop(-1)
print(produtos)
print(precos)

# inserir um valor
produtos.insert(1, "airpod")
print(produtos)

# contar valores
print(produtos.count("airpod"))

