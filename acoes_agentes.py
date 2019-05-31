from enum import Enum
class AcoesJogador(Enum):
    PERMUTAR = "permutar"
    MOVER_DIREITA = "direita"
    MOVER_ESQUERDA = "esquerda"
    MOVER_BAIXO = "baixo"

from dataclasses import dataclass
@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()
    
    @classmethod
    def permutar(cls, i, j):
        """ Cria uma instância da classe AcaoJogador representando a acao
        permutar elementos das posicoes i e j.
        """
        return cls(AcoesJogador.PERMUTAR, (i,j))


    @classmethod
    def direita(cls, event):
        """ Cria uma instância da classe AcaoJogador representando a acao
        permutar elementos das posicoes i e j.
        """
        return cls(AcoesJogador.MOVER_DIREITA (event))