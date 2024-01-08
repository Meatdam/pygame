import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)  # задали шрифт для нашей надписи game over в конце игры

screen_width, screen_height = 800, 600  # Размеры нешего окна игры
screen_fill_color = (32,52, 71)  # переменная цвета фона
screen = pygame.display.set_mode((screen_width, screen_height))  # Coздание игровой поверхности

pygame.display.set_caption("Awesome Shooter Game")  # Название нашей игры

FIGHTER_STEP = 1  # шаг перемещения
# загрузка и размеры нашего кораблика
fighter_image = pygame.image.load('images/fighter.png')  # загрузка нашего кораблика
fighter_width, fighter_height = fighter_image.get_size()  # высчитали размеры нашего кораблика при помощи метода get_size
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height  # задали чтобы караблик появлялся по середине экрана с низу
fighter_is_moving_left, fighter_is_moving_right = False, False
# =========================================================================
# загрузка и размеры нашей ракеты
ROCKET_STEP = 1.5   # шаг перемещения
rocket_image = pygame.image.load('images/ball.png')  # загрузка нашей ракеты
rocket_width, rocket_height = rocket_image.get_size()  # высчитали размеры нашей ракеты
rocket_x, rocket_y = 0, 0  # создание переменных нашей ракеты
rocket_was_fired = False
# ========================================================================
# инопланитянен ==============================
ALIEN_STEP = 0.05  # шаг перемещения
alien_speed = ALIEN_STEP  # скорость отпускания инопланетянина
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), 0
# =============================================
game_is_running = True

game_score = 0  # Переменная счета

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # закончить игру при нажатии на закрытие окна
# цикл перемещения каробля
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:  # меняем условие на True если ракета вылетает при нажатие на пробел
                rocket_was_fired = True
# здесь мы уже просто определяем координаты коробля после условия
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height
# ===============================================================
# Условия ниже если мы отпускаем клаоыише перемещения то значение меняем на False и кораблик останавливается
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False
# =========================================================================================================
    # Условия для самого движения кораблика с нажатой клавишей
    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:  # условия не выходить за экран
        fighter_x -= FIGHTER_STEP

    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    alien_y += alien_speed  # при поподание в инпланитяниня скорость увеличивается

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False  # задаем условие если рокета достигает верх нашего экрана игры то значение становится False

    if rocket_was_fired:  # Условие для ракеты чтобы она дваигалась по координате Y вверх
        rocket_y -= ROCKET_STEP

    screen.fill(screen_fill_color)  # цвет фона
    screen.blit(fighter_image, (fighter_x, fighter_y))  # кораблик поместили на экран по вверх всех слоев при помощи метода blit

    screen.blit(alien_image, (alien_x, alien_y))  # показываем инопланитянина

    if rocket_was_fired:  # условие по которому должна вылетать ракета, после того как нажали пробел
        screen.blit(rocket_image, (rocket_x, rocket_y))  # показываем ракету по начальным координатам

    game_score_text = game_font.render(f"Your Score is: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()  # вызов дисплея

    if alien_y + alien_height > fighter_y:  # выход из цикла конец игры
        game_is_running = False
  # условие по поподанию по инопланитянину ракетой
    if rocket_was_fired and \
            alien_x < rocket_x < alien_x + alien_width - rocket_width and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height:
        rocket_was_fired = False
   # ==============================================
        alien_x, alien_y = randint(0, screen_width - alien_width), 0  # если ракета попала, то инопланетянин возвращается на исходную позицию
        alien_speed += ALIEN_STEP / 2
        game_score += 1  # создали счет

# работа с надписью game over =============
game_over_text = game_font.render("Game Over", True, 'white')   # наша надпись
game_over_rectangle = game_over_text.get_rect()  # Прямоугольник для нашей надписи
game_over_rectangle.center = (screen_width / 2, screen_height / 2)  # координаты центра нашего прямоугольника
screen.blit(game_over_text, game_over_rectangle)  # помещаем текст в наш прямоугольник
pygame.display.update()
pygame.time.wait(5000)
# =======================================
pygame.quit()



