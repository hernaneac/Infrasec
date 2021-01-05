numeros = range(1,100)
print(numeros)
print(list(numeros))
print('')

for numero in numeros:
    print(f'O valor do range agora é: {numero}')

numeros_par = []
numeros_impar = []
print('')
for numero in numeros:
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print(f'Numeros pares {numeros_par}')
print(f'Números impar {numeros_impar}')
