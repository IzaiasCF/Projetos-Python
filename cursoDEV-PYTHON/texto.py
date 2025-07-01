faturamento = 1000
custo = 700
email = "email_falso@gmail.com"

lucro = faturamento - custo

#print(f"Faturamento: R$ {faturamento:.2f}, Custo: R$ {custo:.2f}, Lucro: R$ {lucro:.2f}")
print(f"Faturamento: R$ {faturamento}, Custo: R$ {custo}, Lucro: R$ {lucro}")
print("E-mail:", email)

email2 ="EMAIL_falso@gmail.com" 
print(email2)  # mantendo upper case do exemplo acima
print(email2.lower())   # com lower case
print(email.upper())   # com upper case
print(email.find("@"))  # posição do @ dentro de email, começando a contar do zero

print(email[11])  # mostra o que está na posição [11]
print(email[11:])  # mostra o que está na posição [11:] até o final

print(email[12])  # mostra o que está na posição [12]
print(email[12:])  # mostra o que está na posição [12:] até o final

posicao = email.find("g")
servidor = email[posicao:]
print(servidor)

nome_email = email[:posicao]
print(nome_email)

# tamanho de um texto
tamanho = len(email)
print(tamanho)

# trocar um pedaço do email
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "izaias correa filho"
print(nome.capitalize())  # torna somente a primeira letra da primeira palavra em maiúscula: Izaias correa filho
print(nome.title())  # torna todas as  primeiras letras de cada palavra em maiúsculas: Izaias Correa Filho

#  formatação
print(f"Faturamento: R$ {faturamento:.2f}, Custo: R$ {custo:.2f}, Lucro: R$ {lucro:.2f}")

#  formatação : acrescenta  ".(ponto) e 02 zeros após o número" - e com uma vírgual na frente do ponto, fica com separador de milhar (veja em "faturamento")
print(f"Faturamento: R$ {faturamento:,.2f}, Custo: R$ {custo:.2f}, Lucro: R$ {lucro:.2f}")

