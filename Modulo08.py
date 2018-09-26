# Modulo08.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
import turtle

# no código, usamos loops para repetir uma tarefa
# vamos nos divertir neste módulo desenhando objetos
# vamos usar loops para desenhar alguns dos nossos objetos
# olá tartaruga
# tartaruga é uma biblioteca python que permite desenhar

# você provavelmente pode adivinhar o que alguns dos comandos da tartaruga fazem:
# right(x) --> rotate right x degrees
# left(x) --> rotate left x degrees
# color("x") --> change pen color to "x"
# forward(x) --> move forward x
# backward(x) --> move backward x

# como poderíamos desenhar um quadrado?
turtle.clearscreen()
turtle.color('green')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# estamos basicamente repetindo as 2 primeiras linhas 4 vezes
# então nós vamos fazer isso:
turtle.clearscreen()
turtle.color('blue')
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)

# somente o código identado é repetido
turtle.clearscreen()
turtle.color('red')
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.forward(200)

# você pode se divertir quando coloca um loop dentro de outro loop
turtle.clearscreen()
turtle.color('yellow')
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for more_steps in range(4):
        turtle.forward(50)
        turtle.right(90)

# só porque é divertido
turtle.clearscreen()
turtle.color('purple')
for steps in range(5):
    turtle.forward(100)
    turtle.right(360 / 5)
    for more_steps in range(5):
        turtle.forward(50)
        turtle.right(360 / 5)

# você também pode usar uma variável para decidir o número de lados que o nosso objeto terá
turtle.clearscreen()
turtle.color('brown')
sides = 7
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(5):
        turtle.forward(50)
        turtle.right(360 / sides)

# você pode olhar para os valores de loop dentro do loop
for steps in range(4):
    print(steps)
# começa com 0, então vai imprimir 0, 1, 2, 3 (4 vezes)

# Se você precisar começar a contar a partir de "1", pode especificar números para contar de e para
for steps in range(1, 4):
    print(steps)
# ele executa até, por isso vai imprimir 1, 2, 3 (3 vezes)

# você também pode dizer ao loop para pular valores especificando uma etapa
for steps in range(1, 10, 2):
    print(steps)
# executa de 1 a 10, portanto, imprimiria 1, 2, 3, 4, 5, 6, 7, 8, 9
# mas como incrementa 2 por 2, na verdade seria impresso 1, 3, 5, 7, 9

# uma das coisas legais sobre python é a maneira que você pode dizer exatamente quais valores
# você deseja usar no loop
for steps in [1, 2, 3, 4, 5]:
    print(steps)
# neste caso, sim, será executado pelo último valor
# então isso imprimiria 1, 2, 3, 4, 5

# e você não precisa usar números!
turtle.clearscreen()
turtle.color('black')
for steps in ['red', 'blue', 'purple', 'black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)

# você pode até misturar diferentes tipos de dados, por exemplo, números e strings, mas isso pode causar alguns erros
for steps in ["red", "blue", "purple", "black", 8]:
    print(steps)

# Seu desafio
# pegar tartaruga para desenhar um octógono
# dica: para calcular o ângulo, você pega 360 graus e divide-o pelo número de lados da forma que está desenhando.
# desafio extra: deixe o usuário especificar quantos lados o objeto terá e desenhe o que eles pedirem
# desafio de bônus duplo: adicione um loop aninhado para desenhar uma versão menor do objeto dentro
# desafio regular
turtle.clearscreen()
turtle.color('red')
sides = 8
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)

# desafio extra
turtle.clearscreen()
turtle.color("orange")
sides = int(input('Quantos lados você quer? '))
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)

# desafio de bônus duplo
turtle.clearscreen()
turtle.color('blue')
sides = int(input('Quantos lados você quer? '))
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)
        for even_more_steps in range(sides):
            turtle.forward(25)
            turtle.right(360 / sides)
