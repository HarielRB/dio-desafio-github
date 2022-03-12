# Condições simples
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

if a > b:
    print(f"{a} é maior que {b}")

print("Fim da condição simples!")

# Condições composta
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

if a > b:
    print(f"{a} é maior que {b}")
else:
    print(f'{b} é maior que {a}')

# Condições Aninhada
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))
c = int(input("Insira o terceiro valor: "))

if a > b and a > c:
    print(f"{a} é maior que {b} e {c}")

elif b > a and b > c:
    print(f"{b} é maior que {a} e {c}")
else:
    print(f'{c} é maior que {a} e {b}')

# Verificando se o valor é par
num1 = int(input('Insira um número: '))
if num1 % 2 == 0:
    print(f'O numero {num1} é par')
else:
    print(f'O número {num1} é impar')
