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

pegar_valor()







