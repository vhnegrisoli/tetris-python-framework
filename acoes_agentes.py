from enum import Enum
class AcoesJogador(Enum):
    PERMUTAR = "permutar"

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