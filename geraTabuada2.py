import cadu
from colorama import init, Fore, Back, Style

def imprimir_tabela(inic:int,valor:float,intervalo:int,salto:int):
    for x in range(inic,intervalo + 1,salto):
        print(f'{valor:.0f} x {x} = {valor * x:.0f}')

def pegar_valor(valor:float):
    intervalo = int(input('será multiplicado até: '))# vai ate
    salto = int(input('dica o salto pra tabuada: '))
    inic = int(input('numero de inicio dos intervalos: '))
    cadu.limpar_tela()
    print('\n')
    imprimir_tabela(inic,valor,intervalo,salto)

def mostrar_infos(num:int):
    print('\n')
    print(Fore.WHITE + f'QUADRADO: {num ** 2:.2f}')
    print(Fore.WHITE + f'RAIZ: {num ** 0.5:.2f}')
    print(Fore.WHITE + f'CUBO: {num ** 3:.2f}')

def main():
    cadu.limpar_tela()
    cadu.mostrar_cabecalho('Gerador de tabuada')
    valor = float(input('numero para gerar a tabuada: '))
    pegar_valor(valor)
    mostrar_infos(valor)

   
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")




