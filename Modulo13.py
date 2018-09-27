# Modulo13.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
import datetime


# repetição
# um dos problemas com o código é que você está freqüentemente fazendo a mesma coisa uma e outra vez
# - as mesmas poucas linhas de código
# - as mesmas tarefas
# - as mesmas operações

# o que é uma função?
# - uma seção de código reutilizável com um nome que faz alguma coisa
# - às vezes chamado de método

# você já usou funções!
# - print
# - open
# - write
# - close

# por que criar funções?
# - reutilização de código: você está fazendo a mesma coisa repetidas vezes
# - simplificar: funções possuem nomes para definir o que fazem
# - simplificar: decompor blocos complexos de código
# - mais fácil de fazer alterações
# - se foi escrito uma vez, você só precisa atualizá-lo uma vez

# como criamos uma função?
# use a palavra-chave def (abreviação de define)
# dê um nome para sua função
# escreva o código no corpo da função


def print_bem_vindo():
    print('Olá mundo!')


# como você chama uma função?
# - simplesmente use seu nome
print_bem_vindo()


def print_nomes(lista):
    for nome in lista:
        print(nome)
    return


# defina esta função
# quando alguém chama esta função, execute este código
def main():
    nomes = ['Ragnar', 'Bjorn', 'Olaf']
    # sim, você pode chamar uma função dentro de outra função
    print_nomes(nomes)
    return


# execute a função
# para fazer isso a função deve ser criada
main()


# gostaria que minha função fosse dinâmica
# em nossos exemplos as funções que criamos só fizeram uma coisa
# às vezes é exatamente isso que precisamos
# mas às vezes precisamos de alguma flexibilidade
# criar mensagens personalizadas para serem exibidas
# forneça dois números para um cálculo
# imprimir na tela e, opcionalmente, em um arquivo

# e quanto aos parâmetros?
# eles não são nada mais que variáveis
# como na impressão, você está enviando uma string como parâmetro para a função print
def alerta(texto):
    print(texto)
    return


# o que dizer de vários parâmetros?
# basta adicioná-los, separados por vírgulas
def mostra_mensagem(cumprimento, nome):
    mensagem = cumprimento + ', ' + nome
    print(mensagem)
    return


mostra_mensagem('Olá', 'Marcio')


# funções retornam dados usando a palavra-chave return
# especifica o valor ou os dados que você deseja repassar após a palavra-chave return
# você pode reutilizar nomes em diferentes funções
def receber_mensagem(nome):
    mensagem = 'Olá, ' + nome
    return mensagem


def print_mensagem(mensagem):
    print(mensagem)
    return


saida = receber_mensagem('Christopher')
print_mensagem(saida)


# seu desafio
# criar uma função para simplificar a gravação em arquivos
# defina a função para aceitar parâmetros
# - um para texto
# - um para o nome de um arquivo
# adicione o código que gravará o texto no arquivo


def write_arquivo(nome_arquivo, conteudo_arquivo):
    meu_arquivo = open(nome_arquivo, 'w')
    meu_arquivo.write(conteudo_arquivo)
    meu_arquivo.close()


def append_arquivo(nome_arquivo, conteudo_arquivo):
    meu_arquivo = open(nome_arquivo, 'a')
    meu_arquivo.write(conteudo_arquivo + '\n')
    meu_arquivo.close()


arquivo = 'extra/13_challenge.txt'

write_arquivo(arquivo, 'War for territory\nWar for territory\n')

append_arquivo(arquivo, 'Years of fighting')
append_arquivo(arquivo, 'Teaching my son')
append_arquivo(arquivo, 'To believe in that man')


# desafio extra
# escreva uma função to_date () e to_char () no formato que você quer


def to_date(date):
    return datetime.datetime.strptime(date, "%d/%m/%Y").date()


def to_char(date):
    return date.strftime('%d/%m/%Y')


dat_date = to_date('31/07/2018')
print(to_char(dat_date))
