#pode usar ela junto com o map e varias outras funções
'''
lista1 = [1 , 2 , 4 ,8]
lista2 = map(lambda x: x * 2,lista1)
print(list(lista2))
'''
#o lambda cria funções para serem usadas de forma simples e podem ser postas em qualquer lugar

teste1 = lambda x: x ** 2
print(teste1(4))

#vc pode tambem dar as opções doque dizer em certos casos
# Aplicar função condicional
numeros = [1, 2, 3, 4, 5, 6]
resultado = map(lambda x: 'par' if x % 2 == 0 else 'ímpar', numeros)
print(list(resultado))  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar', 'par']
