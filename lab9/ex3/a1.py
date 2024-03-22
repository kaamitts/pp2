import pygame
from pygame.locals import *

pygame.init()

# Создание окна
screen = pygame.display.set_mode((1080, 800))
clock = pygame.time.Clock()

# Создание переменных
radius = 10
done = False

# Создание цветов заранее для удобства
colors = {"RED": (230, 0, 0), "GREEN": (0, 230, 0), "BLUE": (0, 0, 230)}
color = (255, 255, 255)  # Белый цвет по умолчанию

# Загрузка ластика
eraser = pygame.image.load("eraser.png")
eraser = pygame.transform.scale(eraser, (70, 70))

# Функция рисования квадратов цветов и кнопки ластика
def draw_color_buttons():
    for i, (color_name, color_value) in enumerate(colors.items()):
        pygame.draw.rect(screen, color_value, (i * 40, 0, 40, 40))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 40, 60), 4)  # Белый
    pygame.draw.rect(screen, (255, 255, 255), (40, 0, 40, 40), 4)  # Ластика

# Функция выбора цвета
def color_pick(x, y):
    for i, (color_name, color_value) in enumerate(colors.items()):
        if i * 40 < x < (i + 1) * 40 and 0 < y < 40:
            return color_value
    if 0 < x < 40 and 0 < y < 60:
        return (255, 255, 255)  # Белый
    if 40 < x < 80 and 0 < y < 40:
        return "eraser"
    return color

# Функция рисования фигур
def draw_shape(shape, x, y):
    if shape == "circle":
        pygame.draw.circle(screen, color, (x, y), 20, 4)
    elif shape == "rect":
        pygame.draw.rect(screen, color, (x, y, 40, 60), 4)
    elif shape == "square":
        pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
    elif shape == "right triangle":
        pygame.draw.polygon(screen, color, [(x, y), (x + 40, y), (x, y + 60)], 4)
    elif shape == "equilateral triangle":
        pygame.draw.polygon(screen, color, [(x + 20, y), (x, y + 40), (x + 40, y + 40)], 4)
    elif shape == "rhombus":
        pygame.draw.polygon(screen, color, [(x, y + 30), (x + 20, y), (x + 40, y + 30), (x + 20, y + 60)], 4)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            color = color_pick(x, y)

    # Отрисовка квадратов цветов и кнопки ластика
    draw_color_buttons()

    # Выбор фигуры для рисования и ее отрисовка
    keys = pygame.key.get_pressed()
    if keys[K_r]:
        draw_shape("rect", x, y)
    elif keys[K_c]:
        draw_shape("circle", x, y)
    elif keys[K_s]:
        draw_shape("square", x, y)
    elif keys[K_t]:
        draw_shape("right triangle", x, y)
    elif keys[K_e]:
        draw_shape("equilateral triangle", x, y)
    elif keys[K_h]:
        draw_shape("rhombus", x, y)
    elif color == "eraser":
        screen.blit(eraser, (0, 0))
    else:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()