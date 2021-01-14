pedidos_dia1 = [
    {'cliente': 'José', 'pastel': 'Queijo'},
    {'cliente': 'Marcos', 'pastel': 'Queijo'},
    {'cliente': 'Carlos', 'pastel': 'Carne'},
    {'cliente': 'Hernane', 'pastel': 'Queijo'},
    {'cliente': 'José', 'pastel': 'Frango'},
    {'cliente': 'Janaína', 'pastel': 'bacalhau'},
]
pedidos_dia2 = [
    {'cliente': 'Fernando', 'pastel': 'Carne'},
    {'cliente': 'Flavia', 'pastel': 'Queijo'},
    {'cliente': 'Carlos', 'pastel': 'Calabresa'},
    {'cliente': 'Gustavo', 'pastel': 'Queijo'},
    {'cliente': 'José', 'pastel': 'Pizza'},
    {'cliente': 'Hernane', 'pastel': 'bacalhau'},
]

clientes_dia1 = set()
for pedido in pedidos_dia1:
    clientes_dia1.add(pedido['cliente'])
print(f'Dia 1 {clientes_dia1}')

clientes_dia2 = set()
for pedido in pedidos_dia2:
    clientes_dia2.add(pedido['cliente'])
print(f'Dia 2 {clientes_dia2}')

todos_cliente = clientes_dia1 | clientes_dia2
print(f'União{todos_cliente}')

cliente_comprou_todo_dia = clientes_dia1.intersection(clientes_dia2)
print(f'Interseção{cliente_comprou_todo_dia}')

cliente_diferença = clientes_dia1 - clientes_dia2
print(f'Diferença {cliente_diferença}')