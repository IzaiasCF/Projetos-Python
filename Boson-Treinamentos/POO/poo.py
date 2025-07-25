# POO: PROGRAMAÇÃO ORIENTADA A OBJETOS  -  É UM PARADIGMA DE PROGRAMAÇÃO
# Classes e Objetos

# EXEMPLO 1
class Veiculo:
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante  # underscore duplo, encapsula a classe
        self.__modelo = modelo  # underscore duplo, encapsula a classe
        self.__num_registro = None  # underscore duplo, encapsula a classe

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


if __name__ == "__main__":
    meu_veiculo = Veiculo("GM", "Cadillac Escalade")
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro("490321-1")
    print(f"Registro: {meu_veiculo.get_num_registro()}\n")
