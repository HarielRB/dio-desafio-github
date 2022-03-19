def escrever_arquivo(texto):

    arquivo = open('teste.txt', 'w')
    # escrever algo no arquivo
    arquivo.write(texto)
    # o write sempre realiza uma nova escrita, então ele apaga a antiga e cria uma nova
    # fechar o arquivo após escrita
    arquivo.close()

    # para atualizarmos um arquivo utiliza-se o A


def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    # metodo que abre o arquivo desejado
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    # escrever_arquivo('Primeira Linha. \n')
    # atualizar_arquivo('Segunda Linha: utilizando o método atualiar_arquivo. \n')
    ler_arquivo('teste.txt')
