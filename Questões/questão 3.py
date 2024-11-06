faturamento_mes = [16532, 23015, 15998, 17633, 25417, 16987, 13974, 18394, 15308, 25962, 18406, 23977, 17489, 15197, 23811, 14764, 18895, 23129, 27520, 24309, 25583, 18462, 27034, 25628, 15795, 20621, 24994, 23528, 22061, 16875]
maior = 0
soma = 0
menor = 99999
i = 0
for valor in faturamento_mes:
    if valor>maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma += valor
media = (soma/len(faturamento_mes))
for valor in faturamento_mes:
    if valor > media:
        i+=1



print("o maior faturamento do mês foi de: " + str(maior))
print("o menor faturamento do mês foi de: " + str(menor))
print("A quantidade de dia que o faturamento foi maior que a média é: " + str(i))
