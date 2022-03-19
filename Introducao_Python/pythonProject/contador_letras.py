def contadorLetras(listaLetras):
    contador = []
    for x in listaLetras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador


if __name__ == '__main__':
    lista = ['Cachorro', 'Gato']
    print(contadorLetras(lista))
