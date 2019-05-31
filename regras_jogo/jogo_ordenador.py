from regras_jogo.regras_abstratas import AbstractRegrasJogo
from enum import Enum, auto

qtdQuadradosLargura = 8
quadradoLado = 30
qtdQuadradosAltura = 10
largura = quadradoLado * qtdQuadradosLargura
altura = quadradoLado * qtdQuadradosAltura
indice = 0
listaPecas = []

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

    # Método responsável por girar uma peça no jogo

    def vira(self, Tela):
        # Cria um array de cópia para armazenar a peça a ser giradea
        copia = [[0 for indiceLinha in range(
            self.tamanho)] for indiceColuna in range(self.tamanho)]

        # Faz a cópia girar a peça
        for lin in range(self.tamanho):
            for col in range(self.tamanho):
                copia[self.tamanho - 1 - col][lin] = self.grade[lin][col]

        # Verifica colisão do array de cópia com algo da tela
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if copia[indiceLinha][indiceColuna] * (self.coluna+indiceLinha) >= qtdQuadradosAltura:
                    return 0
                if copia[indiceLinha][indiceColuna] == 1 and Tela.grade[self.coluna+indiceLinha][self.linha+indiceColuna] != 0:
                    return 0
        # Copia os valores do array cópia para a grade
        for lin in range(self.tamanho):
            for col in range(self.tamanho):
                self.grade[lin][col] = copia[lin][col]
        return 1

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

class Tela:

    def __init__(self):
        # Define uma matriz e itera por ela usando [[], []]
        self.grade = [[0 for indiceLinha in range(qtdQuadradosLargura)]
                      for indiceColuna in range(qtdQuadradosAltura)]

    # Método responsável por adicionar peças ao jogo conforme forem caindo as anteriores
    def addPecas(self, peca):
        for lin in range(peca.tamanho):
            for col in range(peca.tamanho):
                if peca.grade[lin][col] != 0:
                    self.grade[lin+peca.coluna][col +
                                                peca.linha] = peca.grade[lin][col]

class AgentesOrdenador(Enum):
    JOGADOR_PADRAO = auto()


class JogoOrdenador(AbstractRegrasJogo):

    def __init__(self, qtde_elems, a_seed=None):
        from random import randint, seed
        from tkinter import Tk, Canvas
        seed(a_seed)
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura,
                             height=altura, bg='black')
        self.canvas.pack()
        
        self.elementos = [randint(1, qtde_elems*3) for _ in range(qtde_elems)]
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
        self.peca = listaPecas[indice]
        self.numPeca = 0
        self.window.bind("<Right>", self.moverParaDireita)
        self.window.bind("<Left>", self.moverParaEsquerda)
        self.window.bind("<Down>", self.moverParaBaixo)
        self.tela = Tela()


        


    
    def moverParaEsquerda(self, event):
        print('esquerda')
        self.peca.esquerda(self.tela)

    def moverParaDireita(self, event):
        print('dir')
        self.peca.direita(self.tela)

    def moverParaBaixo(self, event):
        print('baixo')
        global indice
        desceu = self.peca.desce(self.tela)
        if desceu == 0:
            if(indice == 9):
                print("Você Venceu!")
                quit()

            indice += 1
            self.tela.addPecas(self.peca)
            self.peca = listaPecas[indice]
            for lin in range(self.peca.tamanho):
                for col in range(self.peca.tamanho):
                    if self.peca.grade[lin][col] == 1 and self.tela.grade[self.peca.coluna+lin][self.peca.linha + col] != 0:
                        print("Você perdeu!")
                        quit()


    def registrarAgenteJogador(self, elem_agente=AgentesOrdenador.JOGADOR_PADRAO):
        """ Só há um agente, o jogador, então não preciso de lógica.
        """
        return 1

    def isFim(self):
        """ Se a lista estiver ordenada, fim de jogo.
        """
        return all(self.elementos[i] <= self.elementos[i+1]
                   for i, _ in enumerate(self.elementos[:-1]))

    def gerarCampoVisao(self, id_agente):
        """ Como esse jogo é muito simples e totalmente observável, vou apenas
        utilizar um dicionário diretamente, com uma tupla imutável, como objeto
        de visão.
        """
        return {"disposicao": tuple(self.elementos)}

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
        if self.acao_jogador.tipo == AcoesJogador.PERMUTAR:
            i, j = self.acao_jogador.parametros
            self.elementos[i], self.elementos[j] = self.elementos[j], self.elementos[i]
        else:
            raise TypeError
