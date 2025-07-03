# extrair servidor de email
nome = "Izaias Correa Filho"
email = "izaiasfalso@gmail.com"

# descobrir servidor de email.
posicao = email.find("@")
print(posicao)
servidor = email[posicao:] # com arroba
servidor = email[posicao:] # sem arroba
print(servidor)


# extrair peimero nome de usuário.
# contruir mensagem: Usuário Izaias Correa Filho cadastrado com sucessocom e o email.
# contruir mensagem: Enviamos um link de confirmação para o email i****ogmail.com.
