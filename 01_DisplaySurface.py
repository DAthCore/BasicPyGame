import pygame
#Before you must install in shell:  python3 -m pip install pygame


#Initialize pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello!!")

#THE MAIN GAME LOOP
running = True
while running:
    #Loop throught a list of Event objects that have occurred
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

#End the Game
pygame.quit()
