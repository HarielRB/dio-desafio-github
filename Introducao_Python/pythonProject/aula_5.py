# Declarando listas
listaInteiros = [1, 2, 3, 4]
listaAnimais = ['Cachorro', 'Gato', 'Calopsita', 'Jabuti']

print("Printando a lista de inteiros!")
print(listaInteiros)

print("printando os indices e elementos da lista de animais:")
for x in range(0, len(listaAnimais)):
    print(f'{x} -> {listaAnimais[x]}')

if 'gato' in listaAnimais:
    print("Sim!")
else:
    print("Não existe!")
    # incluir o valor
    listaAnimais.append('Lobo')
print(listaAnimais)

# Tuplas

tupla = (1, 12, 10, 14)
print(tupla)

# transformando uma lista em tupla
tuplaAnimal = tuple(listaAnimais)