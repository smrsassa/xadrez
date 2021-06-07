import pygame
import webbrowser

class Interface:
    def __init__(self, tela, tamTabuleiro, ignora = False):
        self.tela = tela
        self.tamanhoTabuleiro = tamTabuleiro
        self.botaoDownloadMoves()
        self.botaoGit()

    def clique(self, x, y):
        if y > 460 and y < 510:
            self.botaoDownloadMovesOnClick()
        elif y > 510:
            self.botaoGitOnClick()


    def botaoDownloadMoves(self):
        downloadIcon = pygame.transform.scale(pygame.image.load('img/download.png'), (45, 45))
        self.tela.blit(downloadIcon, pygame.Rect(562, 462, 45, 45))
    def botaoDownloadMovesOnClick(self):
        print("aqui")

    def botaoGit(self):
        gitHubLogo = pygame.transform.scale(pygame.image.load('img/gitHub.png'), (50, 50))
        self.tela.blit(gitHubLogo, pygame.Rect(560, 510, 50, 50))
    def botaoGitOnClick(self):
        webbrowser.open_new('https://github.com/smrsassa/xadrez')