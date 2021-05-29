import pygame
import gameEngine


LARGURA = ALTURA = 512
DIMENSAO = 8
TAMANHO_CASA = ALTURA // DIMENSAO
MAX_FPS = 15
IMAGENS = {}

def carregarImagens():
    pecas = ["wR", "wN", "wB", "wQ", "wK", "wP", "bR", "bN", "bB", "bQ", "bK", "bP"]
    for peca in pecas:
        IMAGENS[peca] = pygame.transform.scale(pygame.image.load('img/' + peca + '.png'), (TAMANHO_CASA, TAMANHO_CASA))

def desenhaTabuleiro(tela):
    cores = [ pygame.Color(235, 235, 208), pygame.Color(119, 148, 85) ]
    for linha in range(DIMENSAO):
        for coluna in range(DIMENSAO):
            cor = cores[ (linha + coluna) % 2 ]
            pygame.draw.rect(tela, cor, pygame.Rect(coluna*TAMANHO_CASA, linha*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))

def desenhaPecas(tela, tabuleiro):
    for linha in range(DIMENSAO):
        for coluna in range(DIMENSAO):
            peca = tabuleiro[linha][coluna]
            if peca != "--":
                tela.blit(IMAGENS[peca], pygame.Rect(coluna*TAMANHO_CASA, linha*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))


def desenhaEstadoAtual(tela, gEngine):
    desenhaTabuleiro(tela)
    desenhaPecas(tela, gEngine.tabuleiro)


def main():
    pygame.init()
    tela = pygame.display.set_mode(( LARGURA, ALTURA ))
    clock = pygame.time.Clock()
    tela.fill(pygame.Color('white'))
    gEngine = gameEngine.gameEngine()
    carregarImagens()
    rodando = True
    sqSelecionado = ()
    clicks = []

    while rodando:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                rodando = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TAMANHO_CASA
                row = y // TAMANHO_CASA
                if sqSelecionado == (row, col):
                    sqSelecionado = ()
                    clicks = []
                else:
                    sqSelecionado = (row, col)
                    clicks.append(sqSelecionado)
                
                if len(clicks) == 2:
                    mover = gameEngine.mover(clicks[0], clicks[1], gEngine.tabuleiro)
                    print(mover.getChessNotation())
                    gEngine.mover(mover)
                    sqSelecionado = ()
                    clicks = []
                    
                

        desenhaEstadoAtual(tela, gEngine)
        
        clock.tick(MAX_FPS)
        pygame.display.flip()   

if __name__ == '__main__':
    main()
