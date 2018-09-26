# Modulo05.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
# Se eu quiser saber quantos dias até meu aniversário, primeiro eu preciso saber a data de hoje
# a classe datetime nos permite obter a data e hora atuais
# a declaração de importação nos dá acesso à funcionalidade da classe datetime
import datetime

# armazenar o valor em uma variável chamada hoje
hoje = datetime.date.today()
print(hoje)
print(hoje.year)
print(hoje.month)
print(hoje.day)
print(f'{hoje.year:04d}')
print(f'{hoje.month:02d}')
print(f'{hoje.day:02d}')

# em python usamos strftime para formatar datas
atual = datetime.date.today()
# strftime permite que você especifique o formato da data
print(atual.strftime('%d/%m/%Y'))

# aqui está mais alguns oy pode achar útil
# %b nome do mês abreviado
# %B nome do mês
# %y ano com dois dígitos
# %Y ano com quatro dígitos
# %a dia da semana abreviado
# %A dia da semana
# %W número da semana do ano
# para uma lista completa, verifique strftime.org
print(atual.strftime('%d %b, %y'))
print(atual.strftime('%d %B %Y'))

# você poderia imprimir um convite de casamento?
# por favor, participe do nosso evento no domingo, 20 de julho no ano de 1997
print(atual.strftime('Por favor, participe do nosso evento na %A, %B %d de %Y'))

# localização em python: http://babel.pocoo.org/

# para calcular os dias até o seu aniversário
# eu preciso perguntar a data do seu aniversário
aniversario = input('Quando é seu aniversário? (dd/mm/aaaa) ')
print(f'Seu aniversário é {aniversario}')

# a função strptime permite converter uma string em uma data
aniversario = datetime.datetime.strptime(aniversario, '%d/%m/%Y').date()

# por que listamos datetime duas vezes?
# porque estamos chamando a função strptime
# que faz parte da classe datetime
# que está no módulo datetime
print(f'O mês do seu aniversário é {aniversario.strftime("%B")}')

# e se o usuário preencher uma data em um formato diferente?
# o programa irá falhar
# você pode dizer ao usuário o formato que você está esperando
# e você pode tentar lidar com o erro, caso isso ocorra
# datas parecem ter um monte de problemas, vale a pena?
# por que não apenas armazená-los como strings?
# você pode criar uma contagem regressiva para dizer quantos dias até um grande evento ou feriado

proximo_aniversario = datetime.datetime.strptime('03/06/2019', '%d/%m/%Y').date()
data_atual = datetime.date.today()

# se subtrair duas datas, recebe de volta o número de dias entre essas datas
diferenca = proximo_aniversario - data_atual
print(diferenca.days)

# há o módulo python-dateutil
# você pode usar isso
# há muitas funções interessantes
# e que horas?
# este módulo é chamado datetime, então sim, ele pode armazenar vezes
hora_atual = datetime.datetime.now()
print(hora_atual.hour)
print(hora_atual.minute)
print(hora_atual.second)
# apenas como datas, você pode usar strftime () para formatar a maneira como uma hora é exibida
print(hora_atual.strftime('%H:%M %p'))
# %H horas (24h)
# %l horas (12h)
# %p AM ou PM
# %m minutos
# %S segundos

# Desafio
# pedir a um usuário que insira o prazo do projeto
# diga quantos dias eles têm para completar o projeto
# para crédito extra, dê a resposta como combinação de semanas e dias
# dica: você precisará de algumas das funções matemáticas do módulo em valores numéricos

prazo = input('Qual é o prazo para este projeto? ')
try:
    d_prazo = datetime.datetime.strptime(prazo, "%d/%m/%Y")
    d_hoje = datetime.datetime.today()
    print(f'Hoje é {d_hoje.strftime("%d/%m/%Y")} e você quer este projeto para {d_prazo.strftime("%d/%m/%Y")}')
    n_dias_entre = d_prazo - d_hoje
    print(f'Estamos falando {n_dias_entre.days:d} dias para entregar o projeto.')
    n_semanas_entre = int(n_dias_entre.days / 7)
    n_dias_entre = n_dias_entre.days - (n_semanas_entre * 7)
    print(f'Ou melhor ainda, {n_semanas_entre} semanas e {n_dias_entre} dias.')
except Exception as e:
    print('Desculpe, mas essa não é uma data válida.')
