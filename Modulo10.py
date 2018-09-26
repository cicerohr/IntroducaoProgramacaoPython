# Modulo10.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
# você pode criar uma lista vazia e adicionar valores depois
convidados = []
contagem = []

# listas permitem que você armazene vários valores
convidados = ['Christopher', 'Suzy', 'Bill', 'John']
contagem = [78, 85, 62, 49, 98]

# você pode referenciar qualquer valor na lista especificando sua posição na lista
# imprima o primeiro convidado - o primeiro convidado está na posição 0
print(convidados[0])
# imprima a quarta pontuação - a quarta pontuação está na posição 3
print(contagem[3])

# você pode contar para trás
# imprime a última entrada na lista
print(convidados[-1])
# imprime a segunda última entrada na lista
print(convidados[-2])

# você pode alterar um valor em uma lista
print(f'O primeiro convidado foi {convidados[0]}')
convidados[0] = 'Michelle'
print(f'O primeiro convidado agora é {convidados[0]}')

# você pode adicionar um valor a uma lista com append ()
convidados.append('Zyon')
convidados.append('Olaf')
convidados.append('Ozzy')
convidados.append('Otta')
convidados.append('Luca')

# você pode remover um valor de uma lista com remove ()
convidados.remove('Ozzy')

# você também pode usar o comando del para excluir uma entrada
del convidados[0]

# a função index () pesquisará a lista e retornará o índice da posição em que o valor foi encontrado
# isto retornará o índice na lista onde o nome Olaf é encontrado
print(convidados.index('Olaf'))

# o que você acha que acontecerá se procurarmos um valor que não exista na lista?
# print (guests.index ("Marietta"))
# ValueError: 'Marietta' não está na lista

# você pode usar a função len () para descobrir quantas entradas estão na sua lista
num_entries = len(convidados)
print(num_entries)

print('--')

# looping através de uma lista (maneira menos inteligente)
for convidado in range(num_entries):
    print(convidados[convidado])

print('--')

# looping através de uma lista (inteligente)
for convidado in convidados:
    print(convidado)

print("--")

# você pode classificar sua lista com a função sort ()
# ordenar os convidados em ordem alfabética
convidados.sort()

# imprima novamente a lista
for convidado in convidados:
    print(convidado)

# seu desafio
# pedir ao usuário para inserir os nomes de todos que participaram de uma festa
# então retorne uma lista dos convidados da festa em ordem alfabética
# isso exigirá reunir tudo o que aprendemos até agora, então vamos percorrer o processo de pensamento
# de ideia para codificar

convidados = []
convidado = 'Qualquer'

while convidado != '':
    convidado = input('Qual é o nome do próximo convidado? (ou deixe vazio para sair) ')
    convidados.append(convidado)
convidados.sort()

for convidado_atual in convidados:
    print(convidado_atual)
