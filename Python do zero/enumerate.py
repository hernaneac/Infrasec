cardapio =['Carne', 'Queijo', 'Calabresa', 'Frango', 'Carne Seca']


print('Pastelaria Devops')
print('Escolha seu recheio')
print('---------------')
for indice, recheio in enumerate(cardapio):
    print(f'[{indice}]: {recheio}')

opcao = int(input('Digite o sabor desejado:'))
if opcao >=0 and opcao <= len(cardapio):
    print(f'O sabor escolhido foi: {cardapio[opcao]}')

else:
    print('Opção inválida')