import pygame
import gameState
import movimento


LARGURA = ALTURA = 512
DIMENSAO = 8
TAMANHO_CASA = ALTURA // DIMENSAO
MAX_FPS = 15
IMAGENS = {}

class MainGame:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(( LARGURA, ALTURA ))
        self.clock = pygame.time.Clock()
        self.tela.fill(pygame.Color('white'))
        self.rodando = True
        self.sqSelecionado = ()
        self.clicks = []
    
    def carregarImagens(self):
        pecas = ["wR", "wN", "wB", "wQ", "wK", "wP", "bR", "bN", "bB", "bQ", "bK", "bP"]
        for peca in pecas:
            IMAGENS[peca] = pygame.transform.scale(pygame.image.load('img/' + peca + '.png'), (TAMANHO_CASA, TAMANHO_CASA))

    def desenhaTabuleiro(self, tela):
        cores = [ pygame.Color(235, 235, 208), pygame.Color(119, 148, 85) ]
        for linha in range(DIMENSAO):
            for coluna in range(DIMENSAO):
                cor = cores[ (linha + coluna) % 2 ]
                pygame.draw.rect(tela, cor, pygame.Rect(coluna*TAMANHO_CASA, linha*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))

    def desenhaPecas(self, tela, tabuleiro):
        for linha in range(DIMENSAO):
            for coluna in range(DIMENSAO):
                peca = tabuleiro[linha][coluna]
                if peca != "--":
                    tela.blit(IMAGENS[peca], pygame.Rect(coluna*TAMANHO_CASA, linha*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))
    
    def desenhaEstadoAtual(self, tela, gState):
        self.desenhaTabuleiro(tela)
        self.desenhaPecas(tela, gState.tabuleiro)
    
    def iniciaJogo(self):

        gState = gameState.gameState()
        self.carregarImagens()

        while self.rodando:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.rodando = False
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    col = x // TAMANHO_CASA
                    row = y // TAMANHO_CASA
                    if self.sqSelecionado == (row, col):
                        self.sqSelecionado = ()
                        self.clicks = []
                    else:
                        self.sqSelecionado = (row, col)
                        self.clicks.append(self.sqSelecionado)

                    if len(self.clicks) == 2:
                        mover = movimento.Mover(self.clicks[0], self.clicks[1], gState.tabuleiro)
                        print(mover.getChessNotation())
                        gState.mover(mover)
                        self.sqSelecionado = ()
                        self.clicks = []

            self.desenhaEstadoAtual(self.tela, gState)

            self.clock.tick(MAX_FPS)
            pygame.display.flip()  

if __name__ == '__main__':
    jogo = MainGame()
    jogo.iniciaJogo()
