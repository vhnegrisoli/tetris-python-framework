from enum import Enum, auto
class AgentesOrdenador(Enum):
    JOGADOR_PADRAO = auto()

class Posicao(Enum):
    VAZIO = 0
    PREENCHIDO = 1

class Peca:

    def __init__(self, linha, coluna, tipo):
        self.linha = linha
        self.coluna = coluna

        # O tipo define como será a peça, sendo:
        # Esta é a cobra em formato de cobra
        if(tipo == 1):
            self.grade = [[Posicao.VAZIO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.PREENCHIDO.value,
                              Posicao.PREENCHIDO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value]]
            self.tamanho = 3

        # Esta é a peça em formato de cobra inversa
        elif(tipo == 2):
            self.grade = [[Posicao.VAZIO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value,
                              Posicao.PREENCHIDO.value],
                          [Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value, Posicao.VAZIO.value]]
            self.tamanho = 3

        # Esta é a peça em formato de quadrado
        elif(tipo == 3):
            self.grade = [[Posicao.VAZIO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value,
                              Posicao.PREENCHIDO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value]]
            self.tamanho = 3

        # Esta é a peça em formato de L
        elif(tipo == 4):
            self.grade = [[Posicao.VAZIO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.VAZIO.value,
                              Posicao.PREENCHIDO.value],
                          [Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value]]
            self.tamanho = 3

        # Esta é a peça em formato de L invertido
        elif(tipo == 5):
            self.grade = [[Posicao.VAZIO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.PREENCHIDO.value,
                              Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value]]
            self.tamanho = 3

        # Esta é a peça em formato de T
        elif(tipo == 6):
            self.grade = [[Posicao.VAZIO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value,
                              Posicao.VAZIO.value],
                          [Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value, Posicao.PREENCHIDO.value]]
            self.tamanho = 3

        # Esta é a peça em formato de barra, em uma matriz 4x4
        elif(tipo == 7):
            self.grade = [[Posicao.VAZIO.value, Posicao.PREENCHIDO.value, Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value,
                              Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value,
                              Posicao.VAZIO.value, Posicao.VAZIO.value],
                          [Posicao.VAZIO.value, Posicao.PREENCHIDO.value, Posicao.VAZIO.value, Posicao.VAZIO.value]]
            self.tamanho = 4


    def desce(self, Tela):
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if self.grade[indiceLinha][indiceColuna] * (self.coluna+1+indiceLinha) >= qtdQuadradosAltura:
                    return 0
                try:
                    if self.grade[indiceLinha][indiceColuna] == 1 and Tela.grade[self.coluna+indiceLinha+1][self.linha+indiceColuna] * self.grade[indiceLinha][indiceColuna] != 0:
                        return 0
                except:
                    print('fim de jogo')
        self.coluna = self.coluna + 1
        return 1

    # Método que permite a movimentação à direita na grade da tela
    def direita(self, Tela):
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if self.grade[indiceLinha][indiceColuna] * (self.linha+1+indiceColuna) > qtdQuadradosLargura-1:
                    return 0
                if Tela.grade[self.coluna][self.linha+1] * self.grade[indiceLinha][indiceColuna] != 0:
                    return 0
        self.linha = self.linha + 1
        return 1

    # Método que permite a movimentação à esquerda na grade da tela
    def esquerda(self, Tela):
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if self.grade[indiceLinha][indiceColuna] * (self.linha-1+indiceLinha) < 0:
                    return 0
                if Tela.grade[self.coluna][self.linha+1] * self.grade[indiceLinha][indiceColuna] != 0:
                    return 0
        self.linha = self.linha - 1
        return 1


quadradoLado = 30
qtdQuadradosLargura = 8
qtdQuadradosAltura = 10
largura = quadradoLado * qtdQuadradosLargura
altura = quadradoLado * qtdQuadradosAltura
indice = 0
listaPecas = [
            Peca(3, 1, 4),
            Peca(3, 1, 1),
            Peca(3, 1, 3),
            Peca(3, 1, 4),
            Peca(3, 1, 7),
            Peca(3, 1, 3),
            Peca(3, 1, 2),
            Peca(3, 1, 5),
            Peca(3, 1, 7),
            Peca(3, 1, 6),
]

