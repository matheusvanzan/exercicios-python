# Exercicio 4

import json

def read():
    with open('usuarios.json', 'r', encoding='utf8') as f:
        return json.load(f)

data = read()

nome = input('Escreva seu nome: ')

if nome == 'Matheus':
    print("Nome: ", data.get("usuarios")[0].get("nome"))
    print("Idade: ", data.get("usuarios")[0].get("data_nasc"))
    grupos = data.get("usuarios")[0].get("grupos")[0:]
    print("Grupos: ", ", ".join(grupos))
    print("E-mail: ", data.get("usuarios")[0].get("email"))

elif nome == 'Vinicius':
    print("Nome: ", data.get("usuarios")[1].get("nome"))
    print("Idade: ", data.get("usuarios")[1].get("data_nasc"))
    grupos = data.get("usuarios")[1].get("grupos")[0:]
    print("Grupos: ", ", ".join(grupos))
    print("E-mail: ", data.get("usuarios")[1].get("email"))

elif nome == 'Lucas':
    print("Nome: ", data.get("usuarios")[2].get("nome"))
    print("Idade: ", data.get("usuarios")[2].get("data_nasc"))
    grupos = data.get("usuarios")[2].get("grupos")[0:]
    print("Grupos: ", ", ".join(grupos))
    print("E-mail: ", data.get("usuarios")[2].get("email"))

else:
    print("Nome Incorreto")