# botões com tkinter
# widget button

import tkinter as tk
from datetime import date

def mostrar_date():
    hoje = date.today()
    texto_data.set(hoje.strftime("%d/%m/%Y"))

# criar a janela principal
janela = tk.Tk()
janela.title("Mostrar a Data")
janela.geometry("300x200")
#janela.configure(bg="#add8e6")  # azul-claro - cor de fundo da janela

# variável para armazenar o texto do label
texto_data = tk.StringVar()

# label
label_data = tk.Label(janela, textvariable=texto_data, font=("Arial, 14"))
label_data.pack(pady=20)

# criar o btão
botao_data = tk.Button(janela, text="Mostrar Data", command=mostrar_date, bg="blue", fg="white")
botao_data.pack(pady=10)

# exibir janela
janela.mainloop()

# ------------------------------- Fim do script ------------------------------ #