'''
tratatamento de exeções bem parecido com java... tudin copiando c é facil né
'''
while True:
    try: #vai executar um bloco de codigo que pode ter algum erro
        num = int(input('insira um numero\n'))
        print(f'numero x 2 = {num * 2}')
        break #é pq deu bom e pode sair do loop

    except ValueError: # da erro de o usuario não digitar um numero
        print('por favor, insira um numero\n')

  
while True:
    try:
        lista = ['leticia' , 'daniel' , 'cadu']
        nun2 = int(input('indice da lista para imprimir: '))
        print(lista[nun2])
        break
    except (IndexError,ValueError): #botar entre parenteses, permite ele analisar mais de um erro
        print("tem que ser um numero, e um indice da lista\n");