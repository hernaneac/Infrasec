import json

meus_pedidos = {
    'estabelecimento': 'Pastelaria Devops',
    'Pedidos': [
        {
            'cliente': 'Carlos',
            'Valor': '24.00'
        },
        {
            'cliente': 'Joao',
            'Valor': '25.00'
        }       
    ]
}
print(type(meus_pedidos))

json_data = json.dumps(meus_pedidos, indent=4)
print(type(json_data))

with open('meus pedidos.json', 'w') as file:
    json.dump(meus_pedidos, file, indent=4)

print('Serialização finalizada')
