"""
mensagem_boas_vindas = 'Seja bem vindo a Pastelaria Devops'

nome_pedido1 = 'Carlos'
sabor_pedido1 = 'Carne'

nome_pedido2 = 'Pedro'
sabor_pedido2 = 'Frango'

print(f'O nome do cliente é {nome_pedido1} e o sabor do pastel é {sabor_pedido1}')
print(f'O nome do cliente é {nome_pedido2} e o sabor do pastel é {sabor_pedido2}')
"""

def mensagemboas_vindas(nome):
    print(f'Seja bem vindo a pastelaria {nome}')

def add_pedidos(nome,sabor):
    if len(nome) < 1:
        msg_erro = 'Insira o nome corretamente'
        return msg_erro
    novo_pedido = f'O cliente {nome} pediu pastel sabor {sabor}'
    return novo_pedido

mensagemboas_vindas(nome='Devops')
pedido1 = add_pedidos('Jose','Carne')
print(pedido1)
pedido2 = add_pedidos(nome='Pedro',sabor='Frango')
print(pedido2)
pedido3 = add_pedidos(nome='Hernane',sabor='Queijo')
print(pedido3)