nome = str(input("diga seu nome: "))
idade = int(input('diga sua idade: '))
dinheiro = float(input('quanto dinheiro tem na conta: '))

print(f'ola meu nome é {nome} e eu tenho {idade} anos e tenho {dinheiro:.2f} reais na conta')
# a sintaxe de {dinheiro:.2f} == %.2 dinheiro(em c)
print("\n")

for x in range(1,11,1):
    print(f'ola meu nome é {nome} e eu tenho {idade} anos e tenho {dinheiro:.2f} reais na conta')
    idade += 1
    dinheiro += 10