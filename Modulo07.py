# Modulo07.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
# o elif permite verificar valores diferentesPaises = input("De onde você é? ")
pais = 'canadá'
if pais.capitalize == 'Canadá':
    print('Hello')
elif pais.capitalize == 'Alemanha':
    print('Guten Tag')
elif pais.capitalize == 'França':
    print('Bonjour')
else:
    print('Bom dia')

# e se você quiser verificar duas condições?
# and
idade = input('Quantos anos você tem? ')
genero = input('Qual é o seu sexo? ')

if float(idade) > 18 and genero == "masculino":
    print('Tudo bem, você pode assistir este vídeo')
else:
    print('Desculpe, você não pode assistir este vídeo')

# combinações possíveis de and
# false and false = false
# false and true  = false
# true  and false = false
# true  and true  = true

# e se você quiser verificar uma dessas condições?
# or
idade = input('Quantos anos você tem? ')
genero = input('Qual é o seu sexo? ')

if float(idade) > 18 or genero == 'masculino':
    print('Tudo bem, você pode jogar futebol')
else:
    print('Desculpe, você não pode jogar futebol')

# combinações possíveis do or
# false or false = false
# false or true  = true
# true  or false = true
# true  or true  = true

pais = ''
animal = ''

# há uma ordem de operações para and/or:
# and é avaliado primeiro
if pais == 'Canadá' and animal == 'alce' or animal == 'cavalo':
    print('Você joga hockey também?')

# isso automaticamente faria isso
if (pais == 'Canadá' and animal == 'alce') or animal == 'cavalo':
    print('Você joga hockey também?')

# Você tem que fazer isso:
if pais == 'Canadá' and (animal == 'alce' or animal == 'cavalo'):
    print('Você joga hockey também?')

# ou você também pode fazer isso:
pais_canada = False
if pais == 'Canadá':
    pais_canada = True

animal_correto = False
if animal == 'alce' or animal == 'cavalo':
    animal_correto = True

if pais_canada and animal_correto:
    print('Você joga hockey também?')

# você pode aninhar se instruções dentro de si

segunda = True
cafe_fresco = False

if segunda:
    # você poderia ter código aqui para verificar se há café fresco
    # a instrução if está aninhada, portanto, esta declaração if
    # só é executado se a outra declaração if for verdadeira
    if not cafe_fresco:
        print('Vá comprar um café!')
    print('Eu odeio segundas-feiras!')
print('agora você pode começar a trabalhar')

# seu desafio
# calcular o total para cobrar por um pedido de uma loja on-line no Canadá
# pergunte ao usuário de que país ele é e seu total de pedidos
# se o usuário for do Canadá, pergunte qual província
# se o pedido for de fora do Canadá, não cobra nenhum imposto
# se o pedido foi feito no Canadá, calcule o imposto com base na província
# - alberta = .05% imposto sobre vendas em geral
# # ontario, new brunswich, nova scotia charge .13% de imposto sobre vendas harmonizado
# - todas as outras províncias cobram 0,06% de imposto provincial sobre vendas + 0,05% de imposto GST

str_pais = input('De qual país você é? ')
str_pedido = input('Qual é o seu pedido total? $ ')
num_pedido = float(str_pedido)

if str_pais.upper() == 'CANADA':
    str_provincia = input('De qual província você é? ')

    if str_provincia.upper() == 'ALBERTA':
        # adicionando imposto geral sobre vendas
        num_pedido = num_pedido * 1.05
    elif str_provincia.upper() == 'ONTARIO' or str_provincia.upper() == 'NEW BRUNSWICH' or str_provincia.upper() == 'NOVA SCOTIA':
        # adicionando imposto sobre vendas harmonizado
        num_pedido = num_pedido * 1.13
    else:
        # adicionando imposto de vendas provincial
        num_pedido = num_pedido * 1.06
        # adicionando imposto geral sobre vendas
        num_pedido = num_pedido * 1.05

print(f'O preço total do seu pedido é $ {num_pedido:.2f}.')
