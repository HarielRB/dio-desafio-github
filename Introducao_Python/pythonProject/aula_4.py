# laço de repetição
print("-=" * 30)
print("Laço com For")
for x in range(10):
    print(x)

for y in range(1, 11):
    print(y)

a = 0

print("-=" * 30)
print("Laço com while!")
while a < 10:
    print(a)
    a += 1

print('-=' * 30)
print("Validação com While")
print('-=' * 30)
nota = int(input('Insira um número: '))
b = 10
while nota != b:
    print("Errou!")
    nota = int(input("Insira um numero novamente: "))

print("Parabéns, você acertou o número")