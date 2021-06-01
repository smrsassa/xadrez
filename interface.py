import pygame


class Interface:
    def __init__(self, tela, tamTabuleiro):
        self.tela = tela
        self.tamanhoTabuleiro = tamTabuleiro
        font=pygame.font.Font(None,30)
        scoretext=font.render("TO aqui", 1,(255,255,255))
        tela.blit(scoretext, (tamTabuleiro + 50, 50))
