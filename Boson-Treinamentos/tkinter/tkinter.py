# INTERFACE GRÁFICA COM TKINTER

import tkinter as tk

janela = tk.Tk()
janela.title("Primeiro APP")
janela.geometry("300x100+20+20")

# criar e posicionar um label com uma mensagem
iblMsg = tk.Label(janela, text="Olá, pessoal!")
iblMsg.pack()

# exibir a janela
janela.mainloop()
