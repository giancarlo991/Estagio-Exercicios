sp = 67836.45
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

lista = [sp, rj, mg, es, outros]
lista_nomes = ['SP', 'RJ', 'MG', 'ES','OUTROS']

soma = 0

for i in lista:
    soma += i

n = 0

while n<len(lista):
    porcentagem = (lista[n]/soma)*100
    print(f"{lista_nomes[n]}: {porcentagem:.2f}%")
    n+=1