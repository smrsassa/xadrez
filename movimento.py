
class Mover:
    rankRows = {"1": 7,"2": 6,"3": 5,"4": 4,"5": 3,"6": 2,"7": 1,"8": 0}
    rowsRanks = {v: k for k, v in rankRows.items()}
    filesCols = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7}
    colsFiles = {v: k for k, v in filesCols.items()}

    def __init__(self, inicio, fim, tabuleiro):
        self.inicioRow, self.inicioCol = inicio
        self.fimRow, self.fimCol = fim
        self.pecaMovida = tabuleiro[self.inicioRow][self.inicioCol]
        self.pecaCapturada = tabuleiro[self.fimRow][self.fimCol]
    
    def getRankFiles(self, row, col):
        return self.colsFiles[col] + self.rowsRanks[row]

    def getChessNotation(self):
        return self.getRankFiles(self.inicioRow, self.inicioCol) + " -> " + self.getRankFiles(self.fimRow, self.fimCol)

    def validaMovimento(self, peca, cor, posicaoAtual, tabuleiro):
        if peca == 'P':
            return self.movPeao(cor, posicaoAtual, tabuleiro)
        elif peca == 'R':
            return []
        elif peca == 'N':
            return []
        elif peca == 'B':
            return []
        elif peca == 'K':
            return []
        elif peca == 'Q':
            return []
        
    def movPeao(self, cor, posicaoAtual, tabuleiro):
        movPossiveis = []
        inverte = 1
        posInicial = 1
        if cor == 'w':
            inverte *= -1
            posInicial = 6

        diagonalEsquerda = tabuleiro[(posicaoAtual[0] + (inverte*1))][(posicaoAtual[1] - 1)]
        diagonalDireita = tabuleiro[(posicaoAtual[0] + (inverte*1))][(posicaoAtual[1] + 1)]
        if diagonalEsquerda != '--' and diagonalEsquerda[0] != 'w':
            movPossiveis.append(((posicaoAtual[0] + (inverte*1)), (posicaoAtual[1] - 1)))
        if diagonalDireita != '--' and diagonalDireita[0] != 'w':
            movPossiveis.append(((posicaoAtual[0] + (inverte*1)), (posicaoAtual[1] + 1)))

        qtdeMov = 1
        if posicaoAtual[0] == posInicial:
            qtdeMov += 1
        for mov in range(1, (qtdeMov + 1)):
            if tabuleiro[(posicaoAtual[0] + (inverte*mov))][posicaoAtual[1]] == '--':
                movPossiveis.append(((posicaoAtual[0] + (inverte*mov)), posicaoAtual[1]))
            if mov == 1 and tabuleiro[(posicaoAtual[0] + (inverte*mov))][posicaoAtual[1]] != '--':
                break

        return movPossiveis
        

