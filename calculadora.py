import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.entrada_texto = tk.StringVar()

        self.criar_interface()

    def criar_interface(self):
        entrada = tk.Entry(self.root, textvariable=self.entrada_texto, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, relief="ridge", justify='right')
        entrada.grid(row=0, column=0, columnspan=4, pady=20)

        botoes = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (texto, linha, coluna) in botoes:
            if texto == "=":
                tk.Button(self.root, text=texto, padx=20, pady=20, font=("Arial", 14), command=self.calcular).grid(row=linha, column=coluna)
            elif texto == "C":
                tk.Button(self.root, text=texto, padx=115, pady=20, font=("Arial", 14), command=self.limpar).grid(row=linha, column=coluna, columnspan=4)
            else:
                tk.Button(self.root, text=texto, padx=20, pady=20, font=("Arial", 14), command=lambda t=texto: self.adicionar_texto(t)).grid(row=linha, column=coluna)

    def adicionar_texto(self, texto):
        self.entrada_texto.set(self.entrada_texto.get() + texto)

    def limpar(self):
        self.entrada_texto.set("")

    def calcular(self):
        try:
            resultado = eval(self.entrada_texto.get())
            self.entrada_texto.set(str(resultado))
        except:
            self.entrada_texto.set("Erro")

# Executar a calculadora
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
