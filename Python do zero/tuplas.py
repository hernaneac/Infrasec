minha_tupla = ()
print(type(minha_tupla))

paste1 = ('Queijo', 6.00, True)
print(paste1)
print(paste1[1])


print('-----')
for info in paste1:
    print(info)

print('-----')

sabor, valor, status = paste1
print(sabor)
print(valor)
print(status)