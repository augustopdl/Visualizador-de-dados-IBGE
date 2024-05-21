from random import choice
from unidecode import unidecode_expect_nonascii

with open('palavras1.txt', encoding='utf-8') as file:
    palavras = file.read().split('\n')

palavra1 = choice(palavras)
palavra2 = unidecode_expect_nonascii(palavra1)
aux = ['_'] * len(palavra2)
erradas = set()
vidas = 5

while True:
    palpite = input('Digite uma letra: ')
    
    if palpite.lower() in palavra2:
        for i, letra in enumerate(palavra2):
            if letra == palpite:
                # substituir _ pelo palpite
                aux[i] = palavra1[i]
    else:
        erradas.add(palpite)
        vidas -= 1
    
    print(aux)
    print(erradas)
    print(f'Vidas: {vidas}')

    if ''.join(aux) == palavra1:
        print('Você ganhou!')
        break
    elif vidas == 0:
        print('Você perdeu!')
        print(f'A palavra era {palavra1}.')
        break
