"""
Exemplo de pyhon....

"""
def realcar(func):
    def inner(*args, **kwargs):
        for a in args:
            print(f'parametro [{a}]')
        for a in kwargs:
            print(f'Chave: [{a}] valor[{kwargs[a]}]')
        print("*" * 30, "decorator.")
        func(*args, **kwargs)
        print("*" * 30, "decorator.")
    return inner

@realcar
def minha_funcao(str_teste=None):
    print(str_teste)

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    straux = 'Python '
    print_hi(straux)
    somatoria = 0
    string_teste = 'Flask'
    for i in range(10):
    	print(i, end=" ")
    print()
    for i in range(10):
        somatoria += i
        if i % 2 == 0:
            print(i, end=" - ")

    print('\nFormatar string no:',straux)
    print('1 somatoria: ' + str(somatoria))
    print('2 somatoria: ' + str(somatoria) + ' - ' + string_teste)
    print('3 somatoria: %d' % somatoria)
    print('4 somatoria: %d - %s' % (somatoria, string_teste))
    print('5 somatoria: {} - {}'.format(somatoria, string_teste))
    print(f'6 somatoria: {somatoria} - {string_teste}')
    print(f'7 somatoria: {somatoria} \n7B string: {string_teste}')
    str = "8 - Fomatar String 2 {}  {}".format(straux, string_teste)
    print (str)

    print('--------------------')
    minha_funcao('Aprendendo flask')
    print('--------------------')
    minha_funcao(str_teste='Flask é um Framework')
    print('--------------------')