import json

with open('meus pedidos.json') as file:
    json_data = json.load(file)

print(type(json_data))
print(json_data)
