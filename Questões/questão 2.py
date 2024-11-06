# Questão 2

lista = [0,1]
valor = int(input('Insira um valor: '))
n = 0
while n < valor:
    n = lista[-1] + lista[-2]
    lista.append(n)
print(lista)
if(lista[-1] == valor):
    print('O valor ' + str(valor) + ' pertence a sequencia')
else:
    print('O valor ' + str(valor) + " não pertence a sequencia")

