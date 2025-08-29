import tkinter as tk
from tkinter import messagebox
import math


def verificar_numero():
    try:
        num = int(entrada.get())
        resultado = []

        # Par ou ímpar
        if num % 2 == 0:
            resultado.append(f"{num} é PAR")
        else:
            resultado.append(f"{num} é ÍMPAR")

        # Verifica se é primo
        if num < 2:
            resultado.append(f"{num} NÃO é primo")
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    resultado.append(f"{num} NÃO é primo")
                    break
            else:
                resultado.append(f"{num} é PRIMO")

        # Fatorial
        if num >= 0:
            resultado.append(f"Fatorial de {num} é {math.factorial(num)}")
        else:
            resultado.append("Fatorial não definido para números negativos")

        messagebox.showinfo("Resultado", "\n".join(resultado))

    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira um número inteiro válido.")


# Interface Gráfica
janela = tk.Tk()
janela.title("Analisador de Número")

tk.Label(janela, text="Digite um número inteiro:").pack(pady=10)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Verificar", command=verificar_numero)
botao.pack(pady=10)

janela.mainloop()
