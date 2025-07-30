# labels com tkinyter
# label simples

import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de Labels")

# criando o label
label = tk.Label(janela, text="Aula de labels")

# empacotar o label na jenala
label.pack()

# loop principal
janela.mainloop()
