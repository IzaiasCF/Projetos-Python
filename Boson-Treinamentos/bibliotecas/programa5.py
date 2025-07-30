# labels com ttk

import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de Labels")

# inserindo ícone
janela.iconbitmap(
    "C:\\Users\\\IzaiasCF\\Documents\\Projetos\\Projetos-Python\\Boson-Treinamentos\\bibliotecas\\favicon.ico"
)

# primeiro label
label1 = ttk.Label(
    janela, 
    text = "Texto do Label 1",
    font=("helvetica, 18")
)
label1.pack(ipadx=10, ipady=30)

# segundo label
label2 = ttk.Label(
    janela,
    text = "Texto do Label 2",
    font=("Arial", 20),
    foreground="blue"
)
label2.pack(ipadx=10, ipady=60)

janela.mainloop()
