X,Y = map(int,input().split())
i = 1
while True:
    mult =  X * i
    if mult == Y:
       print('é multiplo')
       break
    
    if mult > Y:
       print('não é multiplo')
       break
    
    i += 1

