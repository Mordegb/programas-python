
def divid(a: int, b:int) -> int:
    resultado = a/b
    return resultado

#a seta apos a declaração de noma da função indica o tipo que a função deve retornar

'''nun_arara = int(input('informe a quantidade de araras: '))
nun_gaiolas = int(input('informe a quantidade de gaiolas: '))'''

nun_arara = 2
nun_gaiolas = 10

resp = divid(nun_gaiolas,nun_arara)
if resp < 4:
    print('N\n')
else:
    print('S\n')

