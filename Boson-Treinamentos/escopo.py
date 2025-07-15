# Escopo global e local

# exemplo 1
var_global = "Curso Completo de Python"

def escreve_texto():
  var_local = "Fabio dos Reis"
  print(f"Variável Global: {var_global}")
  print(f"Variável Local: {var_local}")

if __name__ == "__main__":
  print(f"Executando a função escreve_texto")
  escreve_texto()
