import pygame
import webbrowser

class Interface:
    def __init__(self, tela, tamTabuleiro, ignora = False):
        if not ignora:
            self.tela = tela
            self.tamanhoTabuleiro = tamTabuleiro
            self.posLinha = 80
            self.posColuna = 20
            font = pygame.font.Font(None,30)
            titulo = font.render("Xadrez em Python", 1,(255,255,255))
            tela.blit(titulo, (tamTabuleiro + self.posColuna, 20))
            self.mover = 0
            pygame.draw.rect(tela, (90,90,90), (835, 80, 15, 400)) #SCROLL BAR
            pygame.draw.rect(tela, (0,0,0), (835, (self.mover + 80), 15, 60)) #SCROLLING BAR
    
    def scrollBar(self, tela, sentido):
        self.mover += (15 * sentido)
        pygame.draw.rect(tela, (90,90,90), (835, 80, 15, 405)) #SCROLL BAR
        pygame.draw.rect(tela, (0,0,0), (835, (self.mover + 80), 15, 60)) #SCROLLING BAR


    def chessNotationLog(self):
        if self.posLinha > 400:
            print(self.posLinha)
            self.posLinha = 80
            self.posColuna += 75
        font = pygame.font.Font(None, 24)
        titulo = font.render("notation", 1,(255,255,255))
        self.tela.blit(titulo, (self.tamanhoTabuleiro + self.posColuna, self.posLinha))
        self.posLinha += 26
