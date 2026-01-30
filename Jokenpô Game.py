from random import choice
from time import sleep

print('='*35)
print('Seja bem vindo, selecione seu idioma\n'
      'Welcome, select your language')
print ('[A] English |  [B] Português')
print('='*35)

lingua = input('Selecione a opção / Select your option: ').strip().upper()

lista_port = ['PEDRA', 'PAPEL', 'TESOURA']
list_eng = ['ROCK', 'PAPER', 'SCISSOR']


sleep(0.5)

# ---------------------ENGLISH---------------------
if lingua in ('A', 'ENGLISH'):

    wins = 0
    losses = 0
    draws = 0

    while True:
        resposta = input("Let's play Rock, Paper or Scissor?\n"
                         "[A] YES | [B] NO\n"
                         "Your choice: ").strip().upper()
        if resposta in ('B', 'NO'):
            print('Ok, see you.')
            break

        elif resposta in ('A', 'YES'):
            while True:
                jogador = input('Choose Rock, Paper or scissor: ').strip().upper()
                if jogador in list_eng:
                    print('SHOOT')
                    sleep(1)
                    comp = choice(list_eng)
                    print(comp)
                else:
                    print('Invalid choice!')
                    continue
                if (jogador == 'ROCK' and comp == 'SCISSOR' or
                        jogador == 'SCISSOR' and comp == 'PAPER' or
                        jogador == 'PAPER' and comp == 'ROCK'):
                    wins += 1
                    print(f'Congratulations. YOU WON! {jogador} beat {comp}')
                elif jogador == comp:
                    draws += 1
                    print('It was a draw. Lets go again')
                else:
                    losses += 1
                    print(f"I WON!! {comp} beat {jogador}\n"
                          " TAKE CARE. I AM THE BEST\n"
                          "let's go again.")

                print(f'Score YOU: {wins} | Computer: {losses} | Draws {draws}')

                #-------------------------------VICTORY CONDITION-------------------------------
                if wins == 5:
                    print('🎉You reached 5 points! YOU WON THE GAME!')
                    print(f'Final score YOU: {wins} | Computer: {losses} | Draws: {draws}')
                    break

                elif losses == 5:
                    print('😈 I reached 5 points! I WON THE GAME!')
                    print(f'Final score YOU: {wins} | Computer: {losses} | Draws: {draws}')
                    break

# ---------------------PORTUGUÊS---------------------

elif lingua in ('B', 'PORTUGUÊS'):

    vitorias = 0
    derrotas = 0
    empates = 0

    while True:
       resposta = input('Vamos jogar Jokenpô?\n'
                        '[A] SIM | [B] NÃO\n'
                        'Sua escolha: ').strip().upper()
       if resposta == 'B' or resposta == 'NÃO':
           print('Ok, até mais')
           break
       elif resposta == 'A' or resposta == 'SIM':
           while True:
                jogador = input('Escolha Pedra, Papel ou Tesoura: ').strip().upper()
                if jogador in lista_port:
                   print('VALENDO')
                   sleep(1)
                   compt = choice(lista_port)
                   print(f'{compt}')
                else:
                   print('Escolha inválida, tente novamente')
                   continue
                if (jogador == 'PEDRA' and compt == 'TESOURA' or
                jogador == 'TESOURA' and compt == 'PAPEL' or
                jogador == 'PAPEL' and compt == 'PEDRA'):
                    vitorias +=1

                    print(f'Parabéns você GANHOU! {jogador} vence {compt}')
                elif jogador == compt:
                    empates += 1
                    print('Nós empatamos, vamos novamente!')
                else:
                    derrotas +=1
                    print(f'Eu GANHEI. {compt} vence {jogador}\n'
                          'Toma cuidado. Eu sou o melhor!\n'
                          'Vamos novamente!')
                print(f'Placar VOCÊ: {vitorias} | Computador: {derrotas} | Empates: {empates}')

                # -------------------------------CONDIÇÃO DE VITÓRIA-------------------------------

                if vitorias == 5:
                    print('🎉 VOCÊ CHEGOU A 5 PONTOS! VOCÊ GANHOU O JOGO!')
                    print(f'Placar final VOCÊ: {vitorias} | Computador: {derrotas} | Empates: {empates}')
                    break

                elif derrotas == 5:
                    print('😈 EU CHEGUEI A 5 PONTOS! EU GANHEI O JOGO!')
                    print(f'Placar final VOCÊ: {vitorias} | COMPUTADOR: {derrotas} | Empates: {empates}')
                    break
