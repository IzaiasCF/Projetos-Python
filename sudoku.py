import tkinter as tk
from tkinter import messagebox
import random
import json
import time
import os
import copy

SAVE_FILE = "sudoku_save.json"

class Sudoku:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Avançado")
        self.window.geometry("700x800")
        self.difficulty = "fácil"
        self.entries = {}
        self.undos = []
        self.redos = []
        self.start_time = None
        self.elapsed_time = 0
        self.score = 1000
        self.timer_running = False

        self.show_timer = tk.BooleanVar(value=True)
        self.show_score = tk.BooleanVar(value=True)
        self.save_enabled = tk.BooleanVar(value=True)

        self.board = None
        self.solution = None

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        settings_frame = tk.LabelFrame(self.window, text="Configurações")
        settings_frame.pack(pady=5)
        tk.Checkbutton(settings_frame, text="Mostrar Cronômetro", variable=self.show_timer).pack(anchor='w')
        tk.Checkbutton(settings_frame, text="Usar Pontuação", variable=self.show_score).pack(anchor='w')
        tk.Checkbutton(settings_frame, text="Salvar Progresso", variable=self.save_enabled).pack(anchor='w')

        self.difficulty_label = tk.Label(self.window, text="Dificuldade:")
        self.difficulty_label.pack()
        self.difficulty_var = tk.StringVar(value=self.difficulty)
        self.difficulty_option = tk.OptionMenu(self.window, self.difficulty_var, "fácil", "médio", "difícil", command=self.change_difficulty)
        self.difficulty_option.pack()

        self.status_frame = tk.Frame(self.window)
        self.status_frame.pack(pady=5)
        self.timer_label = tk.Label(self.status_frame, text="Tempo: 00:00")
        self.timer_label.grid(row=0, column=0, padx=10)
        self.score_label = tk.Label(self.status_frame, text="Pontuação: 1000")
        self.score_label.grid(row=0, column=1, padx=10)

        control_frame = tk.Frame(self.window)
        control_frame.pack(pady=5)
        tk.Button(control_frame, text="Iniciar Jogo", command=self.start_game).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="Desfazer", command=self.undo).grid(row=0, column=1, padx=5)
        tk.Button(control_frame, text="Refazer", command=self.redo).grid(row=0, column=2, padx=5)
        tk.Button(control_frame, text="Verificar", command=self.check_solution).grid(row=0, column=3, padx=5)

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        self.stats_label = tk.Label(self.window, text="", justify='left', font=("Arial", 10))
        self.stats_label.pack(pady=10)

    def change_difficulty(self, level):
        self.difficulty = level
        self.start_game()

    def start_game(self):
        self.undos.clear()
        self.redos.clear()
        self.entries.clear()
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.board, self.solution = self.generate_unique_board()

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.board_frame, width=2, font=("Arial", 18), justify="center", bg="white")
                value = self.board[row][col]
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state='disabled', disabledforeground="black", bg="#e0e0e0")
                else:
                    entry.bind("<FocusIn>", lambda e, r=row, c=col: self.highlight_related(r, c))
                    entry.bind("<FocusOut>", lambda e, r=row, c=col: self.validate_input(r, c))
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[(row, col)] = entry

        self.start_time = time.time()
        self.elapsed_time = 0
        self.score = 1000
        if self.timer_running:
            self.window.after_cancel(self.timer_running)
        self.update_timer()

    def highlight_related(self, row, col):
        for r in range(9):
            for c in range(9):
                entry = self.entries[(r, c)]
                if r == row or c == col:
                    entry.config(bg="#ccf2ff" if entry['state'] != 'disabled' else "#e0e0e0")
                elif (r//3 == row//3) and (c//3 == col//3):
                    entry.config(bg="#d0ffd0" if entry['state'] != 'disabled' else "#e0e0e0")
                else:
                    entry.config(bg="white" if entry['state'] != 'disabled' else "#e0e0e0")

    def validate_input(self, row, col):
        entry = self.entries[(row, col)]
        value = entry.get()
        if value.isdigit() and 1 <= int(value) <= 9:
            self.undos.append(((row, col), self.board[row][col]))
            self.board[row][col] = int(value)
            self.redos.clear()
            self.score -= 1
        elif value == "":
            self.undos.append(((row, col), self.board[row][col]))
            self.board[row][col] = 0
            self.redos.clear()
            self.score -= 1
        else:
            messagebox.showwarning("Valor inválido", "Digite um número entre 1 e 9.")
            entry.delete(0, tk.END)
            self.score -= 5
        self.update_stats()

    def undo(self):
        if self.undos:
            (row, col), previous_value = self.undos.pop()
            current_value = self.board[row][col]
            self.board[row][col] = previous_value
            self.entries[(row, col)].delete(0, tk.END)
            if previous_value != 0:
                self.entries[(row, col)].insert(0, str(previous_value))
            self.redos.append(((row, col), current_value))
            self.score -= 2
            self.update_stats()

    def redo(self):
        if self.redos:
            (row, col), value = self.redos.pop()
            self.undos.append(((row, col), self.board[row][col]))
            self.board[row][col] = value
            self.entries[(row, col)].delete(0, tk.END)
            if value != 0:
                self.entries[(row, col)].insert(0, str(value))
            self.score -= 2
            self.update_stats()

    def check_solution(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[(row, col)].get()
                if value == "" or int(value) != self.solution[row][col]:
                    messagebox.showerror("Erro", "A solução está incorreta!")
                    self.score -= 10
                    return
        messagebox.showinfo("Parabéns!", f"Você venceu! Pontuação final: {self.score}")
        if self.save_enabled.get():
            os.remove(SAVE_FILE)

    def update_stats(self):
        row_counts = [set() for _ in range(9)]
        col_counts = [set() for _ in range(9)]
        box_counts = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = self.entries[(r, c)].get()
                if val.isdigit():
                    val = int(val)
                    row_counts[r].add(val)
                    col_counts[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    box_counts[box_index].add(val)
        stats = []
        for i in range(9):
            stats.append(f"Linha {i+1}: {sorted(row_counts[i])}")
        for i in range(9):
            stats.append(f"Coluna {i+1}: {sorted(col_counts[i])}")
        for i in range(9):
            stats.append(f"Bloco {i+1}: {sorted(box_counts[i])}")
        self.stats_label.config(text="\n".join(stats))

    def update_timer(self):
        if self.show_timer.get():
            self.elapsed_time = int(time.time() - self.start_time)
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.timer_label.config(text=f"Tempo: {minutes:02d}:{seconds:02d}")
        else:
            self.timer_label.config(text="")
        if self.show_score.get():
            self.score_label.config(text=f"Pontuação: {self.score}")
        else:
            self.score_label.config(text="")
        self.timer_running = self.window.after(1000, self.update_timer)
        if self.save_enabled.get():
            self.save_game()

    def generate_unique_board(self):
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def solve_board(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        nums = list(range(1, 10))
                        random.shuffle(nums)
                        for num in nums:
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve_board(board):
                                    return True
                                board[row][col] = 0
                        return False
            return True

        def remove_cells(board, attempts):
            while attempts > 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                if board[row][col] != 0:
                    backup = board[row][col]
                    board[row][col] = 0
                    board_copy = copy.deepcopy(board)
                    if not solve_board(board_copy):
                        board[row][col] = backup
                        continue
                    attempts -= 1

        full_board = [[0]*9 for _ in range(9)]
        solve_board(full_board)
        board = copy.deepcopy(full_board)
        difficulty_map = {"fácil": 35, "médio": 45, "difícil": 55}
        remove_cells(board, difficulty_map[self.difficulty])
        return board, full_board

    def save_game(self):
        data = {
            "board": self.board,
            "difficulty": self.difficulty,
            "time": self.elapsed_time,
            "score": self.score
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

if __name__ == "__main__":
    Sudoku().window.mainloop()
