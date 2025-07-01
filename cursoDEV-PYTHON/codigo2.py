faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("Faturamento: R$", faturamento)
print("Lucro: R$", lucro)
print("Margem de lucro: ", margem_lucro, "%")

restituicao = imposto + 0.1

print("Restituição:", restituicao, "%")
