import pygame, os, time

pygame.init()
screen = pygame.display.set_mode((830, 800))
done = False
x = 200
y = 200
clock = pygame.time.Clock()
angle = 20
_image_librery = {}
def get_image(path):
    global _image_librery
    image =_image_librery.get(path)
    if image == None:
        canon_path = path.replace("\\", os.sep)
        image = pygame.image.load(canon_path)
        _image_librery[path] = image
    return image

"""_image_librery1 = {}
def get_image(path):
    global _image_librery1
    image =_image_librery1.get(path)
    if image == None:
        canon_path = path.replace("\\", os.sep)
        image = pygame.image.load(canon_path)
        _image_librery1[path] = image
    return image"""

current_time = time.localtime()
minutes = current_time.tm_min
seconds = current_time.tm_sec

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))     
    original_image = get_image("mainclock1.png")
    #scaled_image = pygame.transform.scale(original_image, (600, 600))  # Change size here
    screen.blit((original_image), (0, 0)) 
    original_image1 = get_image("leftarm.png")
    #scaled_image1 = pygame.transform.scale(original_image1, (100, 100))  # Change size here
    screen.blit(original_image1, (394, -85)) 
    pygame.display.flip()
    clock.tick(60)