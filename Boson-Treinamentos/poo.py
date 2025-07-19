# POO: PROGRAMAÇÃO ORIENTADA A OBJETOS  -  E UM PARADIGMA DE PROGRAMAÇÃO
# Classes e Objetos

# EXEMPLO 1
class Veiculo:
  def movimentar(self):
    print("Sou um veículo e me desloco!")

  def __init__(self, fabricante, modelo):
    self.fabricante = fabricante
    self.modelo = modelo
    self.num_registro = None

if __name__ == "__main__":
  meu_veiculo = Veiculo("GM", "Cadillac Escalade")
  meu_veiculo.movimentar()
  print(meu_veiculo.fabricante)
  print(meu_veiculo.modelo)

