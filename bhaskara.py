a,b,c = map(float,input().split())
if a <= 0 or b <= 0 or c <= 0:
    print('Impossivel calcular')

else:
    delta = (b ** 2) - (4 * a * c)
    if not delta > 0:
        print('Impossivel calcular')

    else: 
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)

        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')
