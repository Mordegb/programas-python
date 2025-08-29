#importados ////////////////////////////////
import math
from time import sleep
import os
from colorama import init, Fore, Back, Style


#constantes ////////////////////////////////
PI = 3.141596

#funções ///////////////////////////////////
def limpar_tela():  #limpa o terminal antes de mostrar algo novo
    os.system('cls' if os.name == 'nt' else 'clear') #o comando os.system executa um comando no terminal

def exibir_cabecalho():
    # escolha a mensagem e a cor dependendo do uso
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + "GERADOR AVANÇADO DE TABUADA".center(50))
    print(Fore.YELLOW + "=" * 50)
    print()









