import pickle

import pygame  # Biblioteca de criação de jogos no python
import os  # Biblioteca para que a gegnte consiga interagir com o computador, pegar as imagens...
import random

# Definindo constantes
TELA_LARGURA = 1280
TELA_ALTURA = 720

IMAGEM_CHAO = pygame.image.load(os.path.join('imgs', 'chao.png'))  # Devo criar um chão maior que 1920

img_botao = pygame.image.load(os.path.join('imgs', 'respawn.png'))

IMAGEM_BOTAO = pygame.transform.scale(img_botao, (img_botao.get_width() // 1.8, img_botao.get_height() // 1.8))

IMAGEM_GAME_OVER = pygame.image.load(os.path.join('imgs', 'game_over_title.png'))

img_homem = pygame.image.load(os.path.join('imgs', 'homem.png'))
img_homem2 = pygame.image.load(os.path.join('imgs', 'homem2.png'))
img_homem3 = pygame.image.load(os.path.join('imgs', 'homem3.png'))
img_homem4 = pygame.image.load(os.path.join('imgs', 'homem4.png'))
img_obstaculo1 = pygame.image.load(os.path.join('imgs', 'planta_carnivora1.png'))
img_obstaculo2 = pygame.image.load(os.path.join('imgs', 'planta_carnivora_2.png'))
img_obstaculo3 = pygame.image.load(os.path.join('imgs', 'planta_carnivora__3.png'))
img_obstaculo4 = pygame.image.load(os.path.join('imgs', 'planta_carnivora_4.png'))
img_passaro1 = pygame.image.load(os.path.join('imgs', 'passaro1.png'))
img_passaro2 = pygame.image.load(os.path.join('imgs', 'passaro2.png'))
img_passaro3 = pygame.image.load(os.path.join('imgs', 'passaro3.png'))
img_passaro4 = pygame.image.load(os.path.join('imgs', 'passaro4.png'))
img_passaro5 = pygame.image.load(os.path.join('imgs', 'passaro5.png'))
img_nuvem = pygame.image.load(os.path.join('imgs', 'nuvem.png'))
img_GO = pygame.image.load(os.path.join('imgs', 'game_over_2.png'))
img_GO2 = pygame.image.load(os.path.join('imgs', 'game_over_3.png'))
img_GO3 = pygame.image.load(os.path.join('imgs', 'game_over_4.png'))
img_GO4 = pygame.image.load(os.path.join('imgs', 'game_over_5.png'))

IMAGEM_NUVEM = pygame.transform.scale(img_nuvem, (img_nuvem.get_width() // 2, img_nuvem.get_height() // 2))

IMAGEM_OBSTACULO = [
    pygame.transform.scale(img_obstaculo1, (img_obstaculo1.get_width() // 1.8, img_obstaculo1.get_height() // 1.8)),
    pygame.transform.scale(img_obstaculo2, (img_obstaculo2.get_width() // 1.8, img_obstaculo2.get_height() // 1.8)),
    pygame.transform.scale(img_obstaculo3, (img_obstaculo3.get_width() // 1.8, img_obstaculo3.get_height() // 1.8)),
    pygame.transform.scale(img_obstaculo4, (img_obstaculo4.get_width() // 1.8, img_obstaculo4.get_height() // 1.8)),
]

IMAGEM_HOMEM = [
    pygame.transform.scale(img_homem, (img_homem.get_width() // 1.8, img_homem.get_height() // 1.8)),
    pygame.transform.scale(img_homem2, (img_homem2.get_width() // 1.8, img_homem2.get_height() // 1.8)),
    pygame.transform.scale(img_homem3, (img_homem3.get_width() // 1.8, img_homem3.get_height() // 1.8)),
    pygame.transform.scale(img_homem3, (img_homem3.get_width() // 1.8, img_homem3.get_height() // 1.8)),
]

IMAGEM_PASSARO = [
    pygame.transform.scale(img_passaro1, (img_passaro1.get_width() // 5, img_passaro1.get_height() // 5)),
    pygame.transform.scale(img_passaro2, (img_passaro2.get_width() // 5, img_passaro2.get_height() // 5)),
    pygame.transform.scale(img_passaro3, (img_passaro3.get_width() // 5, img_passaro3.get_height() // 5)),
    pygame.transform.scale(img_passaro4, (img_passaro4.get_width() // 5, img_passaro4.get_height() // 5)),
    pygame.transform.scale(img_passaro5, (img_passaro5.get_width() // 8, img_passaro5.get_height() // 8)),
]

IMAGEM_GO = [
    pygame.transform.scale2x(img_GO),
    pygame.transform.scale2x(img_GO2),
    pygame.transform.scale2x(img_GO3),
    pygame.transform.scale2x(img_GO4),
]
# Iniciando o arquivo para salvar o melhor resultado
if os.path.getsize("resultado.bin") == 0:
    with open("resultado.bin", "wb") as f:
        pickle.dump(0, f) 

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    VELOCIDADE = 10 + random.randint(1, 5)
    TEMPO_ANIMACAO = 3
    LARGURA = IMAGEM_PASSARO[0].get_width()
    IMGS = IMAGEM_PASSARO

    def __init__(self, x, y):
        self.x0 = x
        self.y = y
        self.contagem_imagem = 0
        self.altura = self.y
        self.imagem = self.IMGS[0]

    def mover(self):
        self.x0 -= self.VELOCIDADE

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[3]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 5:
            self.imagem = self.IMGS[4]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 6:
            self.imagem = self.IMGS[3]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 7:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 8:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 8 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        tela.blit(self.imagem, (self.x0, self.y))


class Chao:
    VELOCIDADE = 10
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self):
        self.y = TELA_ALTURA - IMAGEM_CHAO.get_height()
        self.x0 = 0
        self.x1 = self.x0 + self.LARGURA

    def mover(self):
        self.x0 -= self.VELOCIDADE
        self.x1 -= self.VELOCIDADE
        if self.x0 + self.LARGURA < 0:
            self.x0 = self.x1 + self.LARGURA

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x0 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x0, self.y))
        tela.blit(self.IMAGEM, (self.x1, self.y))


class Homem:
    IMGS = IMAGEM_HOMEM
    TEMPO_ANIMACAO = 2
    GRAVIDADE = 1.2  # Aceleração da gravidade

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        if self.y == self.altura:  # Verificar se o homem está no chão
            self.velocidade = -10.5
            self.tempo = 0

            if self.altura != 0 and self.altura < 10:
                self.altura = self.y

    def mover(self):
        # Calcular o deslocamento
        self.tempo += 1
        deslocamento = (self.tempo ** 2) + self.velocidade * self.tempo

        # Restringir o deslocamento máximo
        if deslocamento > 30:
            deslocamento = 30

        # Ajustar a posição do homem
        self.y += 2 * deslocamento

        if self.y > self.altura:
            self.y = self.altura
            self.velocidade = 0

        # Atualizar a imagem do homem
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[3]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        tela.blit(self.imagem, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Obstaculo:
    VELOCIDADE = 30  # VElocidade de movimento dos viloes
    IMGS = IMAGEM_OBSTACULO
    TEMPO_ANIMACAO = 4

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.y = TELA_ALTURA - IMAGEM_CHAO.get_height() - IMAGEM_HOMEM[1].get_height() - 40
        self.passou = False
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def mover(self):
        self.x -= self.VELOCIDADE

        # Atualizar a imagem do obstaculo
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[3]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 5:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 6:
            self.imagem = self.IMGS[3]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 6 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        tela.blit(self.imagem, (self.x, self.y))

    def colidir(self, homem):
        # Criando mascaras para cada figura, para conseguir analiosar se houve colidemento
        passaro_mask = homem.get_mask()
        mask = pygame.mask.from_surface(self.imagem)

        distancia = (self.x - homem.x, self.y - round(homem.y))

        base_ponto = passaro_mask.overlap(mask, distancia)

        if base_ponto:
            return True
        else:
            return False


class Nuvem:
    VELOCIDADE = 2

    def __init__(self):
        self.x = TELA_LARGURA + 100
        self.y = 100 + random.randint(0, 100)
        self.imagem = IMAGEM_NUVEM

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))


class GameOver:
    VELOCIDADE = 4
    TEMPO_ANIMACAO = 5

    def __init__(self):
        self.x = TELA_LARGURA / 2 - 550
        self.y = TELA_ALTURA - IMAGEM_CHAO.get_height() - IMAGEM_GO[0].get_height() + 20
        self.IMGS = IMAGEM_GO
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[3]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        tela.blit(self.imagem, (self.x, self.y))


class Botao:
    def __init__(self, x, y, imagem):
        self.x = x
        self.y = y
        self.imagem = imagem

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))


def resetar_jogo():
    pontos = 0
    homens = [Homem(100, TELA_ALTURA - IMAGEM_CHAO.get_height() - IMAGEM_HOMEM[0].get_height() + 30)]
    passaros = [Passaro(TELA_LARGURA, 100)]
    obstaculos = [Obstaculo(TELA_LARGURA)]
    nuvens = [Nuvem()]
    chao = Chao()

    return homens, passaros, obstaculos, nuvens, chao, pontos


def desenhar_tela(tela, chao, homens, obstaculos, passaros, nuvens, pontos):
    if pontos >= 2500:
        IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'background2.png'))
    else:
        IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'background.png'))
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    chao.desenhar(tela)
    for nuvem in nuvens:
        nuvem.desenhar(tela)
    for passaro in passaros:
        passaro.desenhar(tela)
    texto = FONTE_PONTOS.render(f'0{pontos}', True, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    for homem in homens:
        homem.desenhar(tela)
    for vilao in obstaculos:
        vilao.desenhar(tela)
    pygame.display.update()


def desenhar_tela_game_over(tela, chao, gameover, nuvens, botao, pontos):
    if pontos >= 2500:
        IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'background2.png'))
    else:
        IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'background.png'))
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    chao.desenhar(tela)
    for nuvem in nuvens:
        nuvem.desenhar(tela)
    for go in gameover:
        go.desenhar(tela)
    texto = FONTE_PONTOS.render(f'0{pontos}', True, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    botao.desenhar(tela)
    tela.blit(IMAGEM_GAME_OVER, (TELA_LARGURA / 2 - 250, TELA_ALTURA / 2 - 350))
    pygame.display.update()


# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
DARKGREEN = (0, 100, 0)
FORESTGREEN = (34, 139, 34)
GRAY = (64, 64, 64)

# Definindo o botão para jogar

# -> Definir a posição do botão
button_x = (1280 / 2) - (200 / 2)
button_y = (720 / 2) - (50 / 2)

# -> Definir o retângulo do botão
button_rect = pygame.Rect(button_x, button_y, 200, 50)

# -> Criar o texto do botão
font = pygame.font.Font(None, 36)
text = font.render("Jogar", True, BLACK)

# Definindo o botão para ver historico de jogos

# -> Definir a posição do botão
button_x1 = (1280 / 2) - (200 / 2)
button_y1 = (1000 / 2) - (50 / 2)

# -> Definir o retângulo do botão
button_rect_hist = pygame.Rect(button_x1, button_y1, 200, 50)

# -> Criar o texto do botão
font1 = pygame.font.Font(None, 36)
text1 = font.render("Historico", True, BLACK)

pygame.init()


def main():
    # Configuração inicial
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Definindo fonte
        fonte = pygame.font.Font(None, 100)

        # Renderize o texto como uma superfície
        header_surface = fonte.render("2D - Game", True, BLACK)

        # Defina a posição da superfície
        header_x = (1280 - header_surface.get_width()) // 2
        header_y = 60

        # Defininfo a cor de fundo
        IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'background.png'))
        tela.blit(IMAGEM_BACKGROUND, (0, 0))

        # Desenhando o chão
        chao = Chao()
        chao.desenhar(tela)

        # Desenhando o homem
        homem = Homem(100, TELA_ALTURA - IMAGEM_CHAO.get_height() - IMAGEM_HOMEM[0].get_height() + 30)
        homem.desenhar(tela)

        # Desenhando o obstaculo
        obstaculo = Obstaculo(TELA_LARGURA - 300)
        obstaculo.desenhar(tela)

        # Desenhando o título na tela
        tela.blit(header_surface, (header_x, header_y))

        # Desenhando o botão na tela
        pygame.draw.rect(tela, WHITE, button_rect)
        tela.blit(text, (button_x + 60, button_y + 10))

        # Desenhando o botão na tela
        pygame.draw.rect(tela, WHITE, button_rect_hist)
        tela.blit(text1, (button_x1 + 50, button_y1 + 10))
        pygame.display.update()

        # Verificando se o botão do mouse foi pressionado
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                jogo(tela)
            elif button_rect_hist.collidepoint(mouse_pos):
                resultado = 0
                if os.path.getsize("resultado.bin") > 0:
                    with open("resultado.bin", "rb") as f:
                        resultado = pickle.load(f)
                run = True
                button = pygame.Rect(40, 660, 85, 50)
                while run:
                    for even in pygame.event.get():
                        if even.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif pygame.mouse.get_pressed()[0]:
                            mouse_pos2 = pygame.mouse.get_pos()
                            if button.collidepoint(mouse_pos2):
                                run = False  # saia do loop quando o botão "Home" é clicado

                    # Definindo fonte
                    fonte = pygame.font.Font(None, 24)

                    text3 = fonte.render("Home", True, BLACK)

                    # Definindo a tela do historico
                    # Definindo fonte
                    fonte = pygame.font.Font(None, 100)

                    # Defininfo a cor de fundo
                    IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'background.png'))
                    tela.blit(IMAGEM_BACKGROUND, (0, 0))

                    # Renderize o texto como uma superfície
                    header_surface = fonte.render("Historico", True, BLACK)

                    # Defina a posição da superfície
                    header_x = (1280 - header_surface.get_width()) // 2
                    header_y = 60

                    # Desenhando o chão
                    chao = Chao()
                    chao.desenhar(tela)

                    # Desenhando o botão na tela
                    pygame.draw.rect(tela, WHITE, button)

                    tela.blit(text3, (60, 680))

                    # Desenhe a superfície na tela
                    tela.blit(header_surface, (header_x, header_y))

                    fonte = pygame.font.Font(None, 36)

                    text2 = fonte.render(f'Recorde atual: {resultado}', True, BLACK)
                    tela.blit(text2, (button_x + 25, button_y + 30))

                    pygame.display.update()


def jogo(tela):
    botao_recomecar = Botao(TELA_LARGURA / 2 - IMAGEM_BOTAO.get_width() / 2, TELA_ALTURA / 2 + 50, IMAGEM_BOTAO)
    homens, passaros, obstaculos, nuvens, chao, pontos = resetar_jogo()
    relogio = pygame.time.Clock()
    relogio.tick(30)
    rodando = True

    while rodando:
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                for homem in homens:
                    homem.pular()

        # Movimentos
        chao.mover()
        for passaro in passaros:
            passaro.mover()
        for homem in homens:
            homem.mover()
        for obstaculo in obstaculos:
            for i, homem in enumerate(homens):
                if obstaculo.colidir(homem):
                    homens.pop(i)
                    rodando = False
                    if os.path.getsize("resultado.bin") > 0:
                        with open("resultado.bin", "rb") as f:
                            resultado = pickle.load(f)
                    else:
                        resultado = 0
                    if resultado < pontos:
                        with open("resultado.bin", "wb") as f:
                            pickle.dump(pontos, f)
                if not obstaculo.passou and homem.x > obstaculo.x:
                    obstaculo.passou = True
                    obstaculos.append(Obstaculo(TELA_LARGURA))
                    passaros.append(Passaro(TELA_LARGURA + 400, 100 + random.randint(0, 100)))
            obstaculo.mover()
            if obstaculo.x + obstaculo.imagem.get_width() < 0:
                obstaculos.remove(obstaculo)
        for nuvem in nuvens:
            nuvem.mover()
            if nuvem.x < -IMAGEM_NUVEM.get_width():
                nuvens.remove(nuvem)
                nuvens.append(Nuvem())

        # Pontuação e desenho
        pontos += 1
        desenhar_tela(tela, chao, homens, obstaculos, passaros, nuvens, pontos)

    # Tela de Game Over
    gover = [GameOver()]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and botao_recomecar.x < event.pos[
                0] < botao_recomecar.x + botao_recomecar.imagem.get_width() and botao_recomecar.y < event.pos[1] < botao_recomecar.y + botao_recomecar.imagem.get_height():
                homens, passaros, obstaculos, nuvens, chao, pontos = resetar_jogo()
                main()
        for nuvem in nuvens:
            nuvem.mover()
            if nuvem.x < -IMAGEM_NUVEM.get_width():
                nuvens.remove(nuvem)
                nuvens.append(Nuvem())
        desenhar_tela_game_over(tela, chao, gover, nuvens, botao_recomecar, pontos)


if __name__ == '__main__':
    main()
