import PySimpleGUI as sg
import csv
from datetime import datetime
import os

# Nome do arquivo onde os dados serão armazenados
NOME_ARQUIVO = "historico_estoque.csv"
CABEÇALHO = ["DataHora", "Produto", "Tipo", "Quantidade"]

# --- Funções de Lógica (separadas da GUI) ---


def inicializar_arquivo():
    """Garante que o arquivo CSV exista e tenha um cabeçalho."""
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:
        with open(NOME_ARQUIVO, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(CABEÇALHO)


def carregar_dados():
    """Lê todos os dados do arquivo CSV para exibir na tabela."""
    inicializar_arquivo()  # Garante que o arquivo existe
    with open(NOME_ARQUIVO, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)  # Pula o cabeçalho
        # Converte o leitor para uma lista de listas
        return list(leitor_csv)


def salvar_movimento(tipo, produto, quantidade):
    """Salva uma nova linha de movimento no arquivo CSV."""
    if not produto or not quantidade:
        sg.popup_error(
            "Erro: Os campos 'Produto' e 'Quantidade' não podem estar vazios."
        )
        return False

    try:
        qtd_int = int(quantidade)
        if qtd_int <= 0:
            sg.popup_error("Erro: A quantidade deve ser um número positivo.")
            return False
    except ValueError:
        sg.popup_error("Erro: A quantidade deve ser um número inteiro válido.")
        return False

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nova_linha = [data_hora, produto, tipo, qtd_int]

    with open(NOME_ARQUIVO, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(nova_linha)

    sg.popup_quick("Movimento registado com sucesso!")
    return True


# --- Definição do Layout da Interface Gráfica ---

sg.theme("Dracula")  # Define um tema visual para a janela

# A tabela onde os dados serão exibidos
tabela_dados = sg.Table(
    values=carregar_dados(),
    headings=CABEÇALHO,
    max_col_width=25,
    auto_size_columns=False,
    justification="left",
    num_rows=20,
    key="-TABELA-",  # Uma "chave" para identificar este elemento
    row_height=25,
    display_row_numbers=True,
)

# A estrutura da janela, organizada em linhas
layout = [
    [sg.Text("Dashboard de Controlo de Estoque", font=("Helvetica", 20))],
    [tabela_dados],
    [
        sg.Text("Produto:", size=(8, 1)),
        sg.InputText(key="-PRODUTO-", size=(30, 1)),
        sg.Text("Quantidade:", size=(10, 1)),
        sg.InputText(key="-QUANTIDADE-", size=(10, 1)),
    ],
    [
        sg.Button(
            "Registrar Entrada", button_color=("white", "green"), key="-ENTRADA-"
        ),
        sg.Button(
            "Registrar Saída", button_color=("white", "firebrick"), key="-SAIDA-"
        ),
    ],
]

# --- Criação da Janela e Loop de Eventos ---

window = sg.Window("Gestor de Estoque v1.0", layout)

# O loop principal que mantém a janela aberta
while True:
    event, values = window.read()  # Espera por uma ação do utilizador

    # Se o utilizador fechar a janela ou clicar em "Sair"
    if event == sg.WIN_CLOSED:
        break

    # Se o utilizador clicar no botão "Registrar Entrada"
    if event == "-ENTRADA-":
        if salvar_movimento("Entrada", values["-PRODUTO-"], values["-QUANTIDADE-"]):
            # Limpa os campos de input e atualiza a tabela
            window["-PRODUTO-"].update("")
            window["-QUANTIDADE-"].update("")
            window["-TABELA-"].update(values=carregar_dados())

    # Se o utilizador clicar no botão "Registrar Saída"
    if event == "-SAIDA-":
        if salvar_movimento("Saída", values["-PRODUTO-"], values["-QUANTIDADE-"]):
            # Limpa os campos de input e atualiza a tabela
            window["-PRODUTO-"].update("")
            window["-QUANTIDADE-"].update("")
            window["-TABELA-"].update(values=carregar_dados())

# Fecha a janela ao sair do loop
window.close()
