import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ading Sound")

#LOAD SOUND EFFECTS
sound1 = pygame.mixer.Sound('sound1.wav')
sound2 = pygame.mixer.Sound('sound2.wav')

#PLAY THE SPUND EFFECTS
sound1.play()
pygame.time.delay(2000)
sound2.play()
pygame.time.delay(2000)

#CHANGE THE VOLUME OF A SOUND EFFECT
sound2.set_volume(.1)
sound2.play()

#LOAD BACKGROUND MUSIC
pygame.mixer.music.load('music.wav')

#STOP AND STOP THE MUSIC
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

#THE MAIN LOOP GAME
runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig == False

#END THE GAME
pygame.quit()
