class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos')

pessoa1 = Pessoa("Rayanne", 28)
pessoa1.saudacao()