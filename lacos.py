# a variavel do for dentro de uma lista assume cada valor dela, se fro diretor''
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Iterando com range()
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Número: {i}")

for i in range(1,10,1): #começa em 1, vai ate menor que 10, e pule de 1 em 1.
    print(i)


contador = 0
while contador < 5: #while com uma condição
    print(f"Contador: {contador}")
    contador += 1

contador = 0
while True: # basicamente um do-while, ele sempre é executado, e so para quando tiver um if dentro.
    print(f"Contador: {contador}")
    if contador == 25:
        break
    