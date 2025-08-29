import os
from colorama import init, Fore, Back, Style

def limpar_tela():  #limpa o terminal antes de mostrar algo novo
    os.system('cls' if os.name == 'nt' else 'clear') #o comando os.system executa um comando no terminal

def triangulo():
    
    base = float(input('Base do triangulo: '))
    altura = float(input('Altura do triangulo: '))
    area = (base * altura)/2       
    print(f'Area do triangulo = {area:.2f}')

def retangulo():
    base = float(input('Base do retangulo: '))
    altura = float(input('Altura do retangulo: '))
    area = (base * altura)
    print(f'Area do retangulo = {area:.2f}')

def trapezio():
    base1= float(input('Base maior do trapezio: '))
    base2 = float(input('Base menor do trapezio: '))
    altura = float(input('Altura do trapezio: '))
    area = ((base1 + base2) * altura) / 2
    print(f'Area do trapezio = {area:.2f}')

def circulo():
    PI =  3.14159
    raio = float(input('Informe o raio do circulo: '))
    area = (raio ** 2) * PI
    print(f'Area do circulo = {area:.2f}')

def quadrado():
   lado = float(input('Informe o lado do quandrado: '))
   area = lado **2
   print(f'Area do quadrado = {area:.2f}')




print(Fore.LIGHTGREEN_EX + "="*40)
print(Fore.LIGHTCYAN_EX+ "bem vindo ao calculador de area".center(40))
print(Fore.LIGHTGREEN_EX + "="*40)
print('\n')
opt = str(input(Fore.WHITE + 'deseja calcular a area de qual forma geometrica?:\n')).lower().strip()
print('\n')


match opt:

    case 'triangulo':
      limpar_tela()
      triangulo()


    case 'retangulo':
      limpar_tela()
      retangulo()
      
    case 'trapezio':
      limpar_tela()
      trapezio()  

    case 'circulo':
      limpar_tela()
      circulo()

    case 'quadrado':
      limpar_tela()
      quadrado()
      

