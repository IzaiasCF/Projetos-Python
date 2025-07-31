# carregando imagens no label

import tkinter as tk
from tkinter import ttk, PhotoImage


# imagem centralizada
def centralizar_imagem(event):
    largura_janela = janela.winfo.width()
    altura_janela = janela.winfo.height()
    largura_imagem = imagem.width()
    altura_imagem = imagem.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_imagem.place(x=posicao_x, y=posicao_y)


# criar janela
janela = tk.Tk()
janela.title("Exibir janela")
janela.geometry("650x600")

# carregar imagem
imagem = PhotoImage(
    file="C:\\Users\\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\bibliotecas\\free.png"
)

# criar e exibir a imagem
lbl_imagem = ttk.Label(janela, image=imagem)

# centralizar a imagem ao redimisionar a janela
janela.bind("<Configure>", centralizar_imagem)

# inserir o label na janela
lbl_imagem.pack(pady=20)

# loop principal
janela.mainloop()
