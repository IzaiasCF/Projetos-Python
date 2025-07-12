# exdmplo 1
# nome = "Izaias"
# letra = nome[2]  # [2] segunda letra de 'Izaias', a parir do zero
# print(letra)  # imprime na tela
# print(len(nome))  # (len) contagem da quantidade de elementos, ou letras, no caso

# exemplo 2
# nome = 'Izaias'
# escola = 'Bóson Treinamentos'
# print(nome + ' estuda na ' + escola + '.')

# exemplo 3
# email = input("Digite seu endereço de e-mail:")
# arroba = email.find("@")  # quantidade de elementos antes de '@'
# print(arroba)
# usuario = email[0:arroba]  # posição do primeiro nome até 'arroba'
# dominio = email[arroba + 1 :]  # posição após o 'arroba'
# print(usuario)
# print(dominio)

# exemplo 4
# produtos = 'cabornato de sódio e óxido de zinco'
# print('sódio' in produtos)  # verifica de ítem dentro de aspas está em 'produtos'
# print('magnésio' in produtos)
# print('magnésio' not in produtos)  # usando operador lógico 'not'

# exemplo 5
# item = 'hipoclorito'
# pos1 = item.find("clor")  # identifica a posição de 'clo' a parit de 0
# print(pos1)

# pos2 = item.find('flu')  # retorna '-1' porque 'flu' não está em pos2
# print(pos2)

# exemplo 6
# objeto_celeste1 = 'galáxia esPIral M31'
# print(objeto_celeste1.upper())  # upper: retorna tudo em maiúsculo

# objeto_celeste2 = 'galáxia ESPIRAL m31'
# print(objeto_celeste2.lower())  # lower: retorna tudo em minúsculo

# objeto_celeste3 = 'galáxia ESPIRAL M31'
# print(objeto_celeste3.capitalize())  # capitalize: retorna apenas a primeira letra da frase em maiúsculo

# objeto_celeste4 = "galáxia ESPIRAL M31"
# print(objeto_celeste3.title())  # title: retorna a primeira letra de cada palavra em maiúsculo

# exemplo 7
# suplemento = 'cloreto de magnésio'
# n_suplemnto = suplemento.replace('magnésio', 'zinco')   # '.raplace': substitue um termo por outro
# print(suplemento)
# print(n_suplemnto)

# exemplo 8
# frase = '     Ômega 3 é bom para  saúde    '
# print(frase)
# print(frase.strip())  # elimina espaós em branco no começo e no final da frase
# print(frase.lstrip())  # elimina espaço à esquerda
# print(frase.rstrip())  # elimina espaços à direita

# exemplo 9
# fruta = 'abacate'
# print(fruta)
# print(fruta.rjust(20))  # printa a palavra 20 espaços à direita
# print(fruta.ljust(20))  # printa a palavra 20 espaços à esquerda
# print(fruta.center(20))  # printa a palavra 20 espaços ao centro

# exemplo 10
# p = 'Bóson Treinamentos'
# print(p.startswith('Bó'))  # verifica se o termo 'Bó' está no COMEÇO do conteúdo - retorna verdadeiro ou falso
# print(p.startswith('b'))
# print(p.endswith('s'))  # verifica se o termo 's' está no FIM do conteúdo

# exemplo 11


