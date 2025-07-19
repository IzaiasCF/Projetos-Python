# POO: PROGRAMAÇÃO ORIENTADA A OBJETOS  -  É UM PARADIGMA DE PROGRAMAÇÃO
# Classes e Objetos

# EXEMPLO 1
class Veiculo:
  def movimentar(self):
    print("Sou um veículo e me desloco!")

  def __init__(self, fabricante, modelo):
    self.fabricante = fabricante
    self.modelo = modelo
    self.num_registro = None
    
# GETTER
def get_fabr_modelo(self):
  print(f"Modelo: {self.__modelo} - Fabricante: {self.__fabricante}.\n")

if __name__ == "__main__":
  meu_veiculo = Veiculo("GM", "Cadillac Escalade")
  meu_veiculo.movimentar()
  meu_veiculo.get_fabr_modelo()


