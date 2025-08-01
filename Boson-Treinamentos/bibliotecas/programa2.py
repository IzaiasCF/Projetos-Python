import tkinter as tk

# janela principal
janela = tk.Tk()

# título da janela
janela.title("Janela Principal")

# geometria da janela
janela.geometry("500x400+200+100")

# cor de fundo da janela
janela.config(bg="lightblue")

# largura máxima da janela
janela.maxsize(800, 600)
# largura minima da janela
# janela.minsize(300,200)
# sem possibilidade de redimensionar
# janela.resizable(False, False)
# janela em tela cheia
# janela.state("zoomed")

# janela transparente
# janela.attributes("-alpha", 0.6)

# inserindo ícones
janela.iconbitmap(
    "C:\\Users\\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\bibliotecas\\favicon.ico"
)

# acionar a janela
janela.mainloop()
