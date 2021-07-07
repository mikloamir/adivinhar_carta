'''

* definir um número secreto
* 3 tentativas adivinhar
* acertou: Você acertou o número secreto
* errou 3 tentativas: Que pena tente novamente!

'''

'''
i = 1
tentativas = 3
nSecreto = 5

while i <= 3 :
    print('-' * 30)
    print('Adivinhe o número secreto: ')
    print(f'Você tem mais {tentativas} tentativas!')
    print('-' * 30)
    tentativa = int(input('Digite um número: '))
    if tentativa == nSecreto :
        print('Você acertou o número secreto!')
        break
    else:
        tentativas -= 1
        print(f'Número incorreto, você tem mais {tentativas} tentativas!')
    i += 1
else:
    print('Que pena tente novamente!')
'''

'''

* Menu 2 opções: Jogar Advinhação ou Sair
* Se Jogar, exibir a lista e escolher mentamente 1 número
* 3 tentativas adivinhar
* Informar se o programa adivinhou o número escolhido mentamente
* Se 3 tentativas volta para o menu, escolher Jogar Advinhação (J) ou Sair (S)
* Se usuario digitar comando invalido informar

* acertou: Você acertou o número secreto
* errou 3 tentativas: Que pena tente novamente!

'''

x = 2
tentativas = 3
nSecreto = [1, 3, 6, 9, 8, 12]
opcao = " "

while opcao.upper() != 'S':

    print('-' * 30)
    print('Jogo adivinhação')
    opcao = input('Escolhar opção desejada: Jogar Advinhação (J) ou Sair (S)')
    print('-' * 30)

    if opcao.upper() != "J" and opcao.upper() != "S" :
        print('Opção invalida!')

    if opcao.upper() == "J" :

        print('Escolhar mentalmente um número secreto: ')
        print(f'{nSecreto}')
        print('-' * 30)

        while tentativas > 0:

            acertou = input(f'Número escolhido é {nSecreto[x]} , sim (Y) ou não (N): ')
            
            if acertou.upper() == 'Y' :
                print('Acertei o número secreto!')
                break

            elif acertou.upper() == 'N' :
                
                escolha = input('O número escolhido é maior (MA) ou menor (ME)')

                if escolha.upper() == 'MA' :
                    x += 1

                elif escolha.upper() == 'ME' :
                    x -= 1

            tentativas -= 1
        else:
            print("Que pena tente novamente!")

    '''
    while tentativas > 0 and opcao.upper() == "J":

        if tentativas == 3 :
            print('Escolhar mentalmente um número secreto: ')
            print(f'{nSecreto}')
            print('-' * 30)

        acertou = input(f'Número escolhido é {nSecreto[x]} , sim (Y) ou não (N): ')
        
        if acertou.upper() == 'Y' :
            print('Acertei o número secreto!')
            break

        elif acertou.upper() == 'N' :
            
            escolha = input('O número escolhido é maior (MA) ou menor (ME)')

            if escolha.upper() == 'MA' :
                x += 1

            elif escolha.upper() == 'ME' :
                x -= 1   

        tentativas -= 1
    else:
        print("Que pena tente novamente!")
    '''

    #21 cards
    #escolhe 1 carta
    #divide por 3
    #imprime 3 sequencias
    #escolhe uma sequecia correpondente a sua carta
    #21 cards
    #divide por 3
    #imprime 3 sequencias
    #escolhe uma sequecia correpondente a sua carta
    #21 cards
    #divide por 3
    #imprime 3 sequencias
    #escolhe uma sequecia correpondente a sua carta

    #distribuição em Z (ESQUERDA PARA DIREITA) final final da linha volta para o inicio da segunda linha
    #qual nipe e qualquer numero
    #não pode ser retido
    #escolheu sequecia
    #sequecia vai para o meio
    
    #escolheu sequecia
    #sequecia vai para o meio

    #distruibuir em Z pela terceira vezes

    #escolheu sequecia
    #sequecia vai para o meio

    #carta escolhica 11a
    #nove primeiras de um lado
    #nove ultimas do outro
    #sobra tres (meio carta escolhida)

    
