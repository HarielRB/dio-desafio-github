# from módulo import classe
# import módulos

# essas são as duas maneiras de realizar a importação de módulos e classes
# de bibliotecas do python
# o from importa uma classe específica e o import importa tudo

from aula_7_2 import Tv
from contador_letras import contadorLetras

televisao = Tv()

print(televisao.ligada)
televisao.power()
print(televisao.ligada)

lista = ['Hariel', 'Harianne', 'José', 'Rizeti', 'Matheus']
print(contadorLetras(lista))
