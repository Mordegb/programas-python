valor = int(input('informe um valor para calcular a quantidade de notas: '))

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    print(f'{quantidade} nota(s) de R$ {nota},00')


