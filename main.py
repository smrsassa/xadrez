import pygame
import gameEngine


LARGURA = ALTURA = 512
DIMENSAO = 8
TAMANHO_CASA = ALTURA // DIMENSAO
MAX_FPS = 15
IMAGENS = {}

def carregarImagens():
    pecas = ["wR", "wN", "ww", "wQ", "wK", "wP", "bR", "bN", "bB", "bQ", "bK", "bP"]
    for peca in pecas:
        IMAGENS[peca] = pygame.transform.scale(pygame.image.load('img/' + peca + '.png'), (TAMANHO_CASA, TAMANHO_CASA))

def main():
    pygame.init()
    tela = pygame.display.set_mode(( LARGURA, ALTURA ))
    clock = pygame.time.Clock()
    tela.fill(pygame.Color('white'))
    gEngine = gameEngine.gameEngine()
    print(gEngine.tabuleiro)

if __name__ == '__main__':
    main()
