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
    
class Carro(Veiculo):   # Herança da classe "Veiculo"
    # Metodo "__init__" sera herdado
    def movimentar():
        print(f"Sou umn carro e corro pelas ruas.")    


if __name__ == "__main__":
    meu_veiculo = Veiculo("GM", "Cadillac Escalade")
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro("490321-1")
    print(f"Registro: {meu_veiculo.get_num_registro()}\n")

    meu_carro = Carro("Volkswagem", "Polo")
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

