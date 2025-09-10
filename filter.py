
'''
o comando filter le uma lista e remove dela oq voçe denominar como filtro,geralmente se uma uma função
como a que é mostrada a seguir, mas o mais commum  e realmente simples é usando o lambda.
obs: ele não retorna uma lista ent deve ser usado em conjunto com o comando list().
'''

lista1 = [10, 12 , 13 , 15 , 20 , 25 , 30 , 40 , 45 , 50]

def menor20(x):
  return x > 20
    
print(list(filter(menor20,lista1)))

#maneira mais simples usando lambda:
print(list(filter(lambda x: x > 20,lista1))) #[25 , 30 , 40, 45, 50]



palavras = ["python", "java", "c", "javascript", "go", "rust"]

# Filtrar palavras com mais de 3 letras
longas = list(filter(lambda p: len(p) > 3, palavras))
print(longas)  # ['python', 'java', 'javascript']