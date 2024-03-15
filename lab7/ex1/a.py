import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode((830, 800))
done = False
clock = pygame.time.Clock()

# Функция загрузки изображений
def get_image(path):
    canonical_path = path.replace("\\", os.sep)
    return pygame.image.load(canonical_path)

# Загрузка изображений для часов и рук Микки
clock_image = get_image("mainclock1.png")
left_arm_image = get_image("leftarm.png")
right_arm_image = get_image("rightarm.png")

# Главный цикл приложения
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Очистка экрана
    screen.fill((255,255,255)) 
    
    # Отображение часов на экране
    screen.blit(clock_image, (0, 0))
    
    # Получение текущего времени
    current_time = time.localtime()
    minutes_angle = current_time.tm_min * 6  # 360 градусов / 60 минут = 6 градусов на минуту
    seconds_angle = current_time.tm_sec * 6  # 360 градусов / 60 секунд = 6 градусов на секунду
    
    # Поворот правой руки Микки в зависимости от минут
    rotated_right_arm = pygame.transform.rotate(right_arm_image, -minutes_angle)
    screen.blit(rotated_right_arm, (394, -85))
    
    # Поворот левой руки Микки в зависимости от секунд
    rotated_left_arm = pygame.transform.rotate(left_arm_image, -seconds_angle)
    screen.blit(rotated_left_arm, (394, -85))
    
    # Обновление экрана
    pygame.display.flip()
    
    # Ограничение частоты кадров
    clock.tick(60)