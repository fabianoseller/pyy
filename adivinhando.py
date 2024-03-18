from random import randint

print('#### Iníciando Jogo...te gruda de vereda ####')

random = randint(0, 10)
chute = 0;
chances = 10;
while chute != random:
    chute = input('Chute um número entre 0 a 10: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns Vivente/chinoca ...., Tu venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break;
        else:
            print('')
            if chute > random:
                print('Você errou Quera...!!! Dica: É um número menor.')
            else:
                print('Tu errou gauderio(a)!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu! mas qe barbaridade tchê')
            print('')
            break;
