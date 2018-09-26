# Modulo06.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
# IF permite que você especifique o código que só é executado se uma condição específica for verdadeira

resposta = input('Você gostaria de remessa expressa por um extra de R$ 10? ')
if resposta.lower() == 'sim':
    print('Tudo bem!')
else:
    print('Ok, não tem problema.')

# você pode usar símbolos diferentes para verificar condições diferentes
# == é igual a                  if total == 1000:
# != não é igual a              if total != 1000:
# < é menor que                 if total < 1000:
# > é maior que                 if total > 1000:
# <= é menor ou igual a         if total <= 1000:
# >= é maior que ou igual a     if total >= 1000:

time_favorito = input('Qual é o seu time favorito? ')
if time_favorito.lower() == "grêmio":
    print("Este é o time.")
print('Tudo bem se você prefere basquete')

# quase todas as declarações if podem ser escritas de duas formas
# if resposta == "sim":
# it not resposta == "não":

# if total < 100:
# if not total >= 100:

# e se tentarmos uma declaração if com números em vez de strings
str_deposito = input('Quanto você quer depositar? ')
num_deposito = float(str_deposito)

# também poderia ter feito assim:
# tmp_deposit = float (input ("Quanto você deseja depositar?"))

if num_deposito > 100:
    print('Você ganha uma torradeira grátis!')
else:
    print('Aproveite sua caneca!')
    print('Tenha um bom dia!')

# pode-se usar variáveis ​​booleanas para lembrar se uma condição é verdadeira ou falsa
str_deposito = input('Quanto você quer depositar? ')
num_deposito = float(str_deposito)
bol_torradeira = False

if num_deposito > 100:
    bol_torradeira = True

if bol_torradeira:
    print("Aproveite sua torradeira grátis!")

# seu desafio
# calcular as despesas de envio para um comprador
# pedir ao usuário para inserir o valor da compra total
# se o valor for menor que R$ 50,00 acrescente R$ 10,00 caso contrário o frete é grátis
# informe ao usuário o total final incluindo os custos de envio e formate o número para que pareça um valor monetário
# não se esqueça de testar sua solução com um valor > 50, um valor < 50 e um valor de exatamente 50

num_custo_remessa = 10
str_preco_produto = input('Qual é o valor total dos produtos que você está comprando? R$ ')
num_preco_produto = float(str_preco_produto)
if num_preco_produto >= 50:
    num_custo_remessa = 0

num_total_purchase = num_preco_produto + num_custo_remessa
print(f'O total da sua compra com envio incluído será R$ {num_total_purchase:.2f}')
