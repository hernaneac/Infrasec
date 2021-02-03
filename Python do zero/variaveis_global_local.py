EMPRESA = 'Infrasec'

def imprime_nome():
    global EMPRESA
    EMPRESA = 'Neppo'
    nome = 'Hernane'
    print(f' O {nome} trabalha na {EMPRESA}')

imprime_nome()
print(EMPRESA)