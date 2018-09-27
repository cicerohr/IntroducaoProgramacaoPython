# Modulo12.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
#
import csv

# ---------------------------------------------- #
# como lemos um arquivo com código?
# use a função open
print('(1)')
meu_arquivo = open('extra/12_tasmania.txt', 'r', encoding='utf-8')

# como lemos o conteúdo do arquivo?
# use o método read
conteudo_arquivo = meu_arquivo.read()
print(conteudo_arquivo)
# como você pode ver, o método read retorna _todo o conteúdo do arquivo em uma string grande

# não esqueça de sempre fechar o arquivo
meu_arquivo.close()

# ---------------------------------------------- #

print('(2)')
meu_arquivo = open('extra/12_tasmania.txt', 'r', encoding='utf-8')

# como lemos o conteúdo do arquivo?
# se preferir, pode ler uma linha de cada vez
# use o método readline
conteudo_arquivo = meu_arquivo.readline()
print(conteudo_arquivo)

conteudo_arquivo = meu_arquivo.readline()
print(conteudo_arquivo)

# não esqueça de sempre fechar o arquivo
meu_arquivo.close()

# ---------------------------------------------- #

# se você estiver lendo um arquivo csv, há uma biblioteca csv que irá ajudá-lo
# para acessar os recursos na biblioteca csv você deve importá-lo
# import csv que esta no início deste arquivo

# agora você pode usar a função de leitura para retornar todas as linhas do arquivo para uma lista
# dados_arquivo = csv.reader (meu_arquivo)

# se o seu arquivo não estiver usando uma vírgula para separar os valores, você pode informar a função do leitor
# qual caractere é usado como um delimitador
# dados_arquivo = csv.reader (meu_arquivo, delimiter = ';')

# agora podemos abrir e ler um csv

print('(3)')
with open('extra/12_tasmania.txt', 'r', encoding='utf-8') as meu_arquivo:
    # leia o conteúdo do arquivo
    linhas = csv.reader(meu_arquivo, delimiter=';')

    # por que temos um "with" e "as"
    # os programas devem sempre abrir um arquivo e fechá-lo quando terminarem
    # uma vez que temos todas as linhas de um arquivo csv retornado, como acessamos as linhas individuais?
    # dados_arquivo é uma lista, então você pode fazer tudo o que vimos no capítulo sobre listas
    for linha in linhas:
        print(linha)

        # mas eu não gosto desses colchetes e citações adicionadas às linhas!
        # você pode usar a função join para formatar a saída
        # - SeparatorToDisplay.join(linha)
        print(';'.join(linha))

        # E se eu quiser acessar um valor individual de uma linha e não apenas imprimir a linha inteira?
        # a linha retornada no loop é, na verdade, uma lista das palavras nessa linha
        # então você pode apenas criar um loop aninhado para percorrer as palavras na linha
        for coluna in linha:
            print(coluna)

# seu desafio
# escreva um programa que imprima os nomes e as idades dos convidados no arquivo da lista de convidados
# que você criou no último módulo se você não fez o último desafio, basta criar um arquivo para ler usando o bloco de
# notas que contém nomes e idades

print('(challenge)')
with open('extra/11_challenge.csv', 'r', encoding='utf-8') as meu_arquivo:
    linhas = csv.reader(meu_arquivo, delimiter=';')

    for linha in linhas:
        print(';'.join(linha))

        for coluna in linha:
            print(coluna)
