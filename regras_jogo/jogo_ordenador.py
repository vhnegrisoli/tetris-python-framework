from regras_jogo.regras_abstratas import AbstractRegrasJogo
from enum import Enum, auto




class AgentesOrdenador(Enum):
    JOGADOR_PADRAO = auto()


class JogoOrdenador(AbstractRegrasJogo):

    def __init__(self, qtde_elems, a_seed=None):
        from random import randint, seed

        seed(a_seed)
        self.elementos = [randint(1, qtde_elems*3) for _ in range(qtde_elems)]

    
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
