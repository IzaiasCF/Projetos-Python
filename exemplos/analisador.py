# - Interface mais elegante e responsiva
# - Experiência do usuário mais fluida
# - Prevenção de erros comuns de entrada
# - Melhor usabilidade com teclado


import tkinter as tk
from tkinter import ttk, messagebox
import math

def verificar_numero(event=None):
    valor = entrada.get()
    if not valor.isdigit() and not (valor.startswith('-') and valor[1:].isdigit()):
        messagebox.showerror("Erro", "Digite um número inteiro válido.")
        return

    num = int(valor)
    resultado = []

    # Par ou ímpar
    resultado.append(f"{num} é {'PAR' if num % 2 == 0 else 'ÍMPAR'}")

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

# Centraliza a janela na tela
def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Interface Gráfica
janela = tk.Tk()
janela.title("Analisador de Número")
centralizar_janela(janela, 420, 260)
janela.resizable(False, False)

# Estilo ttk
estilo = ttk.Style()
estilo.theme_use("clam")

frame = ttk.Frame(janela, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Digite um número inteiro:", font=("Segoe UI", 12)).pack(pady=10)
entrada = ttk.Entry(frame, font=("Segoe UI", 12), width=25)
entrada.pack(pady=5)
entrada.focus()

botao = ttk.Button(frame, text="Verificar", command=verificar_numero)
botao.pack(pady=15)

# Atalho: Enter para verificar
janela.bind('<Return>', verificar_numero)

janela.mainloop()
