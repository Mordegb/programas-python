import matplotlib.pyplot as ptl #importar a biblioteca de graficos matematicos

#cria listas com os dados nescessarios
cidades = ['fortaleza' , 'salvador' , 'bahia' , 'teresina']
temperaturaMedia = [30.4 , 27.3 , 30 , 40]

#criar grafico de barras:
ptl.bar(cidades , temperaturaMedia ,color=['yellow' ,'blue','green','red'])
ptl.ylabel('temperatura media (C)')
ptl.show() #o comando ptl.show mostra seu grafico

#criar grafco de linhas
ptl.plot(cidades , temperaturaMedia)
ptl.grid() #coloca linha nas grades
ptl.show()


#grafico em pizza
ptl.pie(temperaturaMedia,labels = cidades , autopct = '%1.1f%%', colors=['#3425ff' ,"#195a09ee","#840ea4","#b00b0b"])
#o grafico em pizza recebe como parametros primeiro os valores numericos, e dps os nomes
ptl.show()


# Dados
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]  # x²
y2 = [1, 2, 3, 4, 5]    # x
y3 = [1, 8, 27, 64, 125] # x³

ptl.plot(x, y1, label='x²', marker='o')
ptl.plot(x, y2, label='x', marker='s')
ptl.plot(x, y3, label='x³', marker='^')

ptl.title("Múltiplas Linhas")
ptl.xlabel("X")
ptl.ylabel("Y")
ptl.legend()  # Mostra a legenda
ptl.grid(True)
ptl.show()




# Dados de temperatura durante a semana
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
temperaturas = [22, 24, 19, 25, 27, 30, 28]

ptl.figure(figsize=(10, 6))
ptl.plot(dias, temperaturas, 'o-', linewidth=2, markersize=8)
ptl.title("Temperatura Durante a Semana")
ptl.ylabel("Temperatura (°C)")
ptl.ylim(16, 35)
ptl.grid(True)

# Adicionar valores nos pontos
for i, temp in enumerate(temperaturas):
    ptl.annotate(f'{temp}°C', (dias[i], temperaturas[i]), 
                textcoords="offset points", xytext=(0,10), ha='center')

ptl.show()