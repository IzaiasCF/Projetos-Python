# Calculadora em Python com função raiz quadrada

import tkinter as tk
import math


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.entrada = tk.Entry(
            root, width=35, borderwidth=5, font=('Arial', 14))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '%', '√',
        ]

        row = 1
        col = 0

        for botao in botoes:
            def comando(x=botao): return self.clicar_botao(x)
            tk.Button(root, text=botao, width=7, height=3, font=(
                'Arial', 12), command=comando).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def clicar_botao(self, valor):
        if valor == 'C':
            self.entrada.delete(0, tk.END)
        elif valor == '=':
            self.calcular()
        elif valor == '%':
            self.calcular_porcentagem()
        elif valor == '√':
            self.calcular_raiz()
        else:
            self.entrada.insert(tk.END, valor)

    def calcular(self):
        try:
            expressao = self.entrada.get()
            resultado = eval(expressao)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

    def calcular_porcentagem(self):
        try:
            expressao = self.entrada.get()
            valor = float(expressao)
            resultado = valor / 100
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

    def calcular_raiz(self):
        try:
            expressao = self.entrada.get()
            valor = float(expressao)
            resultado = math.sqrt(valor)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

root = tk.Tk()
calc = Calculadora(root)
root.mainloop()
