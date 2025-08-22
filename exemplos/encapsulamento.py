class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome  # Atributo privado
        self.__cpf = cpf  # Atributo privado

    # Métodos para acessar o nome
    def get_nome(self):
        return self.__nome  # "__": encapsulamento para proteger dados sensíveis

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    # Métodos para acessar o CPF (somente leitura)
    def get_cpf(self):
        return self.__cpf  # "__": encapsulamento para proteger dados sensíveis


# Criando uma pessoa
p = Pessoa("Izaias", "090.588.448-54")

# Acessando os dados de forma segura
print("Nome:", p.get_nome())
print("CPF :", p.get_cpf())
