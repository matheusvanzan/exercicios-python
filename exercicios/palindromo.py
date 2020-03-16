entrada = str(input('frase: ')).strip()# entrada da frase
palavra = entrada.split() # tirar os espacos
palavra_junta = ''.join(palavra) # juntar as palavras
palavra_inversa = '' # varivavel vazia para as palavras poderem ficar inversas

# loop para que o for ande de tras para frente voltando uma letra
for letra in range(len(palavra_junta) -1, -1, -1): 
	palavra_inversa += palavra_junta[letra] # inverte a palavra

print(palavra_inversa)
print(palavra_junta)

# compara se as frases sao iguais
if palavra_inversa == palavra_junta:
	print('Essa frase é um palíndromo')
else:
	print('Essa frase não é um palíndromo')
