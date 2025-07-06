#  EXERCÍCIO
nome = "Izaias Correa Filho"
email = "izaiasfalso@gmail.com"

# descobrir servidor de email.
posicao = email.find("@")
print(posicao)
servidor1 = email[posicao:] # com arroba
servidor2 = email[posicao+1:] # sem arroba
print(servidor1)
print(servidor2)

# extrair peimero nome de usuário.
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]  # dois pontos na frente de "posicao" pega o priemrio ítem e exclui o restante
print(primeiro_nome)

# contruir mensagem: Usuário Izaias Correa Filho cadastrado com sucessocom e o email.
mensagem = f"Usuário {primeiro_nome} cadastrado com sucesso, com o email: {email}"
print(mensagem)

# contruir mensagem: Enviamos um link de confirmação para o email i****ogmail.com.
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmação para o email {primeira_letra}****{servidor2}"
print(mensagem2)

