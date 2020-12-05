print('Seja bem vindo a Pastelaria Devops')
print('Faça seu pedido')

'''
0 - Estabelecimento fechado
1 - Estabelecimento aberto
'''
'''
status = 1
print(status == 1)
while status == 1 :
    item_pedido = input('Qual sabor do seu Pastel vc deseja: ')
    print(f'Pedido Confirmado')
    status = int(input('Digite 1 para fazer novos pedidos ou 0 para encerrar: '))
'''
contador = 0
quantidade_de_pedidos = 10
while contador < quantidade_de_pedidos:
    item_pedido = input('Qual sabor do seu Pastel vc deseja: ')
    print(f'Pedido Confirmado')
    contador += 1
    
   
