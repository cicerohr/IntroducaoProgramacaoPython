# Modulo11.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
# você já precisou anotar algo para lembrar depois?
# uma lista de ingredientes para comprar uma receita?
# uma lista de convidados?
# um número de telefone?

# às vezes até os programas precisam anotar algo para que possam lembrar mais tarde
# lembrar qual página eu estava lendo meu e-book
# lembre-se de que tesouros eu colecionei quando fiz uma pausa do jogo

# trabalhando com arquivos
# uma das maneiras que um programa pode fazer uma anotação de algo para escrevê-lo em um arquivo

# como você escreve no arquivo com código?
# use a função open para criar e abrir um arquivo
# my_file = open(file_name, access_mode)
# você deve especificar
# - file_name
# - access_mode

# qual é o nome do arquivo?
# o nome do arquivo é o nome do seu arquivo, incluindo a extensão (data.txt, my_times.csv)
# o arquivo será criado na mesma pasta que seu programa

# qual é o modo de acesso?
# o modo de acesso especifica o que você fará com o arquivo depois de abri-lo
# você pode especificar qualquer um dos seguintes itens:# - r: read the file
# - b: abre um arquivo binário
# - w: escreve no arquivo
# - a: anexar ao conteúdo do arquivo existente
# - w+: lê e escreve ao mesmo tempo
WRITE = 'w'
file = open('extra/11_guest_list.txt', mode=WRITE, encoding='utf-8')

# se o arquivo não existir, python irá criá-lo
# write sempre sobrescreverá o arquivo
# append adicionará o conteúdo no final do arquivo

# agora que temos um arquivo, como escrevemos nele?
# use a função write
file.write('Olá!')
file.write('Como vai?')
# como você pode ver, escreveu tudo na mesma linha

# se você quiser imprimir na próxima linha, pense em declarações de impressão
# lembre-se \ n?
file.write("\nOlá!")
file.write("\nComo vai?")

print('--------------------------')

file_name = 'extra/11_demo.csv'
APPEND = 'a'

file = open(file_name, mode=APPEND)

file.write('Nome;Idade;\n')
file.write('Susan;29;\n')
file.write('Christopher;31;\n')

print('--------------------------')

file_name = 'extra/11_user_file.txt'
WRITE = 'w'

data = input('Por favor, insira as informações do arquivo: ')
file = open(file_name, mode=WRITE, encoding='utf-8')
file.write(data)

print('Arquivos escritos com sucesso')

# seu desafio
# crie o arquivo csv abaixo!

file = open('extra/11_challenge.csv', 'w', encoding='utf-8')

emp_name = ' '
emp_age = '0'
while emp_name != '':
    emp_name = input('Por favor, insira o nome do empregado: ')
    emp_age = input('Por favor insira a idade do empregado: ')
    file.write(emp_name + ';' + emp_age + ';' + '\n')

print('Arquivos escritos com sucesso')

# quando você terminar, você deve sempre fechar o arquivo
# use o método close
file.close()
