# Exercicio 4

import json

usuarios = open('usuarios.json', 'r')
dados = json.load(usuarios)

nome = input('Insira o nome do usuário: ')
