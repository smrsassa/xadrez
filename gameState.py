
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
    
    def mover(self, mover):
        self.tabuleiro[mover.inicioRow][mover.inicioCol] = "--"
        self.tabuleiro[mover.fimRow][mover.fimCol] = mover.pecaMovida
        self.moveLog.append(mover)
        self.brancasJogam = not self.brancasJogam
    