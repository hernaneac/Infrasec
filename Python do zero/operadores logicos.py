nome_estabelecimento = 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
status = True
valor_pastel1 = 7.0
valor_pastel2 = 6.0
valor_pastel3 = 5,5
valor_pastel4 = 6
print(nome_estabelecimento)
print(pastel1,valor_pastel1,status)
print(pastel2,valor_pastel2,status)
print(pastel3,valor_pastel3,status)
print(pastel4,valor_pastel4,status)

print('O Valor do pastel 1 é igual ao valor do pastel2?', (valor_pastel1 == valor_pastel2))
print('O Valor do pastel 1 é menor que o valor do pastel2', (valor_pastel1 < valor_pastel2))
print('O Valor do pastel 1 é maior que o valor do pastel2', (valor_pastel1 > valor_pastel2))
print('O Valor do pastel 1 é menor ou igual que o valor do pastel2', (valor_pastel1 <= valor_pastel2))
print('O Valor do pastel 1 é maior ou igual que o valor do pastel2', (valor_pastel1 >= valor_pastel2))
print('O Valor do pastel 1 é diferente do valor do pastel2', (valor_pastel1 != valor_pastel2))

print('---------')
print('---------')
print('')
pagamento_pedido1_cartao = True
pagamento_pedido2_cartao = True
print('Precisa levar a maquina de cartão?', pagamento_pedido1_cartao and pagamento_pedido2_cartao)
print('---------')
print('---------')
print('')
pagamento_pedido1_cartao = True
pagamento_pedido2_cartao = True
print('Precisa levar a maquina de cartão?', pagamento_pedido1_cartao or pagamento_pedido2_cartao)
print('---------')
print('---------')
print('')
pagamento_pedido1_cartao = False
print('A máquina pode ficar?', not pagamento_pedido1_cartao)
