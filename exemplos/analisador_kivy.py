from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.input = TextInput(hint_text="Digite um número", multiline=False)
        self.add_widget(self.input)

        self.button = Button(text="Verificar")
        self.button.bind(on_press=self.verificar)
        self.add_widget(self.button)

        self.resultado = Label(text="")
        self.add_widget(self.resultado)

    def verificar(self, instance):
        try:
            num = int(self.input.text)
            resultado = []

            resultado.append(f"{num} é {'PAR' if num % 2 == 0 else 'ÍMPAR'}")

            if num < 2:
                resultado.append(f"{num} NÃO é primo")
            else:
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        resultado.append(f"{num} NÃO é primo")
                        break
                else:
                    resultado.append(f"{num} é PRIMO")

            if num >= 0:
                resultado.append(f"Fatorial: {math.factorial(num)}")
            else:
                resultado.append("Fatorial não definido para negativos")

            self.resultado.text = "\n".join(resultado)
        except ValueError:
            self.resultado.text = "Entrada inválida. Digite um número inteiro."


class NumeroApp(App):
    def build(self):
        return MainLayout()


NumeroApp().run()
