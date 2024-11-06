palavra = str(input('Digite uma palavra: '))

palavra_invertida = ""

for i in range(len(palavra)):
    palavra_invertida += palavra[-1]
    palavra = palavra[:-1]
    
print(palavra_invertida)