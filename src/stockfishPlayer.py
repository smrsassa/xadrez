import subprocess


class StockfishPlayer:
    def __init__(self, path: str, depth: int = 5) -> None:        
        self.stockfish = subprocess.Popen(
            path, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )

        self.depth = str(depth)
        self.cmdWrite("uci")

        self.iniciaPartida()

    def cmdWrite(self, comando: str) -> None:
        self.stockfish.stdin.write(f"{comando}\n")
        self.stockfish.stdin.flush()

    def goDepth(self) -> None:
        self.cmdWrite(f"go depth {self.depth}")

    def cmdLerLinha(self) -> str:
        return self.stockfish.stdout.readline().strip()

    def iniciaPartida(self) -> None:
        self.cmdWrite("ucinewgame")

    def listaParaString(*moves: list) -> str:
        moves = moves[1]
        result = ""
        for move in moves:
            result += f"{move} "
        return result.strip()

    def posicaoTabuleiro(self, moves: list) -> None:
        if moves is None:
            moves = []
        self.cmdWrite(f"position startpos moves {self.listaParaString(moves)}")
    
    def melhorMovimento(self) -> str:
        self.goDepth()
        last_text: str = ""
        while True:
            text = self.cmdLerLinha()
            splitted_text = text.split(" ")
            if splitted_text[0] == "bestmove":
                if splitted_text[1] == "(none)":
                    return None
                self.info = last_text
                return splitted_text[1]
            last_text = text

    def posicaoFen(self) -> str:
        self.cmdWrite("d")
        while True:
            text = self.cmdLerLinha()
            splitted_text = text.split(" ")
            if splitted_text[0] == "Fen:":
                return " ".join(splitted_text[1:])

if __name__ == '__main__':
    stock = StockfishPlayer(r'C:/Users/g_gar/pyProj/stockfish_13_win_x64_bmi2/stockfish_13_win_x64_bmi2.exe')
    stock.posicaoTabuleiro(["e2e4", "e7e5"])
    print(stock.melhorMovimento())
