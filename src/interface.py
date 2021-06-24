import pygame
from webbrowser import open_new as openBrowserTab

class Interface:
    def __init__(self, tela: pygame.Surface, tamTabuleiro: int) -> None:
        self.tela = tela
        self.tamanhoTabuleiro = tamTabuleiro
        self.botaoDownloadMoves()
        self.botaoGit()

    def clique(self, x: int, y: int) -> None:
        if y > 460 and y < 510:
            pass
            #self.botaoDownloadMovesOnClick()
        elif y > 510:
            self.botaoGitOnClick()

    def botaoDownloadMoves(self) -> None:
        downloadIcon = pygame.transform.scale(pygame.image.load('img/download.png'), (50, 50))
        self.tela.blit(downloadIcon, pygame.Rect(560, 460, 50, 50))
    def botaoDownloadMovesOnClick(self, fen: str, movLog: list) -> None:
        arquivo = open("partidas/partidas.txt", "a")

        arquivo.write(fen)
        arquivo.write("\n")
        arquivo.writelines(mov + " - " for mov in movLog)
        arquivo.write("\n")
        arquivo.write("=-=" * 30)
        arquivo.write("\n")

        arquivo.close()


    def botaoGit(self) -> None:
        gitHubLogo = pygame.transform.scale(pygame.image.load('img/gitHub.png'), (50, 50))
        self.tela.blit(gitHubLogo, pygame.Rect(560, 510, 50, 50))
    def botaoGitOnClick(self) -> None:
        openBrowserTab('https://github.com/smrsassa/xadrez')
