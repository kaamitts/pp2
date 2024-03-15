#Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
#When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 
#20 pixels in the direction of pressed key. The ball should not leave the screen, 
#i.e. user input that leads the ball to leave of the screen should be ignored

import pygame
import os
pygame.init()

screen = pygame.display.set_mode((500,500))
radius = 25
done = False
x = 250
y = 250
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - 20  >= radius:
        y -=20
    if pressed[pygame.K_DOWN]and  y + 20 <= screen.get_height() - radius:
        y += 20
    if pressed[pygame.K_LEFT] and x - 20 >= radius: 
        x -= 20
    if pressed[pygame.K_RIGHT] and x + 20 <= screen.get_width() - radius:
        x += 20
        
    screen.fill((0, 0, 0))
    color = (255, 50, 0)
    pygame.draw.circle(screen, color, (x, y), radius)
                
    pygame.display.flip()
    clock.tick(60)