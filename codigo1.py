faturamento = 1200  # número inteiro -> int
custo = 270

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1  # número decimal -> float

# texto -> string
# verdadeiiro ou falso -> boolean

imposto = taxa_imposto * faturamento

print("Faturamento: R$", faturamento)
print("Custo: R$", custo)
print("Imposto sobre faturamento: R$", imposto)
print("Lucro: R$", faturamento - custo - imposto)

