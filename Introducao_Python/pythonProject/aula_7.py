class Calculadora:
    def __init__(self, num1, num2):
        self.valorA = num1
        self.valorB = num2

    def soma(self):
        return self.valorA + self.valorB

    def subtracao(self):
        return self.valorA - self.valorB

    def divisao(self):
        return self.valorA / self.valorB

    def multiplicacao(self):
        return self.valorA * self.valorB


'''class MinhaClasse:
    def __init__(self, numero1, numero2):
        self.variavel1 = numero1
        self.variavel2 = numero2

    def aumentar(self):
        self.variavel1 += self.variavel2
        return self.variavel1
    def escrever(self):
        print(f'O valor aumentado é {self.variavel1}')'''


calculadora = Calculadora(10, 2)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multiplicacao())
'''classe = MinhaClasse(10, 3)
classe.aumentar()
classe.escrever()'''
