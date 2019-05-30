
qtdQuadradosLargura = 8
quadradoLado = 30
qtdQuadradosAltura = 10
largura = quadradoLado * qtdQuadradosLargura
altura = quadradoLado * qtdQuadradosAltura
indice = 0
listaPecas = []

from agentes.abstrato import AgenteAbstrato
class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        elems_dipostos = percepcao_mundo['disposicao']
        guia_indices = f'i- {",".join(f"{i:2d}" for i in range(len(elems_dipostos)))}'
        elems = f'e| {",".join(f"{e:2d}" for e in elems_dipostos)}'

        from tkinter import Tk, Canvas
               
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura,
                             height=altura, bg='black')
        self.canvas.pack()
        print(guia_indices, elems, '-'*len(elems), sep='\n')
    
    def escolherProximaAcao(self):
        from acoes_agentes import AcaoJogador
        i, j = (int(s) for s in input("Proxima troca (i,j)? ").split(',', 2))
        return AcaoJogador.permutar(i, j)