from regras_jogo.regras_abstratas import AbstractRegrasJogo
from tkinter import Tk, Canvas
class JogoOrdenador(AbstractRegrasJogo):

    def __init__(self, qtde_elems, a_seed=None):
        self.grade = [[0 for indiceLinha in range(qtdQuadradosLargura)]
        for indiceColuna in range(qtdQuadradosAltura)]
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura,
        height=altura, bg='black')
        self.canvas.pack()
        self.peca = listaPecas[0]
        '''self.window.bind("<Right>", print('right'))
        self.window.bind("<Left>", print('left'))
        self.window.bind("<Down>", print('down'))'''
        
        


    # Método responsável por adicionar peças ao jogo conforme forem caindo as anteriores
    def addPecas(self, peca):
        for lin in range(peca.tamanho):
            for col in range(peca.tamanho):
                if peca.grade[lin][col] != 0:
                    self.grade[lin+peca.coluna][col +  peca.linha] = peca.grade[lin][col]

    def registrarAgenteJogador(self, elem_agente=AgentesOrdenador.JOGADOR_PADRAO):
        """ Só há um agente, o jogador, então não preciso de lógica.
        """
        return 1
    
    def isFim(self):
        """ Se a lista estiver ordenada, fim de jogo.   
            XXXX
        """
        return False


    def gerarCampoVisao(self, id_agente):
        """ Como esse jogo é muito simples e totalmente observável, vou apenas
        utilizar um dicionário diretamente, com uma tupla imutável, como objeto
        de visão.
        """
        for indiceLinha in range(self.peca.tamanho):
            for indiceColuna in range(self.peca.tamanho):
                if self.peca.grade[indiceLinha][indiceColuna] != 0:
                    self.canvas.create_polygon(
                        [(self.peca.linha + indiceColuna) * quadradoLado+2,
                         (self.peca.coluna + indiceLinha) * quadradoLado+2,
                         (self.peca.linha + indiceColuna) *
                         quadradoLado + quadradoLado-2,
                         (self.peca.coluna + indiceLinha) * quadradoLado+2,
                         (self.peca.linha + indiceColuna) *
                         quadradoLado + quadradoLado - 2,
                         (self.peca.coluna + indiceLinha) *
                         quadradoLado + quadradoLado - 2,
                         (self.peca.linha + indiceColuna) * quadradoLado+2,
                         (self.peca.coluna + indiceLinha)*quadradoLado+quadradoLado-2], fill='green')

        for lin in range(qtdQuadradosAltura):
            for col in range(qtdQuadradosLargura):
                if self.grade[lin][col] != 0:
                    self.canvas.create_polygon(
                        [col*quadradoLado+2,
                         lin * quadradoLado+2,
                         col*quadradoLado+quadradoLado-2,
                         lin*quadradoLado + 2,
                         col*quadradoLado+quadradoLado-2,
                         lin*quadradoLado+quadradoLado-2,
                         col*quadradoLado+2,
                         lin*quadradoLado+quadradoLado-2], fill="red")
        return { "grade": tuple(self.grade) }

    def registrarProximaAcao(self, id_agente, acao):
        """ Como só há um agente atuando no mundo, o próprio jogador, não é
        necessário nenhum mecanismo para guardar ações associadas por agentes
        distintos.
        """
        self.acao_jogador = acao
    
    def atualizarEstado(self, diferencial_tempo):
        """ Não preciso me preocupar com a passagem do tempo, pois só uma
        jogada é feita por vez, e o jogo não muda seu estado sem jogadas.

        Verifico a ação última registrada e atualizado o estado do jogo
        computando-a.
        """
        from acoes_agentes import AcoesJogador
        if self.acao_jogador.tipo == AcoesJogador.MOVER:
            direcao = self.acao_jogador.parametros
            if(direcao == "dir"):
                self.peca.direita(self)
            if(direcao == "esq"):
                self.peca.esquerda(self)
            if(direcao == "baixo"):
                global indice
                desceu = self.peca.desce(self)
                if desceu == 0:
                    if(indice == 9):
                        print("Você Venceu!")
                        quit()

                    indice += 1
                    self.addPecas(self.peca)
                    self.peca = listaPecas[indice]
                    for lin in range(self.peca.tamanho):
                        for col in range(self.peca.tamanho):
                            if self.peca.grade[lin][col] == 1 and self.grade[self.peca.coluna+lin][self.peca.linha + col] != 0:
                                print("Você perdeu!")
                                quit()


            self.canvas.delete('all')
        else:
            raise TypeError
