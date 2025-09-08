vetor = list(map(float,input().split()))
maior = vetor[0]
menor= vetor[0]
#   for n in sorted(nums) , o comando sorted ordena em ordem crecente automaticamente    ///////////
for i in range(len(vetor)): 
    #o comando len() retorna a quantidade de elementos de um vetor (ou lista como chaman no python)

    if vetor[i] > maior:
        maior = vetor[i]

    if vetor[i] < menor:
        menor = vetor[i]
    

print(f'Maior numero do array: {maior:.2f}')
print(f'Menor numero do array: {menor:.2f}')

