# abrindo outra janela ao clicar na janela inicial

import tkinter as tk

# criando seguna janela
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

    # definindo a geometria da janela 2
    segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

# criando janela principal
janela_principal = tk.Tk()
janela_principal.title("Janela principal")
janela_principal.geometry("600x500")

janela_principal.bind("<Buttom-1>", lambda event: abrir_segunda_janela())  ### (Buttom-1) botão esquerdo do mouse

