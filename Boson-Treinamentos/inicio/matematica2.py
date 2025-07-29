def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


# Bloco de teste
if __name__ == "__main__":
    print("_Executando testes simples_")
    print("2 + 3 =", somar(2, 3))
    print("5 - 2 =", subtrair(5, 2))
    print("4 * 3 =", multiplicar(4, 3))
    print("10 / 2 =", dividir(10, 2))
