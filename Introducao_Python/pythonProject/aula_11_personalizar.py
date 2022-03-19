class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input("Insira uma nota de 0 a 10: "))

        if x > 10:
            # forçando exceção
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        print(x)
        break
    except ValueError:
        print("Valor inválido, insira apenas números!")
    except InputError as ex:
        print(ex)
