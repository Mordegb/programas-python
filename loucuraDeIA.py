import math
from time import sleep
import os
from colorama import init, Fore, Back, Style

# Inicializa colorama para cores no terminal
init(autoreset=True)

def limpar_tela():
    """Limpa a tela do terminal de forma cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho estilizado do programa"""
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + "GERADOR AVANÇADO DE TABUADA".center(50))
    print(Fore.YELLOW + "=" * 50)
    print()

def validar_numero(entrada):
    """Valida se a entrada é um número válido"""
    try:
        num = float(entrada)
        return num
    except ValueError:
        return None

def obter_numero_usuario():
    """Obtém e valida o número do usuário"""
    while True:
        numero = input(Fore.GREEN + "Digite um número para gerar a tabuada (ou 'sair' para encerrar): " + Style.RESET_ALL)
        
        if numero.lower() == 'sair':
            return None
        
        num_validado = validar_numero(numero)
        
        if num_validado is not None:
            return num_validado
        else:
            print(Fore.RED + "Entrada inválida! Por favor, digite um número válido.")
            sleep(1)

def obter_configuracoes():
    """Obtém as configurações adicionais para a tabuada"""
    print(Fore.BLUE + "\nConfigurações da Tabuada:")
    
    while True:
        try:
            inicio = int(input("Início do intervalo (padrão: 1): ") or 1)
            fim = int(input("Fim do intervalo (padrão: 10): ") or 10)
            passo = int(input("Passo (padrão: 1): ") or 1)
            
            if passo == 0:
                print(Fore.RED + "O passo não pode ser zero!")
                continue
                
            if (fim - inicio) * passo <= 0:
                print(Fore.RED + "Intervalo inválido para o passo informado!")
                continue
                
            return inicio, fim, passo
        except ValueError:
            print(Fore.RED + "Por favor, digite valores inteiros válidos.")

def gerar_tabuada(numero, inicio, fim, passo):
    """Gera e exibe a tabuada formatada"""
    print(Fore.MAGENTA + f"\nTabuada do {numero} (de {inicio} a {fim} com passo {passo}):")
    print(Fore.YELLOW + "-" * 40)
    
    for i in range(inicio, fim + 1 if passo > 0 else fim - 1, passo):
        resultado = numero * i
        # Formatação especial para números inteiros vs decimais
        if isinstance(numero, int) and isinstance(i, int):
            print(Fore.CYAN + f"{numero:>5} {Fore.WHITE}x {i:>3} {Fore.WHITE}= {Fore.GREEN}{resultado:>8}")
        else:
            print(Fore.CYAN + f"{numero:>7.2f} {Fore.WHITE}x {i:>5} {Fore.WHITE}= {Fore.GREEN}{resultado:>10.2f}")
    
    print(Fore.YELLOW + "-" * 40)

def exibir_info_adicional(numero):
    """Exibe informações matemáticas adicionais sobre o número"""
    print(Fore.BLUE + "\nInformações Adicionais:")
    print(Fore.WHITE + f"- Raiz quadrada: {math.sqrt(numero):.2f}")
    print(f"- Quadrado: {numero**2:.2f}")
    print(f"- Cubo: {numero**3:.2f}")
    
    if numero != 0:
        print(f"- Inverso (1/x): {1/numero:.4f}")
    
    print(f"- Paridade: {'Par' if numero % 2 == 0 else 'Ímpar'}" if isinstance(numero, int) else "- Paridade: Apenas para inteiros")

def main():
    """Função principal do programa"""
    limpar_tela()
    exibir_cabecalho()
    
    while True:
        numero = obter_numero_usuario()
        
        if numero is None:
            print(Fore.YELLOW + "\nEncerrando o programa...")
            sleep(1)
            break
            
        limpar_tela()
        exibir_cabecalho()
        
        inicio, fim, passo = obter_configuracoes()
        
        limpar_tela()
        exibir_cabecalho()
        
        gerar_tabuada(numero, inicio, fim, passo)
        exibir_info_adicional(numero)
        
        input(Fore.WHITE + "\nPressione Enter para gerar outra tabuada...")
        limpar_tela()
        exibir_cabecalho()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nPrograma interrompido pelo usuário.")
    finally:
        print(Style.RESET_ALL)