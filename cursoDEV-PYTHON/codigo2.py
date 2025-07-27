faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

# print("Faturamento: R$", faturamento)
# print("Lucro: R$", lucro)
# print("Margem de lucro: ", margem_lucro, "%")

# Mod - resto da divisão
#print(10 % 3)
#print("Restituição:", restituicao, "%")

# tempo_em_meses = 160
# tempo_em_anos = int(tempo_em_meses / 12)
# print(tempo_em_anos, "anos e", tempo_em_meses % 12, "meses")

# Arredondar (round)
numero = 123.37
print(round(numero))
    
faturamento = 139_018_182
print(faturamento)
 
print("Faturamento: R$", faturamento)
print("Lucro: R$", lucro)
print(round("Margem de lucro: ", margem_lucro(.2), "%"))
