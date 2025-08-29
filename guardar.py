import os
a,b,c = map(float, input('informe os valores das variveis "A" , "B" , "C ": \n').split())

#o comando map(tipo de variavel, input),defini todos os tipos de um vetor como o tipo escolhido dentro.

#o comando .split() dividi partes de uma strig separada por espaço(ou por oque tiver dentro dos parenteses)

'''
exemplo: ola mundo linux
[0] = ola
[1] = mundo
[2] = linux

texto = "Python é incrível"
resultado = texto.split()
print(resultado)  # Output: ['Python', 'é', 'incrível']
'''

PI =  3.14159

tringulo_retangulo = (a * c)/2
circulo = (c **2) * PI
trapezio = ((a + b) * c)/2
quadrado = b **2
retangulo = a * b


os.system('cls' if os.name == 'nt' else 'clear')
print('\n')
print(f'TRIANGULO: {tringulo_retangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
print('\n')