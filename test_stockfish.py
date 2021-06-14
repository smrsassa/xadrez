from stockfish import Stockfish


# https://pypi.org/project/stockfish/

stockfish = Stockfish(r'C:/Users/g_gar/pyProj/stockfish_13_win_x64_bmi2/stockfish_13_win_x64_bmi2.exe')

stockfish.set_position(["e2e4", "e7e6"])

print(stockfish.get_best_move())

print(stockfish.get_board_visual())

print(stockfish.get_fen_position()) #Forsyth–Edwards notation

print(stockfish.get_top_moves(3))

getChar = input(":")
