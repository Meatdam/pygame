import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))  # Ширина и высота окна игры

pygame.display.set_caption("My Pygame")

rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2  # высчитываем координаты прямоугольника по ширине (по центру)
rect_y = screen_height / 2 - rect_height / 2  # Высчитываем координыта прямоугольника по высоте (по центру)

rect_color = pygame.Color('lightyellow')  # переменная цвета квадрата
fill_color = (32, 52, 71)  # переменная цвета фона

STEP = 10

while True:
    for event in pygame.event.get():  # цикл игры
        print(event)
        if event.type == pygame.QUIT:  # Выход из игры конец цикла
            sys.exit()  # Выход из приложения
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:  # Условия перемещения прямоугольника по кнопка вверх, вниз, влево, вправо
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:  # условия запрета выхода прямоугольника за границы экрана
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP

    screen.fill(fill_color)  # цвет фона
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))  # задаем координаты для премоугольника
    pygame.display.update()

    # clock.tick(1)  # скорость обновление экрана



