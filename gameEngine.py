
class gameEngine:
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


class mover():
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
        return self.getRankFiles(self.inicioRow, self.inicioCol) + self.getRankFiles(self.fimRow, self.fimCol)

    