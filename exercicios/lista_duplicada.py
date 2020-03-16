lista = ['a', 'b', 'c', 'a', 'b']


def nao_repetir_set(entrada):
	entrada = set(entrada)
	return sorted(entrada)

def nao_repetir(entrada):
	lista_copia = []
	for num in range(len(entrada)):
		if entrada[num] not in lista_copia:
			lista_copia.append(entrada[num])
	return sorted(lista_copia)

print(nao_repetir_set(lista), 'set')
print(nao_repetir(lista), 'sem set')