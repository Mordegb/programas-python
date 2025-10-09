'''
tratatamento de exeções bem parecido com java... tudin copiando c é facil né
'''
while True:
    try: #vai executar um bloco de codigo que pode ter algum erro
        num = int(input('insira um numero\n'))
        print(f'numero x 2 = {num * 2}')
        break

    except ValueError: # da erro de o usuario não digitar um numero
        print('por favor, insira um numero\n')

  
