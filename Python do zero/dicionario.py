cardapio = {}
print(type(cardapio))

pastel1 = {'sabor': 'queijo', 'valor': '6.00', 'status': True}
print(pastel1)
print(pastel1['sabor'])
print(pastel1['valor'])
print(pastel1['status'])
# print(pastel1['quantidade']) ##Key error, chave não econtrada

pastel1['valor'] = 7.00
print(pastel1)

print(pastel1.get('quantidade'))
if pastel1.get('quantidade'):
    print(pastel1)
else:
    pastel1['quantidade'] = 10
print(pastel1)

keys = pastel1.keys()
print(pastel1)
print('-----')
for key in keys:
    if key == 'status':
        print(f'A Chave {key} foi encontrada')
    else:
       pass
values = pastel1.values()
for value in values:
    print(f'O elemento {value} foi econtrado')

dict_itens = pastel1.items()
for key, value in dict_itens:
    print(f'A chave {key} foi econtrada e o valor é {value}')
print('-----')
pastel1.pop('status')
print(pastel1)