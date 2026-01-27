import random
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
print ('-=-'*10)
print('Vamos jogar Jokenpô?')
print ('-=-'*10)
jogador = str(input('Escolha entre PEDRA, PAPEL ou TESOURA: ')).strip().upper()

sleep(1)

if jogador not in lista:
    print('Escolha inválida. Tente Novamente.')
    exit()

comp = random.choice(lista)
print(f'Eu escolhi...')
sleep(1)
print(f'{comp}')
sleep(1)
if (jogador == 'PEDRA' and comp == 'TESOURA'
        or jogador == 'TESOURA' and comp == 'PAPEL'
        or jogador == 'PAPEL' and comp == 'PEDRA'):
    print(f'Parabéns, você GANHOU! {jogador} ganha de {comp}')
elif jogador == comp:
    print('Haha, empatamos. Vamos novamente!')
else:
    print(f'Eu GANHEI!! {comp} ganha de {jogador}\n'
          f'Quer jogar novamente?')
