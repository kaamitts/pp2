import pygame
import os

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        print(path)
        canonicalized_path = path.replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
    screen.fill((255, 255, 255))
        
    screen.blit(get_image('ex3/ball.png'), (60, 60))
        
    pygame.display.flip()
    clock.tick(60)