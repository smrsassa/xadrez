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
            tela.blit(titulo, (tamTabuleiro + self.posColuna, 30))

    def chessNotationLog(self, notation):
        if self.posLinha > 400:
            print(self.posLinha)
            self.posLinha = 80
            self.posColuna += 75
        font = pygame.font.Font(None, 24)
        titulo = font.render(notation, 1,(255,255,255))
        self.tela.blit(titulo, (self.tamanhoTabuleiro + self.posColuna, self.posLinha))
        self.posLinha += 26

