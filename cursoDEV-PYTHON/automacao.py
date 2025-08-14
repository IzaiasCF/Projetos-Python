import pyautogui
import keyboard
import time


# criando função
def tarefa():
    print("Rodando Automação")


# associar função a uma combinação de teclas
keyboard.add_hotkey("ctrl+alt+a", tarefa)

keyboard.wait("esc")
