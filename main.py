import pygame
from pygame.mixer import pre_init
import gameState
import interface


LARGURA = ALTURA = 560
TAMANO_INTERFACE = 50
DIMENSAO = 8
TAMANHO_CASA = ALTURA // DIMENSAO
MAX_FPS = 15
IMAGENS = {}

class MainGame:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(( LARGURA + TAMANO_INTERFACE, ALTURA ))
        pygame.display.set_caption('Xadrex')
        self.clock = pygame.time.Clock()
        self.tela.fill(pygame.Color(50, 50, 50))
        self.interface = interface.Interface(self.tela, LARGURA)
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

    def acoesJogo(self, gState, x, y):
        col = x // TAMANHO_CASA
        row = y // TAMANHO_CASA

        if self.sqSelecionado == (row, col):
            self.sqSelecionado = ()
            self.clicks = []
        elif len(self.clicks) == 0 and gState.tabuleiro[row][col] == '--':
            pass
        else:
            self.sqSelecionado = (row, col)
            self.clicks.append(self.sqSelecionado)

        if len(self.clicks) == 2:
            gState.mover(self.clicks)
            self.sqSelecionado = ()
            self.clicks = []

    def iniciaJogo(self):

        gState = gameState.gameState()
        self.carregarImagens()

        while self.rodando:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.rodando = False
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if x < LARGURA:
                        self.acoesJogo(gState, x, y)
                    else:
                        self.interface.clique(x, y)

            self.desenhaEstadoAtual(self.tela, gState)

            self.clock.tick(MAX_FPS)
            pygame.display.flip()  

if __name__ == '__main__':
    jogo = MainGame()
    jogo.iniciaJogo()
