tam = int(input('informe o tamanho do veto: '))
vetor = [] #cria o vetor com tamenho dinamico (so da assim...)

for i in range(tam):
    num = int(input(f'vetor[{i}]: '))
    vetor.append(num) # comando "append" adiciona um numero ao final do vetor

maior = vetor[0]
menor= vetor[0]

for i in range(tam):
    if vetor[i] > maior:
        maior = vetor[i]
    
    if vetor[i] < menor:
        menor = vetor[i]

print('\n')
print(f'o maior numero do vetor é: {maior}')
print(f'o menor numero do vetor é: {menor}\n')

