from agentes.abstrato import AgenteAbstrato
class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        elems_dipostos = percepcao_mundo['grade']
        linhas = len(elems_dipostos)
        colunas = len(elems_dipostos[0])

        for i in range(linhas):
            for j in range(colunas):
                if(j == colunas - 1):
                    print("%d" %elems_dipostos[i][j])
                else:
                    print("%d" %elems_dipostos[i][j], end = " ")
    
    def escolherProximaAcao(self):
        from acoes_agentes import AcaoJogador
        
        direcao = input("Mover para? (dir, esq, baixo) ")
        return AcaoJogador.mover(direcao)


    