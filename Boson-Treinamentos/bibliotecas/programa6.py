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

    

