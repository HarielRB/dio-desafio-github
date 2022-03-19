
lista = [1, 10]


try:
    arquivo = open('teste.txt', 'r')
    divisao = 10/1
    numero = lista[1]
    # x = a

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero!')

except IndexError:
    print('Erro ao acessar um index inválido da lista!')

except BaseException as ex:
    print(f'Erro Desconhecido! {ex}')

else:
    print('Tudo nos conformes!')

finally:
    print("Fechando o Arquivo")
    arquivo.close()
