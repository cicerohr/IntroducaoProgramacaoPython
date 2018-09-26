# Modulo09.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
import turtle

# às vezes precisamos realizar uma ação mais de uma vez
# despeje uma xícara de café para cada convidado
# lave os pratos até que estejam todos limpos
# faça um cartão de nome para cada convidado que participa de uma festa
# laços for nos permitem executar código por um número fixo de vezes
# por isso, se sabemos que há vinte convidados, podemos imprimir vinte cartões de nome
for guest in range(20):
    print(guest)

# laços while permitem que você execute até que uma determinada condição seja verdadeira
responda = '0'
while responda != '4':
    responda = input('Quanto é 2 + 2? ')

print('Sim! 2 + 2 = 4!')

# você pode descobrir o que esse código fará?
contador = 0
while contador < 4:
    turtle.forward(100)
    turtle.right(90)
    contador += 1

# o que acontece se você esquecer de incrementar o contador?
# um loop infinito!
# seja extremamente cuidadoso quando usar enquanto
# está tudo sob seu controle!

# é mais fácil cometer um erro com um laço while do que um laço for
# use laço for sempre que possível
# mas não tenha medo do laço while

# seu desafio
# criar e gravar um programa de esboço
# fazer com que o usuário insira uma cor de caneta, um comprimento de linha e um ângulo
# use tartaruga para desenhar uma linha com base em suas especificações
# deixá-los especificar novas linhas repetidamente até que elas insiram um comprimento de linha de 0
turtle.clearscreen()
comprimento_linha = 1
while comprimento_linha != 0:
    cor_caneta = input('Qual é a cor da caneta que você deseja para este esboço? ')
    comprimento_linha = input('Qual é o tamanho da linha que você deseja para este esboço? ')
    angulo = input('Qual é o ângulo que você deseja desenhar este esboço? ')
    turtle.color(cor_caneta)
    turtle.forward(int(comprimento_linha))
    turtle.right(int(angulo))
