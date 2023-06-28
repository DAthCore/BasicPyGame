import pygame

#Initialize pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#DEFINE COLORS AS RGB TUPLES
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

#GIVE A BACKGROUND COLOR TO  THE DISPLAY
display_surface.fill(BLUE)

#DRAWN A VARIOUS SHAPES ON OUR DISPLAY
#Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 1)

#CIRCLE(surface, color, center, radius, thickness... 0 for fill)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6) 
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0) 

#Rectangle(surface, color, (top-left x, top-left y, width, height)
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100)) 
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100)) 

#THE MAIN GAME LOOP
running = True
while running:
    #Loop throught a list of Event objects that have occurred
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
            
    #UPDATE THE DISPLAY
    pygame.display.update()

#End the Game
pygame.quit()