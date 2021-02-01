import csv

create_file = open('pedidos.csv','w',newline='',encoding='utf-8')
hernane = csv.writer(create_file, delimiter=';')
janaina = ['ID', 'Nome', 'Valor Total']
hernane.writerow(janaina)

pedido1 = ['01', 'José', '24.00']
hernane.writerow(pedido1)
pedido2 = ['02', 'Carlos', '44.00']
hernane.writerow(pedido2)
pedido3 = ['03', 'Francisco', '64.00']
hernane.writerow(pedido3)
pedido4 = ['04', 'Kãzian', '25.00']
hernane.writerow(pedido4)

create_file.close()