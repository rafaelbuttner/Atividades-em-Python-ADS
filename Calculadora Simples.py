import time

def soma(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if a == 0 or b == 0:
        return 'Impossivel divisao por zero'
    else:
        return a/b


print('>>> Calculadora <<<')
while True:
    time.sleep(1)
    r1 = input('Selecione uma opcao:\n1- Soma\n2- Subtracao\n3- Multiplicacao\n4- Divisao\n5- Sair\n')
    if r1 in '5':
        break
    elif r1 not in '12345':
        print('Opcao invalida')
    else:
        r2 = int(input('Digite dois numeros para a operacao:\nPrimeiro numero: '))
        r3 = int(input('Segundo numero: '))

        if r1 in '1':
            print(f'Resultado = {soma(r2,r3)}\n')
        elif r1 in '2':
            print(f'Resultado = {sub(r2,r3)}\n')
        elif r1 in '3':
            print(f'Resultado = {mult(r2,r3)}\n')
        elif r1 in '4':
            print(f'Resultado = {div(r2,r3)}\n')
    
print('Programa finalizado.')

