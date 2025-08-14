import pyautogui
import keyboard
import time


# criando função
def tarefa():
    print("Rodando Automação")
    time.sleep(2)
    # abrir navegador
    pyautogui.press("win")
    time.sleep(2)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    # entrar no Teams


# associar função a uma combinação de teclas
keyboard.add_hotkey("ctrl+alt+a", tarefa)

keyboard.wait("esc")
