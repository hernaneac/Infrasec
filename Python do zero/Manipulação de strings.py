nome_estabelecimento = 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
status = True
valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 6
valor_pastel4 = 6
print(nome_estabelecimento)
print(pastel1,valor_pastel1,status)
print(pastel2,valor_pastel2,status)
print(pastel3,valor_pastel3,status)
print(pastel4,valor_pastel4,status)

##Antes
...
print(pastel1,valor_pastel1,status)
print(pastel2,valor_pastel2,status)
print(pastel3,valor_pastel3,status)
print(pastel4,valor_pastel4,status)
...
print('Concatenacao')
print('')
mensagem = 'O nome do estabelecimento é ' + nome_estabelecimento
print(mensagem)

mensagem2 = 'O Preço do pastel de ' + pastel1 + ' é R$ ' + str(valor_pastel1)
print(mensagem2)

print('')
print('Interpolação')
print('')
print('O nome do estabelecimento é %s' %nome_estabelecimento)
print('O Valor do pastel de %s é de R$ %f' %(pastel1, valor_pastel1) )
print('O Valor do pastel de %s é de R$ %.2f' %(pastel1, valor_pastel1) )
print('O Valor do pastel de %s é de R$ %.3f' %(pastel1, valor_pastel1) )
print('O Valor do pastel de %s é de R$ %d' %(pastel3, valor_pastel3) )
print('O Valor do pastel de %s é de R$ %.3d' %(pastel3, valor_pastel3) )

print('')
print('Método Format')
print('')
print('O nome do estabelecimento é {}'.format(nome_estabelecimento))
print('O Valor do Pastel de {} é R$ {}'.format(pastel1,valor_pastel1))
print('O Valor do Pastel de {} é R$ {:.2f}'.format(pastel1,valor_pastel1))
print('O Valor do Pastel de {} é R$ {:03}'.format(pastel1,valor_pastel1))

print('')
print('Método f-String o mais recomendado')
print('')
print(f'O nome do estabelecimento é {nome_estabelecimento}')
print(f'O Valor do Pastel de {pastel1} é R$ {valor_pastel1}')
print(f'O Valor do Pastel de {pastel2} é R$ {valor_pastel2:.2f}')
print(f'O Valor do Pastel de {pastel3} é R$ {valor_pastel3:03}')