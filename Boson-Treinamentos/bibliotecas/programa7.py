# botões com tkinter
# widget button

import tkinter as tk
from datetime import date

def mostrar_date():
    hoje = date.today()
    texto_data.set(hoje.strftime("%d/%m/%y"))

# criar a janela principal
janela = tk.Tk()
janela.title("Mostrar a Data")
janela.geometry("300x200")

# variável para armazenar o texto do label
texto_data = tk.StringVar()

# label
