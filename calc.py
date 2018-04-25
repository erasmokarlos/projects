import math
rs = 's'
print('=-='*20)
print('=-='*20)
print('                       Autor - eramoks ')
while rs == 's':

    print('=-=' * 20)
    print('                 Calculadora multifuncional ')
    print('-=' * 13, ' MENU ', '-=' * 13)
    print('Qual tipo de conta vc deseja fazer?')
    print('Área                 [1]')
    print('forula de bhaskara   [2]')
    print('trigonometria        [3]')
    print('Volume               [4]')
    resposta = str(input())

    if resposta == '1':
        print('========== Área =========')
        print('Qual é a forma geométrica?')
        print('Quadrado  [1] ')
        print('Circulo   [2] ')
        print('retangulo [3]')
        print('Losango   [4]')
        print('Triangulo [5]')
        print('Retornar ao menu anterior [0]')
        resposta = str(input(' '))
        if resposta == '1' :
            print('')
            print(' --- QUADRADO --- ')
            l = float(input('Qual o valor do lado?  '))
            aq = l**2
            print('A área do quadrado é {}'.format(aq))
        elif resposta == '2' :
            print(' --- CIRCULO ---')
            r = float(input('Qual o valor do Raio? '))
            ac = (r**2) * 3,14
            print('A area do ciruclo é {}'.format(ac))
        elif resposta == '3' :
            print(' --- RETANGULO ---')
            b = float(input('Qual a base? '))
            h = float(input('Qual a altura?'))
            print('a Áre do retangulo é igual a {}'.format(b*h))
        elif resposta == '4' :
            print(' --- losango --- ')
            c = float(input('Qual o comprimento? '))
            h = float(input('Qual a altura? '))
            print('A area do losango é {}'.format((c*h)/2))
        else:
            print(' --- TRIANGULO --- ')
            b = float(input('Qual a base? '))
            h = float(input('Qual a altura? '))
            print('A area do triangulo é {}'.format((b*h)/2))
    elif resposta == '2':
            print('------- Calculadora do 2° Grau ----------')
            a = float(input('Quanto vale A? '))
            b = float(input('Quanto vale B? '))
            c = float(input('Quanto vale C ?'))
            if 4*a*c >= 0 :
                d = (b**2) - (4*a*c)
            else:
                d = (b**2) + (4*a*c)
            if d <= 0:
                print(' O valor de delta eh {}'.format(d))
                print('não é possivel fazer o caulculo com o delta negativo! ')
                exit()

            print(' O valor de delta eh {}'.format(d))
            b2 = b-(b*2)
            x1 = (b2+(d**0.5)) / (2*a)
            x2 = (b2-(d**0.5)) / (2*a)
            print('Sendo que o x1 é {} , e x2 é {}'.format(x1, x2))
    elif resposta == '3':
        print('======= TRIGONOMETRIA =======')
        print(' Teorema de pitagoras [1].\n relações Trigonometricas [2] ')
        resposta = str(input())

        if resposta == '1':
            ca = float(input('Qual o valor do Cateto adjacente? '))
            co = float(input('Qual o valor do cateto oposto? '))
            h = math.hypot(ca, co)
            print('A hipotenusa vale {}'.format(h))
        elif resposta == '2':
            print(' --- Relações trignometricas --- ')
            print(' Seno [1] \n Cosseno [2] \n Tangente [3] \n')
            resposta = input()
            if resposta == '1':
                print(' -- SENO --')
                aa = float(input('Qual o angulo que vc quer saber o seno? '))
                a = math.sin(aa)
                print('o valor do seno de {} é igual à {}'.format(aa, a))
            elif resposta == '2':
                print(' -- Cosseno -- ')
                aa = float(input(('Qual o angulo que vc quer saber o cosseno? ')))
                a = math.cos(aa)
                print('o valor do cosseno de {} é igual à {}'.format(aa, a))
            elif resposta == '3':
                print(' -- Tangente -- ')
                aa = float(input('Qual o angulo que vc quer saber a tangente? '))
                a = math.tan(aa)
                print('o valor da tangente de {} é igual à {}'.format(aa, a))
rs = input('Deseja Continuar? [S/N]')