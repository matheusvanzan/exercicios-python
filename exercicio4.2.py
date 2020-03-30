# Exercicio 4

import json
from datetime import datetime, date

def read():
    with open('usuarios.json', 'r', encoding='utf8') as f:
        return json.load(f)

def calc_idade(idadeUsuario):
    ano = int(usuario["data_nasc"][6:])
    mes = usuario["data_nasc"][3:5]
    dia = int(usuario["data_nasc"][:2])

    if '0' in mes:
        mes = mes.replace('0', '')

    mes = int(mes)

    dtNasc = datetime(ano, mes, dia)
    idade = datetime.utcnow() - dtNasc
    idadeEmAnos = int(idade.days / 365)

    return idadeEmAnos

data = read()

nome = input('Escreva seu nome: ')


for usuario in data["usuarios"]:
    if usuario['nome'] == nome:
        print('Nome: ', usuario['nome'])
        idadeUsuario = usuario['data_nasc']
        idade = calc_idade(idadeUsuario)
        print("Idade: ", idade)
        print('Grupos: ', '\n         '.join(usuario['grupos']))
        print('E-mail: ', usuario['email'])