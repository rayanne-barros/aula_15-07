class Personagem:
    def __init__(self, nome, pontuacao, moedas, poder_especial):
        self.nome = nome
        self.idade = pontuacao
        self.moedas = moedas
        self.poder_especial = poder_especial

    def usar_poder(self):
        if (self.nome == "Mario"):
            return print(f'{self.nome}: {self.poder_especial}!')
        elif (self.nome == "Luigi"):
            return print(f"{self.nome}: {self.poder_especial}!")
        else:
            return print(f'{self.nome}: {self.poder_especial}')


personagem1 = Personagem("Mario", 20, 300, "Super Mario")
personagem1.usar_poder()
personagem2 = Personagem("Luigi", 15, 200, "Fire Luigi")
personagem2.usar_poder()
personagem3 = Personagem("Yoshi", 10, 100, "Flying Yoshi")
personagem3.usar_poder()


#### Resolução Professor ####

class Personagem:
    def __init__(self, nome, pontuacao, moedas):
        self.nome = nome
        self.idade = pontuacao
        self.moedas = moedas

    def usar_poder(self):
        if (self.nome == "Mario"):
            return "Super Mario"

        elif (self.nome == "Luigi"):
            return "Fire Luigi"

        else:
            return "Flying Yoshi"


personagem1 = Personagem("Mario", 20, 300)
print(f"Nome do Personagem: {personagem1.nome} Poder Especial: {personagem1.usar_poder()}!")
personagem2 = Personagem("Luigi", 15, 200)
print(f"Nome do Personagem: {personagem2.nome} Poder Especial: {personagem2.usar_poder()}!")
personagem3 = Personagem("Yoshi", 10, 100)
print(f"Nome do Personagem: {personagem3.nome} Poder Especial: {personagem3.usar_poder()}!")


