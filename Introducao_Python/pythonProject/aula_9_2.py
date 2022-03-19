import shutil

def escrever_arquivo(texto):

    arquivo = open('teste.txt', 'w')
    # escrever algo no arquivo
    arquivo.write(texto)
    # o write sempre realiza uma nova escrita, então ele apaga a antiga e cria uma nova
    # fechar o arquivo após escrita
    arquivo.close()

    # para atualizarmos um arquivo utiliza-se o A


def atualizar_arquivo(nome_arquivo, aluno):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(aluno)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    # metodo que abre o arquivo desejado
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([float(i) for i in notas]) / 4
        print(aluno)
        print(lista_notas)
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, 'C:/Users/balto/Downloads/notasAlunos.txt')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/balto/Downloads')


if __name__ == '__main__':
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira Linha. \n')
    #aluno = '\n Paulo Tejando, 2, 1, 7.5, 2'
    #atualizar_arquivo('notas.txt', aluno)
    # copia_arquivo('notas.txt')
    media_notas('notas.txt')

