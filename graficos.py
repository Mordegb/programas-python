import matplotlib.pyplot as ptl #importar a biblioteca de graficos matematicos

#cria listas com os dados nescessarios
cidades = ['fortaleza' , 'salvador' , 'bahia' , 'teresina']
temperaturaMedia = [30.4 , 27.3 , 30 , 40]

#criar grafico de barras:
ptl.bar(cidades , temperaturaMedia)
ptl.ylabel('temperatura media (C)')
ptl.show()

#criar grafco de linhas
ptl.plot(cidades , temperaturaMedia)
ptl.grid() #coloca linha nas grades
ptl.show()
