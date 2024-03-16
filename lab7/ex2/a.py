#Create music player with keyboard controller. You have to be able to press keyboard: 
#play, stop, next and previous as some keys. Player has to react to the given command appropriately.
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
playing = False
done = False
clock = pygame.time.Clock()

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]  # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]  # move current song to the front of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

_songs = ['Jah Khalib – Искал-Нашёл.mp3', 'Jah Khalib – Сжигая дотла.mp3', 'Jah Khalib – Твои сонные глаза.mp3']
SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('Jah Khalib – Искал-Нашёл.mp3')

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()
            elif event.key == pygame.K_p:  # Нажатие клавиши 'p' для запуска музыки
                pygame.mixer.music.play()
                playing = True
                
        if event.type == SONG_END:
            print("the song ended!")
            play_next_song() 
            
    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()