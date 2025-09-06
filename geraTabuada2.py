import cadu

def imprimir_tabela(inic:int,valor:float,intervalo:int,salto:int):
    for x in range(inic,intervalo + 1,salto):
        print(f'{valor:.0f} x {x} = {valor * x:.0f}')

def pegar_valor():
    cadu.limpar_tela()
    valor = float(input('numero para gerar a tabuada: '))
    intervalo = int(input('intervalo dos multiplos: '))# vai ate
    inic = int(input('numero de inicio dos intervalos: '))
    salto = int(input(' dica o salto pda tabuada: '))
    cadu.limpar_tela()
    imprimir_tabela(inic,valor,intervalo,salto)

def mostrar_infos(num:int)
    print(f'QUADRADO: {num **2 :.2f}')
    print(f'RAIZ: {num ** 0,5 :.2f}')
    print(f'QUADRADO: {num **2 :.2f}')
    print(f'QUADRADO: {num **2 :.2f}')
    print(f'QUADRADO: {num **2 :.2f}')

pegar_valor()







