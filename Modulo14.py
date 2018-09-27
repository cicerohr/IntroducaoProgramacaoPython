# Modulo14.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
#
import sys

# erros de sintaxe são erros que a ferramenta de desenvolvimento pode detectar
# mas às vezes erros de digitação não podem ser detectados até que você execute o programa

# erros lógicos estão sintaticamente corretos, mas o programa não faz o que queremos fazer
salario = '5000'
bonus = '500'
salario_bruto = salario + bonus
print(salario_bruto)

# erros de runtime ocorrem quando o código basicamente funciona, mas algo fora do comum trava o código
# você escreve um programa de calculadora e um usuário tenta dividir um número por zero
# seu programa tenta ler um arquivo e o arquivo está faltando
# seu programa está tentando executar um cálculo de data e a data fornecida está no formato errado

# a quebra do código é uma experiência muito ruim para o usuário

# vamos criar um programa de calculadora que pegue dois números e os divida para o usuário
primeiro = input('Digite o primeiro número: ')
segundo = input('Digite o segundo número: ')

primeiro_numero = float(primeiro)
segundo_numero = float(segundo)

try:
    resultado = primeiro_numero / segundo_numero
    print(f'{primeiro_numero:.2f} / {segundo_numero:.2f} = {resultado:.2f}')
except:
    print('Desculpe, mas algo deu errado')
finally:
    print('Eu sempre rodarei. Eu sou útil para fechar o banco de dados ou arquivo de texto')
    print('É garantido que ele será executado, mesmo se você executar um sys.exit ()')

# agora tente dividir por zero
# a-ha! isso quebrou
# ZeroDivisionError: divisão decimal por zero

# você pode adicionar try/except em torno do código que gera o erro para lidar com isso graciosamente

# se você quiser saber qual foi o erro, você pode usar a função sys.exc_info ()

primeiro_numero = 3
segundo_numero = 0

try:
    resultado = primeiro_numero / segundo_numero
    print(f'{primeiro_numero:.2f} / {segundo_numero:.2f} = {resultado:.2f}')
except:
    erro = sys.exc_info()[0]
    print('Desculpe, mas algo deu errado')
    print(erro)

# depois de obter o nome do erro, você pode mostrar ao usuário uma mensagem específica
primeiro_numero = 3
segundo_numero = 0

try:
    resultado = primeiro_numero / segundo_numero
    print(f'{primeiro_numero:.2f} / {segundo_numero:.2f} = {resultado:.2f}')
except ZeroDivisionError:
    print('Desculpe, mas você não pode dividir por zero')

# como posso forçar meu programa a sair se ocorrer um erro e não quiser continuar?
# você pode usar a função sys.exit () na biblioteca sys
try:
    resultado = primeiro_numero / segundo_numero
    print(f'{primeiro_numero:.2f} / {segundo_numero:.2f} = {resultado:.2f}')
except ZeroDivisionError:
    print('Desculpe, mas você não pode dividir por zero')
    # sys.exit()
print("Ei! Eu nunca vou rodar!")

# você também pode usar variáveis ​​e uma instrução if para controlar o que acontece depois de um erro
erro = False
try:
    resultado = primeiro_numero / segundo_numero
    erro = False
except ZeroDivisionError:
    erro = True

if not erro:
    print(f'{primeiro_numero:.2f} / {segundo_numero:.2f} = {resultado:.2f}')

# existem muitas situações diferentes que podem causar erros no nosso código
# convertendo entre tipos de dados
# abrindo arquivos
# cálculos matemáticos
# tentando acessar um valor em uma lista que não existe

# como você sabe quais erros serão levantados?
# você pode testá-lo e quando ocorre um erro use a função sys.exc_info () para obter o nome do erro

# mas a coisa mais importante a fazer é testar!
# 1. executar seu código com tudo funcionando normalmente
# 2. executar seu código com entrada incorreta do usuário
# - digite letras em vez de números
# - insira 0 ou espaços
# - insira um valor no formato errado (por exemplo, datas)
# 3. tente outros cenários de erro, como arquivos ausentes
# 4. tentar qualquer coisa que você pode pensar que pode falhar seu código
# - inserindo números realmente grandes
# - números negativos

# eu preciso lidar com todos os erros possíveis? - às vezes escrever o código para lidar com os erros leva mais tempo
# do que escrever o programa original - se é necessário lidar com todos os erros possíveis depende de como o código
# será usado - se você está escrevendo um sistema para controle de tráfego aéreo, eu gostaria de um tratamento de
# erros muito completo

# seu desafio escrever código para abrir e ler um arquivo permite que o usuário especifique o nome do arquivo
# adicione tratamento de erros para fornecer uma mensagem de erro adequada se o arquivo especificado pelo usuário não
# puder ser encontrado
caminho = 'extra/'
nome_arquivo = input('Digite o nome do arquivo que você deseja ler: ')

try:
    meu_arquivo = open(caminho + nome_arquivo, "r")
    print(meu_arquivo.read())
    meu_arquivo.close()
except FileNotFoundError as e:
    print('Arquivo não encontrado!')
