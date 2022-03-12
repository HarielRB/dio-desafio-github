a = float(input('Insira a nota do primeiro bimestre: '))
if a < 0 or a > 10:
    a = float(input('Você inseriu um valor errado! \n '
                    'Insira a nota do primeiro bimestre: '))
b = float(input('Insira a nota do segundo bimestre: '))
if b < 0 or b > 10:
    b = float(input('Você inseriu um valor errado! \n '
                    'Insira a nota do segundo bimestre: '))
c = float(input('Insira a nota do terceiro bimestre: '))
if c < 0 or c > 10:
    c = float(input('Você inseriu um valor errado! \n '
                    'Insira a nota do terceiro bimestre: '))
d = float(input('Insira a nota do quarto bimestre: '))
if d < 0 or d > 10:
    d = float(input('Você inseriu um valor errado! \n '
                    'Insira a nota do quarto bimestre: '))

media = (a + b + c + d) / 4

if media >= 7:
    print('O aluno foi aprovado!')
elif 5 < media <= 6:
    print('O aluno esta em recuperação!')
else:
    print('O aluno foi reprovado!')
