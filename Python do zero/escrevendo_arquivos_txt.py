clientes = ['Celestino','Pedro','Carlos','Gustavo','Janaína','Hernane','Jose','Tropeço']
file = open('clientes.txt', 'w')
for cliente in clientes:
    print(f'Client {cliente} adicionado na lista')
    file.write(f'{cliente}\n')

file.close()