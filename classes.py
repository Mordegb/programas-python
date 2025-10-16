class Pessoa: #primeira letra ao criar uma classe deve ser maiuscula
    def __init__(self, nome, idade, trabalho): #basicamente o construtor, incia a classe com valores padrão
        self.nome = nome #vc adiciona sempre o self pra atribuir os atributos dele mesmo
        self.idade = idade
        self.trabalho = trabalho

    def apresentar (self): #pode colocar so self como parametro que vc ja pode usar todos os atributos
        print(f'olá meu nome é {self.nome} e tenho {self.idade} anos. \n')



pessoa1 = Pessoa("cadu" , 16 , "estudante") #semple declarar quando criar
pessoa1.apresentar()

pessoa1.idade = 18
pessoa1.apresentar()