# Modulo02.py criado por Cicero em 2018-09-26. Projeto IntroducaoProgramacaoPython.
# 
print('Hello World')
print('Aqui tem aspas duplas "' + " e aqui tem aspas simples '")
print("ou você pode fazer \" para funcionar")

mensagem = 'olá mundo!'
# mostra o índice onde começa a sequencia de caracteres
# o l á   m u n d o !
# 0 1 2 3 4 5 6 7 8 9
print(mensagem.find('mundo'))
# conta quantas vezes encontrou o caracter
print(mensagem.count('o'))
# Inicia a primeira palavra com maiúscula
print(mensagem.capitalize())
# Troca uma sequencia de caracter por outra
print(mensagem.replace('olá', 'oi'))
