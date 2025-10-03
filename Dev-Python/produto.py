import csv
from datetime import datetime
import os

# Nome do arquivo onde os dados serão armazenados
NOME_ARQUIVO = 'historico_estoque.csv'

def registrar_movimento(tipo):
    """
    Registra uma entrada ou saída de produto e salva no arquivo CSV.
    
    Args:
        tipo (str): O tipo de movimento ('Entrada' ou 'Saída').
    """
    print(f"\n--- Registrar {tipo} de Produto ---")
    
    # Pede o nome do produto ao usuário
    produto = input("Digite o nome do produto: ")
    
    # Loop para garantir que a quantidade seja um número válido
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade > 0:
                break
            else:
                print("Erro: A quantidade deve ser um número positivo.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido para a quantidade.")

    # Pega a data e hora atuais e formata
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Prepara a linha de dados a ser salva
    nova_linha = [data_hora, produto, tipo, quantidade]
    
    # Abre o arquivo CSV no modo 'append' (para adicionar no final)
    # 'newline=""' evita que linhas em branco sejam criadas
    try:
        with open(NOME_ARQUIVO, mode='a', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.writer(arquivo)
            
            # Se o arquivo estiver vazio, escreve o cabeçalho primeiro
            if os.path.getsize(NOME_ARQUIVO) == 0:
                escritor_csv.writerow(['DataHora', 'Produto', 'Tipo', 'Quantidade'])
            
            # Escreve a nova linha com os dados do movimento
            escritor_csv.writerow(nova_linha)
            
        print(f"\n✅ {tipo} de {quantidade} unidade(s) de '{produto}' registrada com sucesso!")
        
    except IOError as e:
        print(f"\n❌ Erro ao escrever no arquivo: {e}")


def visualizar_historico():
    """
    Lê o arquivo CSV e exibe todos os movimentos registrados.
    """
    print("\n--- Histórico de Entradas e Saídas ---")
    
    try:
        with open(NOME_ARQUIVO, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            
            # Pula o cabeçalho
            cabecalho = next(leitor_csv, None)
            
            if not cabecalho:
                print("Nenhum movimento registrado ainda.")
                return

            # Imprime o cabeçalho formatado
            print(f"{cabecalho[0]:<20} | {cabecalho[1]:<25} | {cabecalho[2]:<10} | {cabecalho[3]:<10}")
            print("-" * 70)
            
            # Itera sobre cada linha do arquivo e imprime os dados
            for linha in leitor_csv:
                print(f"{linha[0]:<20} | {linha[1]:<25} | {linha[2]:<10} | {linha[3]:<10}")
                
    except FileNotFoundError:
        print("Nenhum movimento registrado ainda. O arquivo será criado no primeiro registro.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao ler o histórico: {e}")


def menu_principal():
    """
    Exibe o menu principal e gerencia a navegação do usuário.
    """
    while True:
        print("\n===== Controle de Estoque Simples =====")
        print("1. Registrar Entrada de Produto")
        print("2. Registrar Saída de Produto")
        print("3. Visualizar Histórico")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            registrar_movimento('Entrada')
        elif escolha == '2':
            registrar_movimento('Saída')
        elif escolha == '3':
            visualizar_historico()
        elif escolha == '4':
            print("Obrigado por usar o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()