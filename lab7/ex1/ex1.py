import pygame
import datetime
pygame.init()
W, H = 800, 800
x = W//2
y = H//2 
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
mickey = pygame.image.load("mainclock1.png")
rightarm = pygame.image.load('rightarm1.png')
leftarm = pygame.image.load("leftarm.png")

def BlitRotateCenter(surf, image, center, angle):
    rotate_image = pygame.transform.rotate(image, angle)
    new_rect = rotate_image.get_rect(center = image.get_rect(center=center).center)
    surf.blit(rotate_image, new_rect)

while True:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
    current_time = datetime.datetime.now()
    minute_angle = -(current_time.minute * 6)
    second_angle = -(current_time.second * 6)
    
    screen.fill(WHITE)
    screen.blit(mickey, (0,0))
    BlitRotateCenter(screen, rightarm, (x,y), minute_angle)
    BlitRotateCenter(screen, leftarm, (x,y), second_angle)
    
    
    pygame.display.update()
    clock.tick(60)