import movimento


class gameState:
    def __init__(self):
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

    def mover(self, clicks):
        corPeca = self.tabuleiro[clicks[0][0]][clicks[0][1]][0]
        peca = self.tabuleiro[clicks[0][0]][clicks[0][1]][1]
        if (corPeca == "w" and self.brancasJogam) or (corPeca == "b" and not self.brancasJogam):
            mover = movimento.Mover(clicks[0], clicks[1], self.tabuleiro)
            movimentosPossiveis = mover.validaMovimento(peca, corPeca, (clicks[0][0], clicks[0][1]), self.tabuleiro)
            if clicks[1] in movimentosPossiveis:
                print(mover.getChessNotation())
                self.tabuleiro[mover.inicioRow][mover.inicioCol] = "--"
                self.tabuleiro[mover.fimRow][mover.fimCol] = mover.pecaMovida
                self.moveLog.append(mover)
                self.brancasJogam = not self.brancasJogam
