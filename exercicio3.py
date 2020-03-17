# Exercicio 3

def deleta_repetidos(lista):
    lista_funcao = []
    for x in lista: # Percorre a lista
        if x not in lista_funcao:   # Se a variavel do for não está na "lista_funcao"
            lista_funcao.append(x) # Adicionar
    return lista_funcao # Retona lista_funcao

lista = ['car', 'bike', 'airplane', 'motorcycle', 'truck', 'airplane', 'bike', 'motorcycle']

print(deleta_repetidos(lista))

# Usando a funcão "set()"

lista = ['car', 'bike', 'airplane', 'motorcycle', 'truck', 'airplane', 'bike', 'motorcycle']

print(sorted(set(lista)))  # sorted() retorna uma lista de objetos interaveis, set() é uma colecão de itens desordenados que cada elemento é único, não pode ser duplicado

