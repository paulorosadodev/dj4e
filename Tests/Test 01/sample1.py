class Player:
    def __init__(self, nome, classe, xp):
        self.name = nome
        self.classe = classe
        self.xp = xp
        self.xpMax = self.calcular_xp_maximo()

    def calcular_nivel(self):
        xp = self.xp
        nivel = 1
        xp_maximo = 100
        while xp >= xp_maximo:
            xp -= xp_maximo
            nivel += 1
            xp_maximo *= 2
        return nivel
    
    def calcular_xp_maximo(self):
        xp = self.xp
        nivel = 1
        xp_maximo = 100
        while xp >= xp_maximo:
            xp -= xp_maximo
            nivel += 1
            xp_maximo *= 2
        return xp_maximo*2
    
    def aumentar_xp(self, xp):
        self.xp = self.xp + xp

nome = input('Digite o nome do seu personagem: ')
classe = input('Digite a classe do seu personagem: ')
xp = int(input('Digite a quantidade de experiência do seu personagem: '))

jogador1 = Player(nome, classe, xp)

print(f'Nome: {jogador1.name}\nClasse: {jogador1.classe}\nNível: {jogador1.calcular_nivel()} ({jogador1.xp}xp/{jogador1.calcular_xp_maximo()}xp)')

aumentar = int(input('Digite quantos pontos de experiência você gostaria de dar ao seu personagem: '))

jogador1.aumentar_xp(aumentar)

print(f'Nível: {jogador1.calcular_nivel()} ({jogador1.xp}xp/{jogador1.calcular_xp_maximo()}xp)')