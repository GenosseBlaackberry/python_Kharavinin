import pygame
from pygame.draw import *

# Создание констант
FPS = 30
BLACK = (0, 0, 0)
PEACH = (255, 185, 145)
EASY = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN_LENGTH = 1500
SCREEN_WIGHTS = 800


def window(finished=False, clock=pygame.time.Clock()):
    """
    Функция организующая процесс смены кадров и выхода из окна

    finished -- флаг завершения работы
    clock -- встроенные часы pygame
    """
    pygame.display.update()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()


def bamboo(x: int, y: int, s: int):
    """
    Функция рисует бамбук

    x -- координата по x
    y -- координата по y
    s -- увеличение (раз)
    """
    pygame.draw.line(screen, GREEN, [100 * s + x, 150 * s + y], [122 * s + x, 115 * s + y], 3 * s)
    pygame.draw.polygon(screen, GREEN, [[122 * s + x, 115 * s + y], [128 * s + x, 102 * s + y],
                                        [160 * s + x, 100 * s + y]])
    pygame.draw.polygon(screen, GREEN, [[122 * s + x, 115 * s + y], [132 * s + x, 115 * s + y],
                                        [150 * s + x, 150 * s + y]])
    pygame.draw.line(screen, GREEN, [90 * s + x, 200 * s + y], [98 * s + x, 152 * s + y], 4 * s)
    pygame.draw.line(screen, GREEN, [88 * s + x, 255 * s + y], [90 * s + x, 202 * s + y], 6 * s)
    pygame.draw.line(screen, GREEN, [93 * s + x, 202 * s + y], [130 * s + x, 180 * s + y], 4 * s)
    pygame.draw.line(screen, GREEN, [131 * s + x, 180 * s + y], [170 * s + x, 175 * s + y], 3 * s)
    pygame.draw.line(screen, GREEN, [97 * s + x, 150 * s + y], [70 * s + x, 120 * s + y], 3 * s)
    pygame.draw.polygon(screen, GREEN, [[170 * s + x, 175 * s + y], [179 * s + x, 177 * s + y],
                                        [180 * s + x, 220 * s + y]])
    pygame.draw.polygon(screen, GREEN, [[170 * s + x, 172 * s + y], [173 * s + x, 163 * s + y],
                                        [205 * s + x, 162 * s + y]])
    pygame.draw.polygon(screen, GREEN, [[155 * s + x, 178 * s + y], [165 * s + x, 180 * s + y],
                                        [162 * s + x, 219 * s + y]])
    pygame.draw.polygon(screen, GREEN, [[70 * s + x, 120 * s + y], [60 * s + x, 153 * s + y],
                                        [62 * s + x, 130 * s + y]])


def eye(x: int, y: int):
    """
    Функция рисует глаз

    x -- координата по x
    y -- координата по y
    """
    pygame.draw.ellipse(screen, EASY, [x, y, 25, 40])
    pygame.draw.ellipse(screen, BLACK, [2 + x, 5 + y, 18, 18])


def ear(x: int, y: int):
    """
    Функция рисует ухо

    x -- координата по x
    y -- координата по y
    """
    pygame.draw.circle(screen, BLACK, [x, y], 23)


def head(x: int, y: int):
    """
    Функция рисует голову

    x -- координата по x
    y -- координата по y
    """
    pygame.draw.circle(screen, WHITE, [750 + x, 400 + y], 100)
    eye(x + 708, y + 380)
    eye(x + 778, y + 380)
    ear(677 + x, 305 + y)
    ear(823 + x, 305 + y)
    pygame.draw.polygon(screen, BLACK, [[753 + x, 440 + y], [743 + x, 430 + y], [763 + x, 430 + y]])
    pygame.draw.rect(screen, RED, [740 + x, 447 + y, 30, 30], 0, border_radius=15, border_top_left_radius=0,
                     border_top_right_radius=0)


def waving_arm(x: int, y: int):
    """
    Функция рисует машущую руку

    x -- координата по x
    y -- координата по y
    """
    pygame.draw.ellipse(screen, EASY, [925 + x, 460 + y, 40, 80])
    pygame.draw.ellipse(screen, EASY, [863 + x, 510 + y, 90, 40])
    pygame.draw.circle(screen, EASY, [943 + x, 450 + y], 23)
    pygame.draw.circle(screen, EASY, [917 + x, 448 + y], 10)
    pygame.draw.circle(screen, EASY, [930 + x, 426 + y], 10)
    pygame.draw.circle(screen, EASY, [955 + x, 426 + y], 10)
    pygame.draw.circle(screen, EASY, [970 + x, 447 + y], 10)


def holding_arm(x: int, y: int):
    """
    Функция рисует руки-бамбуки

    x -- координата по x
    y -- координата по y
    """
    bamboo(605 + x, 390 + y, 1)
    pygame.draw.ellipse(screen, EASY, [600 + x, 520 + y, 40, 80])
    pygame.draw.ellipse(screen, EASY, [610 + x, 570 + y, 90, 40])
    pygame.draw.circle(screen, EASY, [702 + x, 585 + y], 23)
    pygame.draw.circle(screen, EASY, [696 + x, 563 + y], 10)


def legs(x: int, y: int):
    """
    Функция рисует ноги

    x -- координата по x
    y -- координата по y
    """
    pygame.draw.ellipse(screen, EASY, [660 + x, 700 + y, 90, 50])
    pygame.draw.ellipse(screen, EASY, [760 + x, 700 + y, 90, 50])
    pygame.draw.rect(screen, RED, [740 + x, 447 + y, 30, 30], 0, border_radius=15, border_top_left_radius=0,
                     border_top_right_radius=0)


def body(x: int, y: int):
    """
    Функция рисует тело

    x -- координата по x
    y -- координата по y
    """
    pygame.draw.ellipse(screen, WHITE, [600 + x, 450 + y, 300, 290])


def panda(x: int, y: int):
    """
    Функция рисует панду

    x -- координата по x
    y -- координата по y
    """
    head(x, y)
    body(x, y)
    holding_arm(x, y)
    waving_arm(x, y)
    legs(x, y)


def __main__():
    """
    Основная функция программы
    """
    pygame.init()

    global screen
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIGHTS))

    screen.fill(PEACH)
    panda(500, 0)
    panda(-560, 0)
    bamboo(500, 520, 1)
    bamboo(700, 230, 2)
    bamboo(200, 0, 3)
    bamboo(430, -400, 4)
    window()


__main__()
