
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
        return self.getRankFiles(self.inicioRow, self.inicioCol) + self.getRankFiles(self.fimRow, self.fimCol)
