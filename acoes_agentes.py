from enum import Enum
class AcoesJogador(Enum):
    MOVER = "mover"

from dataclasses import dataclass
@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()
  

    @classmethod
    def mover(cls, direcao):
        """ Cria uma instância da classe AcaoJogador representando a acao
        de mover a Peca a direita.
        """
        return cls(AcoesJogador.MOVER, (direcao))
    
  

