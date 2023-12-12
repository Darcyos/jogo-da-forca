import random

frutas = ['uva', 'pera', 'banana']
carros = ['uno', 'compass', 'mobi']


categoria = [frutas, carros]
resultado = random.choice(categoria)
dica = ""
if resultado[0] == frutas[0]:
    dica = "frutas"
else:
    dica = "carros"


Nresultado = ""
if dica == 'frutas':
    Nresultado = random.choice(frutas)
else:
    Nresultado = random.choice(carros)




while True:
    print(f'a dica é: {dica}')
    resposta=input('Digite um nome: ')
    if resposta == Nresultado:
        break
    else:
        print("tente novamente...")

print('parabens você acertou!')