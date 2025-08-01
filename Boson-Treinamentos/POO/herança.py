# POO: PROGRAMAÇÃO ORIENTADA A OBJETOS
# HERANÇA


# EXEMPLO 1
class Veiculo:
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    def movimentar(self):
        print("Sou um veículo e me desloco!")

    # SETTER
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # GETTER
    def get_fabr_modelo(self):
        print(f"Modelo: {self.__modelo} - Fabricante: {self.__fabricante}.\n")

    def get_num_registro(self):
        return self.__num_registro


class Carro(Veiculo):  # Herança da classe "Veiculo"
    # Metodo "__init__" sera herdado
    def movimentar(self):
        print(f"Sou umn carro e corro pelas ruas!")


# EXEMLO 2
# Polimorfismo
class Motocicleta(Veiculo):
    def movimentar(self):
        print(f"Corro muito!")


class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat

    def movimentar(self):
        print(f"Eu voo alto!")


if __name__ == "__main__":
    # meu_carro = Carro("Volkswagem", "Polo")
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()

    # seu_carro = Carro("Audi", "AS SportBack")
    # seu_carro.movimentar()
    # seu_carro.get_fabr_modelo()

    # # Polimorfismo
    # moto = Motocicleta("Harley Davidson", "Nighster Special")
    # moto.movimentar()
    # moto.get_fabr_modelo()

    meu_aviao = Aviao("Boing", "747", "Comercial")
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f"Categoria: {meu_aviao.get_categoria()}")
    meu_aviao.get_categoria()
