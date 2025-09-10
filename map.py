
'''
o comando map funciona geralmente atribuindo a varias variaveis um uma lista,assim como o filter
voce pode usar o lambda dentro dele,e funções,pode ser usado para conversao de tipos em uma lista,
e modificar coisas como letrras maiuscula e minuscula dentro delas tambem,
obs: ele não retorna uma lista ent deve ser usado em conjunto com o comando list().
'''

# Elevar ao quadrado cada número
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x**2, numeros)
print(list(quadrados))  # [1, 4, 9, 16, 25]

def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
resultado = map(dobrar, numeros)
print(list(resultado))  # [2, 4, 6, 8, 10]



# Somar elementos de duas listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
soma = map(lambda x, y: x + y, lista1, lista2)
print(list(soma))  # [5, 7, 9]




# Converter para float
numeros_str = ['3.14', '2.71', '1.61']
numeros_float = map(float, numeros_str)
print(list(numeros_float))  # [3.14, 2.71, 1.61]



# Capitalizar palavras
palavras = ['python', 'map', 'function']
maiusculas = map(str.capitalize, palavras)
print(list(maiusculas))  # ['Python', 'Map', 'Function']

# Converter para minúsculas
nomes = ['João', 'MARIA', 'Pedro']
minusculas = map(str.lower, nomes)
print(list(minusculas))  # ['joão', 'maria', 'pedro']



