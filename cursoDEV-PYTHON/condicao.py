"""
### CONDIÇÃO ###
< = maior
> = menor
>= = maior ou igual
<= = menor ou igual
== = igual
!= = diferente
"""

# condição
# faturamento = 1000
# custo = 1800
# lucro = faturamento - custo

# if lucro > 0:
#     print("Lucro R$", lucro)
# else:
#     print("Prejuízo!!!")
#     print(lucro)

# condição com listas
produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite aqui o novo produto: ")
novo_produto = novo_produto.lower()  # vai inserir na lista um novo produto, independente se digitarem em maiúsculo ou minúsculo

if novo_produto in produtos:
    print("Produto já cadastrado")
else:
    print("Produto cadastrado com sucesso!")
    produtos.append(novo_produto)  # acrescenta o novo produto à lista produtos
print(produtos)
