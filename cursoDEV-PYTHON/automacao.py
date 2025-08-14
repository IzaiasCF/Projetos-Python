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
    pyautogui.press("Enter")  # "Enter" em maiúsculo
    # entrar no Teams
    time.sleep(2)
    pyautogui.write("https://teams.microsoft.com/v2/")
    pyautogui.press("Enter")
    time.sleep(2)
    # entrar na reunião
    pyautogui.press("enter")


# associar função a uma combinação de teclas
keyboard.add_hotkey("ctrl+alt+a", tarefa)

keyboard.wait("esc")
