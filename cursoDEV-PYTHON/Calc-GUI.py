import tkinter as tk
import math


class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Completa")

        self.display = tk.Entry(
            master, width=35, borderwidth=5, justify="right", font=("Arial", 16)
        )
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        botoes = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
            ("=", 4, 3),
            ("C", 5, 0),
            ("⌫", 5, 1),
            ("sin", 1, 4),
            ("cos", 2, 4),
            ("tan", 3, 4),
            ("sqrt", 4, 4),
            ("^", 5, 4),
            ("ln", 1, 5),
            ("log10", 2, 5),
        ]

        for texto, linha, coluna in botoes:
            if texto == "=":
                botao = tk.Button(
                    master,
                    text=texto,
                    padx=40,
                    pady=20,
                    font=("Arial", 14),
                    command=self.calcular,
                )
            elif texto == "C":
                botao = tk.Button(
                    master,
                    text=texto,
                    padx=38,
                    pady=20,
                    font=("Arial", 14),
                    command=self.limpar,
                )
            elif texto == "⌫":
                botao = tk.Button(
                    master,
                    text=texto,
                    padx=38,
                    pady=20,
                    font=("Arial", 14),
                    command=self.apagar,
                )
            else:
                botao = tk.Button(
                    master,
                    text=texto,
                    padx=40,
                    pady=20,
                    font=("Arial", 14),
                    command=lambda t=texto: self.adicionar_ao_display(t),
                )

            botao.grid(row=linha, column=coluna)

    def adicionar_ao_display(self, valor):
        self.display.insert(tk.END, valor)

    def limpar(self):
        self.display.delete(0, tk.END)

    def apagar(self):
        self.display.delete(len(self.display.get()) - 1, tk.END)

    def calcular(self):
        try:
            expressao = self.display.get()
            if "^" in expressao:
                base, expoente = expressao.split("^")
                resultado = str(float(base) ** float(expoente))
            elif "sqrt" in expressao:
                numero = float(expressao.replace("sqrt", ""))
                resultado = str(math.sqrt(numero))
            elif "sin" in expressao:
                angulo = float(expressao.replace("sin", ""))
                resultado = str(math.sin(math.radians(angulo)))
            elif "cos" in expressao:
                angulo = float(expressao.replace("cos", ""))
                resultado = str(math.cos(math.radians(angulo)))
            elif "tan" in expressao:
                angulo = float(expressao.replace("tan", ""))
                resultado = str(math.tan(math.radians(angulo)))
            elif "ln" in expressao:
                numero = float(expressao.replace("ln", ""))
                resultado = str(math.log(numero))
            elif "log10" in expressao:
                numero = float(expressao.replace("log10", ""))
                resultado = str(math.log10(numero))
            else:
                resultado = str(eval(expressao))
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro")


if __name__ == "__main__":
    root = tk.Tk()
    calculadora = CalculadoraGUI(root)
    root.mainloop()
