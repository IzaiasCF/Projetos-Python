# abrindo outra janela ao clicar na janela inicial

import tkinter as tk

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segunda Janela")
    segunda_janela.config(bg="#20EE70")

    # tamanho da janela
    largura_janela = 300
    altura_janela = 200

    # obtendo dimensões do monitor
    largura_tela = segunda_janela.winfo_screenmmwidth()
    altura_tela = segunda_janela.winfo_screenmmwidth()

    # calcular coordenadas para centralizar na tela a janela 2
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    

