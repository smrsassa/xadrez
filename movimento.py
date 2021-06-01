
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
            return self.movTorre(cor, posicaoAtual, tabuleiro)
        elif peca == 'N':
            return []
        elif peca == 'B':
            return self.movBispo(cor, posicaoAtual, tabuleiro)
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
        if (posicaoAtual[1] + 1) < 8:
            diagonalDireita = tabuleiro[(posicaoAtual[0] + (inverte*1))][(posicaoAtual[1] + 1)]
            if diagonalDireita != '--' and diagonalDireita[0] != cor:
                movPossiveis.append(((posicaoAtual[0] + (inverte*1)), (posicaoAtual[1] + 1)))
        if diagonalEsquerda != '--' and diagonalEsquerda[0] != cor:
            movPossiveis.append(((posicaoAtual[0] + (inverte*1)), (posicaoAtual[1] - 1)))

        qtdeMov = 1
        if posicaoAtual[0] == posInicial:
            qtdeMov += 1
        for mov in range(1, (qtdeMov + 1)):
            if tabuleiro[(posicaoAtual[0] + (inverte*mov))][posicaoAtual[1]] == '--':
                movPossiveis.append(((posicaoAtual[0] + (inverte*mov)), posicaoAtual[1]))
            if mov == 1 and tabuleiro[(posicaoAtual[0] + (inverte*mov))][posicaoAtual[1]] != '--':
                break

        return movPossiveis

    def loopMovimentoLinhaReta(self, vertical, inicio, fim, passo, posicaoAtual, tabuleiro, cor):
        movPossiveis = []
        if vertical:
            for casa in range(inicio, fim, passo):
                if tabuleiro[casa][posicaoAtual[1]] == '--':
                    movPossiveis.append((casa, posicaoAtual[1]))
                elif tabuleiro[casa][posicaoAtual[1]][0] != cor:
                    movPossiveis.append((casa, posicaoAtual[1]))
                    break
                else:
                    break
        else:
            for casa in range(inicio, fim, passo):
                if tabuleiro[posicaoAtual[0]][casa] == '--':
                    movPossiveis.append((posicaoAtual[0], casa))
                elif tabuleiro[posicaoAtual[0]][casa][0] != cor:
                    movPossiveis.append((posicaoAtual[0], casa))
                    break
                else:
                    break

        return movPossiveis

    def movTorre(self, cor, posicaoAtual, tabuleiro):
        movPossiveis = []
        menor = -1
        maior = 8
        movPossiveis = movPossiveis + self.loopMovimentoLinhaReta(True, (posicaoAtual[0]+1), maior, 1, posicaoAtual, tabuleiro, cor)
        movPossiveis = movPossiveis + self.loopMovimentoLinhaReta(True, (posicaoAtual[0]-1), menor, -1, posicaoAtual, tabuleiro, cor)
        movPossiveis = movPossiveis + self.loopMovimentoLinhaReta(False, (posicaoAtual[1]+1), maior, 1, posicaoAtual, tabuleiro, cor)
        movPossiveis = movPossiveis + self.loopMovimentoLinhaReta(False, (posicaoAtual[1]-1), menor, -1, posicaoAtual, tabuleiro, cor)

        return movPossiveis
        
    def loopMovimentoLinhaDiagonal(self, sentidoRow, sentidoCol, cor, posicaoAtual, tabuleiro):
        movPossiveis = []
        for casa in range(1, 8):
            row = posicaoAtual[0] + (casa * sentidoRow)
            col = posicaoAtual[1] + (casa * sentidoCol)
            if row < 0 or row > 7 or col < 0 or col > 7 :
                break
            elif tabuleiro[row][col] == '--':
                movPossiveis.append((row, col))
            elif tabuleiro[row][col][0] != cor:
                movPossiveis.append((row, col))
                break
            else:
                break
        return movPossiveis

    def movBispo(self, cor, posicaoAtual, tabuleiro):
        movPossiveis = []
    
        movPossiveis = self.loopMovimentoLinhaDiagonal(1, 1, cor, posicaoAtual, tabuleiro)
        
        movPossiveis = movPossiveis + self.loopMovimentoLinhaDiagonal(-1, 1, cor, posicaoAtual, tabuleiro)
        movPossiveis = movPossiveis + self.loopMovimentoLinhaDiagonal(1, -1, cor, posicaoAtual, tabuleiro)
        movPossiveis = movPossiveis + self.loopMovimentoLinhaDiagonal(-1, -1, cor, posicaoAtual, tabuleiro)
    
        return movPossiveis
    