import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.configure(bg="#222222")
        self.root.geometry("400x600")
        self.equation = ""
        self.history = []

        self.display_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.root, bg="#222222")
        display_frame.pack(expand=True, fill="both")

        display_entry = tk.Entry(display_frame, textvariable=self.display_text, font=('Arial', 24), bd=10,
                                 relief=tk.RIDGE, bg="#333333", fg="#FFFFFF", justify="right")
        display_entry.pack(expand=True, fill="both", ipadx=8, ipady=15)

        # Buttons
        buttons_frame = tk.Frame(self.root, bg="#222222")
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ('7', '#444444'), ('8', '#444444'), ('9', '#444444'), ('/', '#FF9500'),
            ('4', '#444444'), ('5', '#444444'), ('6', '#444444'), ('*', '#FF9500'),
            ('1', '#444444'), ('2', '#444444'), ('3', '#444444'), ('-', '#FF9500'),
            ('0', '#444444'), ('.', '#444444'), ('=', '#00C853'), ('+', '#FF9500'),
            ('C', '#D50000'), ('←', '#FF5722'), ('%', '#FF9500'), ('Hist', '#2962FF')
        ]

        rows = 6
        cols = 4

        # Posição dos botões na grade
        positions = [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2), (4, 3)
        ]

        for index, (text, color) in enumerate(buttons):
            action = lambda x=text: self.on_button_click(x)
            grid_options = {
                "row": positions[index][0],
                "column": positions[index][1],
                "sticky": "nsew",
                "padx": 2,
                "pady": 2
            }
            button = tk.Button(buttons_frame, text=text, bg=color, fg="white", font=('Arial', 18),
                               relief=tk.FLAT, command=action)
            button.grid(**grid_options)

        # Ajustar expansão
        for i in range(rows):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(cols):
            buttons_frame.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.equation = ""
            self.display_text.set("")
        elif char == '←':
            self.equation = self.equation[:-1]
            self.display_text.set(self.equation)
        elif char == '=':
            try:
                result = str(eval(self.equation))
                self.history.append(f"{self.equation} = {result}")
                self.display_text.set(result)
                self.equation = result
            except Exception:
                messagebox.showerror("Erro", "Expressão inválida")
                self.equation = ""
                self.display_text.set("")
        elif char == 'Hist':
            self.show_history()
        elif char == '%':
            try:
                # Calcula porcentagem do último número da equação
                if self.equation:
                    last_number = ''
                    for c in reversed(self.equation):
                        if c.isdigit() or c == '.':
                            last_number = c + last_number
                        else:
                            break
                    if last_number:
                        percent = str(float(last_number) / 100)
                        self.equation = self.equation[:-len(last_number)] + percent
                        self.display_text.set(self.equation)
            except Exception:
                messagebox.showerror("Erro", "Erro ao calcular porcentagem")
        else:
            self.equation += str(char)
            self.display_text.set(self.equation)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Histórico de Cálculos")
        history_window.geometry("300x400")
        history_window.configure(bg="#333333")

        history_text = tk.Text(history_window, font=('Arial', 14), bg="#222222", fg="white")
        history_text.pack(expand=True, fill="both")

        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")

        history_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
    