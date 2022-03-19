class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1

    def diminuiCanal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    # se o arquivo que chamar a classe for onde ela foi criado ela faz tudo isso
    # se não for ele só instancia a classe
    televisao = Tv()
    print(f'A televisão esta ligada? \n{televisao.ligada}')
    televisao.power()
    print(f'Esta ligada agora? \n{televisao.ligada}')
    print(f'Canal Atual: {televisao.canal}')
    televisao.aumentaCanal()
    televisao.aumentaCanal()
    print(f'Canal Atual: {televisao.canal}')
    televisao.diminuiCanal()
    print(f'Canal Atual: {televisao.canal}')
