# Modulo04.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
#
# É importante poder armazenar e manipular números, bem como strings
idade = 42
print(idade)

# você pode realizar operações matemáticas em valores numéricos ou em variáveis ​​contendo valores numéricos
largura = 20
altura = 5

area = largura * altura
print(f'Área do retângulo: {area}')

# as duas maneiras estão corretas
perimetro = 2 * largura + 2 * altura
print(f'Perímetro do retângulo: {perimetro}')

perimetro = 2 * (largura + altura)
print(f'Perímetro do retângulo: {perimetro}')

# estas são as operações matemáticas mais comuns
# + adição 5 + 2 = 7
# - subtração 5 - 2 = 3
# * multiplicação 5 * 2 = 10
# / divisão 5 / 2 = 2.5
# ** exponenciação 5 ** 2 = 25
# % modulo 5 % 2 = 1

# regras de matemática aplicam-se
# ordem de operações
# () parenteses
# ** exponenciação (ex.: **2 quadrado **3 cubo)
# /* multiplicação e divisão
# +- adição e subtração

area = 0
altura = 10
largura = 20

# calcular a área de um triângulo
area = altura * largura / 2
print(f'Área do triângulo: {area}')

# às vezes você precisará formatar os números quando os exibir para os usuários

# Eu tenho 6 gatos (apenas convertendo esse número em uma string)
print(f'Eu tenho {6:d} gatos')
# Eu tenho 6 gatos (formatados como inteiros com espaços de preenchimento à esquerda para criar 3 dígitos)
print(f'Eu tenho {6:3d} gatos')
# Eu tenho 006 gatos (formatados como números inteiros com zeros de preenchimento à esquerda para criar 3 dígitos)
print(f'Eu tenho {6:03d} gatos')
# Eu tenho 6.000000 gatos (formatados como float padrão)
print(f'Eu tenho {6:f} gatos')
# Eu tenho 6.00 gatos (formatados como float com 2 casas decimais)
print(f'Eu tenho {6:.2f} gatos')

# outra maneira de fazer a mesma coisa
print('Aqui estão três números: %.2f, %.3f and %.4f' % (1, 2, 3))
# e aqui está outra maneira de fazer a mesma coisa
print('Aqui estão três números: {0:.2f}, {1:.3f} and {2:.4f}'.format(1, 2, 3))

# às vezes os comandos são muito longos para caber em uma única linha
# você pode usar um "\" para indicar que um comando continua na próxima linha
total = 5 + 6 + 8 + \
        3 + 2
print(total)

# pedir ao usuário por entrada numérica
str_idade = input('Quantos anos você tem? ')
int_idade = int(str_idade)
print(int_idade + 1)

salario = input('Por favor insira o seu salário: ')
bonus = input('Por favor insira seu bônus: ')
salario_liquido = salario + bonus
print(salario_liquido)

# existem funções para converter de um tipo de dados para outro:
# int(valor) converte em um inteiro
# long(valor) converte em um inteiro longo
# float(valor) converte em um número que pode conter casas decimais
# str(valor) converte em uma string

salario = input('Por favor insira o seu salário: ')
bonus = input('Por favor insira seu bônus: ')
salario_liquido = float(salario) + float(bonus)
print(salario_liquido)

# O que você acha que acontecerá se alguém digitar "BOB" como salário?
# vai dar erro.
# vamos aprender a lidar com erros mais tarde no curso


# seu desafio - crie uma calculadora de empréstimos
# solicitar que o usuário insira o custo do empréstimo, a taxa de juros e o número de anos para o empréstimo
# calcular pagamentos mensais com a seguinte fórmula:
# P = E [j (1 + j) n] / [(1 + j) n-1]
# P = pagamento mensal
# E = valor do empréstimo
# j = taxa de juros (para uma taxa de juros de 5%, i = 0,05)
# n = número de anos
str_emprestimo = input('Valor do empréstimo: ')
str_juros = input('Taxa de juro: ')
str_anos = input('Número de anos: ')

num_emprestimo = float(str_emprestimo)
num_juros = float(str_juros)
num_anos = float(str_anos)

num_pagamento = num_emprestimo * (num_juros * (1 + num_juros) * num_anos) / (((1 + num_juros) * num_anos) - 1)

print(f'O pagamento mensal será R$ {num_pagamento:.2f}')
