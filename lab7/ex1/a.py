import pygame
import datetime

pygame.init()
W, H = 800, 800
x = W // 2
y = H // 2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
mickey = pygame.image.load("mainclock1.png")
leftHand = pygame.image.load("leftarm.png")
rightHand = pygame.image.load("rightarm1.png")
mickeyRect = mickey.get_rect()

def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    surf.blit(rotated_image, new_rect)

while True:
    sc.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    current_time = datetime.datetime.now()
    hour_angle = -(current_time.minute * 6)  # Угол для часовой стрелки (зависит от минут)
    minute_angle = -(current_time.second * 6)  # Угол для минутной стрелки (зависит от секунд)

    sc.fill(WHITE)
    sc.blit(mickey, (0, 0))
    blitRotateCenter(sc, leftHand, (x, y), minute_angle)
    blitRotateCenter(sc, rightHand, (x, y), hour_angle)

    pygame.display.update()
    clock.tick(60)