# Tratando EXCEÇÕES com RAISE

# EXEMPLO 1
# from math import sqrt

# if __name__ == "__main__":
#     try:
#         num = int(input("Digite um numero positivo: "))
#         if num < 0:
#             raise ArithmeticError
#     except ArithmeticError:
#         print(f"ERROR: Foi digitado um número negativo.")
#     else:
#         print(f"A raiz quadrada de {num} é {sqrt(num)}")
#     finally:
#         print(f"\n>>> FIM DO CÁLCULO <<<")


# EXEMPLO 2
from math import sqrt

class NumeroNegativoError(Exception):  # criando nossa própria classe de erros
    def __init__(self):
        pass

if __name__ == "__main__":
    try:
        num = int(input("Digite um numero positivo: "))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print(f"ERROR: Foi digitado um número negativo.")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print(f"\n>>> FIM DO CÁLCULO <<<")
