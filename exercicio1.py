#Exercicio 1

frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split() # Divide as palavras e gera uma lista
juntar = ''.join(palavras) # Juntar tudo em uma string
inverso = ''

print('O inverso de {} é {}'.format(juntar, inverso))
 
for letra in range(len(juntar) - 1, -1, -1): # Pega o numero de letras de 'junto', tirar 1, vai até a letra -1 e vai voltando uma letra
    inverso += juntar[letra]

if inverso == juntar: 
    print('Palindromo!')
else:
    print('Não é')