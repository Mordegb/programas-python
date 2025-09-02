dias_semana = {

    1: "segunda feira",
    2: "terça feira",
    3: "quarta feira",
    4: "quinta feira",
    5: "sexta feira",
    6: "sabado",
    7: "domingo"
}

num = int(input('diga um numero: '))
dia = dias_semana.get(num)
try:
    print(dias_semana[num])  # Tenta acessar o dicionário, e o cochete "[]", é usado para acessar um valor no dicionario.
except KeyError:  # Se ocorrer o erro específico "KeyError" (chave não encontrada)
    print(f"tu é burro?, semana não tem dia {num} não kkkkkkk")