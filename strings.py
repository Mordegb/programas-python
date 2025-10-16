lista = ['maça','banana','melancia','alexandre','silvie','bia']

#deixa as primeira letras da string em maiusculo e todo os o resto minusculo
capacitaze = map(str.capitalize ,lista) 
print(list(capacitaze))

#deixa todas as strings maiusculas
Maiusculas = map(str.upper, lista)
print(list(Maiusculas)) 

#deixa as letras todas minusculas
minusculas = map(str.lower, lista)
print(list(minusculas))

#deixa a primeira letra da string em minusculo e ignora o resto.
titulo = map(str.title , lista)
print(list(titulo))

#deixa troca o sentido das ltras, oq tava maiusculo fica minusculo e vise-versa
viraVira = map(str.swapcase , lista)
print(list(viraVira))

test = 'cadu esta com fome e sono'
sla = test.split( )
print(sla)