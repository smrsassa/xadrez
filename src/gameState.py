import movimento

class gameState:
    def __init__(self) -> None:
        self.tabuleiro = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.brancasJogam = True
        self.moveLog = []
        self.moveLogNotation = []

    def mover(self, clicks: list) -> None:
        corPeca = self.tabuleiro[clicks[0][0]][clicks[0][1]][0]
        peca = self.tabuleiro[clicks[0][0]][clicks[0][1]][1]
        if (corPeca == "w" and self.brancasJogam) or (corPeca == "b" and not self.brancasJogam):
            mover = movimento.Mover(clicks[0], clicks[1], self.tabuleiro)
            movimentosPossiveis = mover.validaMovimento(peca, corPeca, (clicks[0][0], clicks[0][1]), self.tabuleiro, self.moveLogNotation)
            if clicks[1] in movimentosPossiveis:
                self.tabuleiro[mover.inicioRow][mover.inicioCol] = "--"
                if peca == 'P':
                    if mover.fimRow == 0 or mover.fimRow == 7:
                        mover.pecaMovida = corPeca + 'Q'
                    peaoPassado = mover.peaoPassado(corPeca, (clicks[0][0], clicks[0][1]), self.tabuleiro, self.moveLogNotation)
                    if (mover.fimRow, mover.fimCol) == peaoPassado[0]:
                        self.tabuleiro[mover.inicioRow][(mover.inicioCol + 1)] = "--"
                    elif (mover.fimRow, mover.fimCol) == peaoPassado[1]:
                        self.tabuleiro[mover.inicioRow][(mover.inicioCol - 1)] = "--"
                if peca == 'K':
                    colDiferenca = mover.fimCol - mover.inicioCol
                    if abs(colDiferenca) == 2:
                        if colDiferenca > 0:
                            self.tabuleiro[mover.inicioRow][7] = "--"
                            self.tabuleiro[mover.inicioRow][5] = corPeca+"R"
                        else:
                            self.tabuleiro[mover.inicioRow][0] = "--"
                            self.tabuleiro[mover.inicioRow][3] = corPeca+"R"

                self.tabuleiro[mover.fimRow][mover.fimCol] = mover.pecaMovida
                self.moveLog.append(mover)
                self.brancasJogam = not self.brancasJogam
                self.moveLogNotation.append(mover.getChessNotation())
