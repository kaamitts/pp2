import pygame
import sys
import random
import time
import psycopg2
from pygame.locals import *

connection = None

try: 
    connection = psycopg2.connect(
        host = "localhost",
        database = "lab10",
        user = "admin",
        password = "qwerty"        
    )
    connection.autocommit()
    
    #Create a table
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXIST Users
        (id serial PRIMARY KEY, nick_name VARCHAR(255))""")
        print("[INFO] Table created successfely")
    
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXIST User_scores
        (id serial PRIMARY KEY, nick_name VARCHAR(255))""")
        print("[INFO] Table created successfely")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 600, 400
FONT = pygame.font.SysFont(None, 30)

# Функция для отображения текста на экране
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Функция для отображения меню с вводом имени пользователя
def input_menu(screen):
    input_box = pygame.Rect(150, 200, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)  # Здесь можно обработать введенное имя
                        running = False
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255,255,255))
        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(screen, 'Enter your name:', FONT, (0, 0, 0), 155, 180)
        draw_text(screen, text, FONT, (0, 0, 0), input_box.x + 5, input_box.y + 5)
        pygame.display.flip()
        clock.tick(30)

# Функция для отображения главного меню
def main_menu(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    name = input_menu(screen)
                    print("Name:", name)
                    return

        screen.fill((255,255,255))
        draw_text(screen, 'Press SPACE to start', FONT, (0, 0, 0), WIDTH//2 - 100, HEIGHT//2)
        pygame.display.flip()

# Создание окна Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Запуск главного меню
main_menu(screen)

# Остальной код вашей игры
#Создание цветов
BLACK = (0,0,0)
SIZE_BLOCK = 20
WHITE = (255,255,255)
FRAME_COLOR = (100, 200, 200)
HEADER_COLOR = (70, 200, 250)
SNAKE_COLOR = (0, 102, 0)
COUNT_BLOCKS = 20
BLUE = (210,255,255)
RED = (224, 0, 0)
MARGIN = 1
HEADER_MARGIN = 70

font = pygame.font.SysFont(None, 60)
game_over = font.render("Game Over", True, BLACK)

pygame.mixer.music.load("Intelligency - August.mp3")
pygame.mixer.music.play(-1)

#Создание переменных 
size = [SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS, 
        SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS+HEADER_MARGIN]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
courier = pygame.font.SysFont("courier", 36, 1)
total_for_speed = 1

#Этот класс помогает нам с упралением и проверками границ
class SnakeBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS
    
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y
    
class Food:
    def __init__(self):
        self.position = self.random_position()
        self.spawn_time = time.time()
        self.alive_time = 10
    
    def random_position(self):
        return random_empty_block()
    
    def respawn(self):
        self.position = self.random_position()
        self.spawn_time = time.time()
        
    def is_alive(self):
        return time.time() - self.spawn_time < self.alive_time

    def draw(self):
        if self.is_alive():
            draw_block(RED, self.position.x, self.position.y)
    
    def update_position(self):
        if not self.is_alive():
            self.respawn()

    
#Эта функция нам нужна для отрисовки поля игры
def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK+column, 
        HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK+row, SIZE_BLOCK, SIZE_BLOCK])
    
#Эта функция нам нужна для отривоски еды на пустом месте в игровом поле
def random_empty_block():
    x = random.randint(0, COUNT_BLOCKS-1)
    y = random.randint(0, COUNT_BLOCKS-1)
    empty_block = SnakeBlock(x,y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS-1)
        empty_block.y = random.randint(0, COUNT_BLOCKS-1)
    return empty_block
            
snake_blocks = [SnakeBlock(9,9), SnakeBlock(9,10), SnakeBlock(9,11)] #Начальное положение змеи

food = Food()

#Эти переменные говорят нам о направлении змеи  
d_row = 0
d_col = 1
speed = 1
total = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            #Само движение
            elif event.key == K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == K_RIGHT and d_row != 0:
                d_col = 1
                d_row = 0
            elif event.key == K_LEFT and d_row != 0:
                d_col = -1
                d_row = 0
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])#Заставка сверху
    
    #Текст на заставке сверху
    text_total = courier.render(f"Total:{total}", 1, WHITE)
    text_speed = courier.render(f"Speed:{speed}", 1, WHITE)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK+230, SIZE_BLOCK))
    
    #Отрисовка поля в цвета в шахматном порядке
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row+column)%2==0:
                color = WHITE
            else:
                color = BLUE
            draw_block(color, row, column)
    
    #Проверка на нахождение змеи на поле        
    head = snake_blocks[-1]
    if not head.is_inside():
        pygame.mixer.Sound("gameover.mp3").play()  
        pygame.mixer.music.stop()    
        screen.fill(WHITE)
        screen.blit(game_over, (90,250))
        pygame.display.update()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()
    
    #Появление еды и змеи на поле
    food.draw()
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)
    
    #Удлинение нашей змеи    
    if food.position == head:
        pygame.mixer.Sound("звукеды.mp3").play()
        total_for_text = random.randint(1, 3)
        total += total_for_text
        text_plus = courier.render(f"+{total_for_text}", 1, WHITE)
        screen.blit(text_plus, (174, SIZE_BLOCK))
        speed = total_for_speed//3 +1
        snake_blocks.append(food.position)
        food.respawn()
        total_for_speed += 1
        
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    
    #Столкновение змеи с собой
    if new_head in snake_blocks:
        pygame.mixer.Sound("gameover.mp3").play()
        pygame.mixer.music.stop()
        screen.fill(WHITE)
        screen.blit(game_over, (90,250))
        pygame.display.update()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()
    
    #Добавление новой головы
    snake_blocks.append(new_head)
    
    #Удаление хвоста, чтобы змея оставалась прежней длины
    snake_blocks.pop(0)
    
    #Обновление позиции еды после 10 секунд
    food.update_position()
    
    pygame.display.update()
    clock.tick(3+speed)