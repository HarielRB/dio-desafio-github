while True:
    x = input("Insira um numero: ")
    if x.isnumeric():
        x = int(x)
        break
    else:
        print("Insira um número INTEIRO!")
#um laço para andar com o numero a ser analisado
for y in range(1, x+1):
    numeroDivisao = 0
    for z in range(1, y+1):
        resto = y % z
        if resto == 0:
            numeroDivisao += 1
    if numeroDivisao == 2:
        print(y)
    else:
        print("Nenhum número inteiro encontrado!")
