faturamento = 1000
custo = 700
email = "email_falso@gmail.com"

lucro = faturamento - custo

print(f"Faturamento: R$ {faturamento}, Custo: R$ {custo}, Lucro: R$ {lucro}")
print("E-mail:", email)

email2 ="EMAIL_falso@gmail.com" 
print(email2)  # mantendo upper case do exemplo acima
print(email2.lower())   # com lower case
print(email.upper())   # com upper case
print(email.find("@"))  # posição do @ dentro de email, começando a contar do zero

print(email[11])  # mostra o que está na posição [11]
print(email[11:])  # mostra o que está na posição [11:] até o final

#print(email[12])  # mostra o que está na posição [12]
#print(email[12:])  # mostra o que está na posição [12:] até o final

posicao = email.find("g")
servidor = email[posicao:]
print(servidor)

nome_email = email[:posicao]
print(nome_email)
