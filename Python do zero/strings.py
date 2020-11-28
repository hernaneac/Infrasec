nome_estabelecimento = 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
pastel5 = "Carne com queijo"
pastel6 = " Carne com frango "

print('------------')
print('')
print('Substituindo caracteres')
print(pastel5.replace('queijo','cheddar'))

novo_sabor = (pastel5.replace('queijo','merda'))
print(novo_sabor)
print(pastel5.upper())
print(pastel5.lower())
print(pastel5.startswith('queijo'))
print(pastel5.startswith('Carne'))
print(pastel5.endswith('queijo'))
print(pastel5.endswith('Carne'))
print(pastel6)
print('Pastel 6:', pastel6)

print('------------')
print('')

novo_pastel6 = pastel6.strip()
novo_pastel6 = pastel6.replace(' ', '-')
print('Com Traço', novo_pastel6)

print('------------')
print('')

novo_pastel6 = pastel6.rstrip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Sem Traço direita', novo_pastel6)
print('------------')
print('')

novo_pastel6 = pastel6.lstrip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Sem Traço esquerda', novo_pastel6)

print('####Função LEN ####')
print('Quantiadade caracteres pastel 5:',len(pastel5))

print('####Função Fatiamento ####')
print(pastel5[0])
print(pastel5[-1])
print(pastel5[0:4])
print(pastel5[4:])

print('####Função IN ####')
print()
result = 'queijo' in pastel5
print(result)
print()
print('####Função NOT IN ####')
print()
result = 'Frango' not in pastel5
print(result)
print()

