import random
palavras = ['desenvolvimento', 'tecnologia', 'computador', 'memoria', 'informacao', 'logica']
palavra_oculta = random.choice(palavras)
palavra_descoberta = ['_' for letra in palavra_oculta]
tentativas_restantes = 6
print('>>> Jogo da Forca <<<')
print(' '.join(palavra_descoberta))
print(f'Você tem {tentativas_restantes} tentativas para adivinhar a palavra oculta.')
while tentativas_restantes > 0 and '_' in palavra_descoberta:
    palpite = input('Tente uma letra: ').lower()
    if palpite in palavra_oculta:
        print('Certo!')
        for indice, letra in enumerate(palavra_oculta):
            if letra == palpite:
                palavra_descoberta[indice] = letra
    else:
        print('Errado!')
        tentativas_restantes -= 1
    print(' '.join(palavra_descoberta))
    print(f'Tentativas restantes: {tentativas_restantes}')
if '_' not in palavra_descoberta:
    print(f'Parabéns!\n Você adivinhou a palavra: {palavra_oculta}!')
else:
    print(f'Game Over!\n A palavra era: {palavra_oculta}.')