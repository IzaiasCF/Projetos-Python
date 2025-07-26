import matplotlib.pyplot as plt

# Dados simulados
valores = [10, 12, 9, 14, 13, 15, 11]

# Cálculo da média
media = sum(valores) / len(valores)
print(f"Média dos valores: {media:.2f}")

# Visualização
plt.plot(valores, marker="o", label="Valores")
plt.axhline(media, color="red", linestyle="--", label="Média")
plt.title("Gráfico de Valores")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.show()
