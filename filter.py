lista1 = [10, 12 , 13 , 15 , 20 , 25 , 30 , 40 , 45 , 50]

def menor20(x):
  return x > 20
    
print(list(filter(menor20,lista1)))

#maneira mais simples usando lambda:
print(list(filter(lambda x: x > 20,lista1)))