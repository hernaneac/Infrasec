nome_estabelecimento = 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
status = True
valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 5.5
valor_pastel4 = 6
print(nome_estabelecimento)
print(pastel1,valor_pastel1,status)
print(pastel2,valor_pastel2,status)
print(pastel3,valor_pastel3,status)
print(pastel4,valor_pastel4,status)

print('-----------')
pedido1= (valor_pastel1+valor_pastel3)
print ('Valor pedido 1:',pedido1,type(pedido1))
print('-----------')
print('-----------')
pedido1= (valor_pastel1+valor_pastel3)
print ('Valor pedido 1:',pedido1,type(pedido1))
print('-----------')
print('-----------')
desconto=3.0
subtracao1=(pedido1-desconto)
print('Valor com desconto:',subtracao1)
