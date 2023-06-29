import pygame

#Initialize pygame
pygame.init()

#CREATE A DISPLAY SURFACE
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

#CREATE IMAGES... RETURNS A SURFACE OBJECT WITH THE IMAGE DRAW ON IT.
#WE CAN THEN GET THE RECT OF TH SURFACE AND USE THE RECT TO POSITION THE IMAGE.
ghost_left_image = pygame.image.load("ghost_left.png")
ghost_left_rect = ghost_left_image.get_rect()
ghost_left_rect.topleft = (0,0)

ghost_right_image = pygame.image.load("ghost_right.png")
ghost_right_rect = ghost_right_image.get_rect()
ghost_right_rect.topright = (WINDOW_WIDTH,0)


#THE MAIN GAME LOOP
runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig == False
            
            
    #BLIT (COPY) A SURFACE OBJECT AT THE GIVEN COORDINATES TO OUR DISPLAY
    display_surface.blit(ghost_left_image, ghost_left_rect)
    display_surface.blit(ghost_right_image, ghost_right_rect)
    
    pygame.draw.line(display_surface, (255,255, 255), (0,75), (WINDOW_WIDTH,75),4)
    
    #UPDATE THE DISPLAY 
    pygame.display.update()
            
#END OF GAME
pygame.quit() 
