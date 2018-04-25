import random

print(' --- JOGO DA ADVINHAÇÃO --- \n Eu escolhi um numero entre 0 e 5, tente advinhar!')
print(' Chute qual o valor que eu pensei : ')
n = random.randint(0, 5)
v = int(input(' ---> '))

if n == v:
    print(' NICE! ACERTOU !')

else:
    print(' AHHH QUE PENA, VOCÊ ERROU, TENTE DENOVO ;-;!')
    while n != v :
        print(' --- JOGO DA ADVINHAÇÃO --- \n Eu escolhi um numero entre 0 e 5, tente advinhar!')
        print(' Chute qual o valor que eu pensei : ')
        n = random.randint(0, 5)
        v = int(input(' ---> '))
        print(" ")
        if n == v:
            print(' NICE! ACERTOU !')

        else:
            print(' AHHH QUE PENA, VOCÊ ERROU, TENTE DENOVO ;-;!')
