'''
Sistema de Calaculo de IMC

O IMC é calculado dividindo o peso em kilos pela Altura  ao quadrado em Metros

- Menor que 18,5 = Magrelo
- Entre 18,5 e 24,9 = Peso Normal
- Entre 25,0 e 29,0 = Gordinho
- Entre 30,0 e 39,0 = Baleia
- Maior que 40,0 = Rolha de Poço
'''
'''
altura = float(input('Digite sua Altura (Ex: 1.75:): '))
peso = float(input('Digite seu peso (Ex: 82:): '))
print('')
imc = peso / (altura**2)
#** é o operador de potencia para fazer o peso ao quadrado
'''
imc = 40

if imc < 18.5:
    print(f' Seu IMC {imc} é de Magrelo destrunido')
elif imc >= 18.5 and imc <= 24.9:
    print(f' Seu IMC {imc} é de Pessoas Normais')
elif imc >= 25.0 and imc <= 29.9:
    print(f' Seu IMC {imc} é de Gordinho')
elif imc >= 30.0 and imc <= 39.9:
    print(f' Seu IMC {imc} é de Baleia')
else:
    imc >= 40.0
    print('Só Nauzara na causa')