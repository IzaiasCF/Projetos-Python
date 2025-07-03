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
# contruir mensagem: Usuário Izaias Correa Filho cadastrado com sucessocom e o email.
# contruir mensagem: Enviamos um link de confirmação para o email i****ogmail.com.
