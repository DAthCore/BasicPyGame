import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text")

#DEFINE COLOURS
GREEN = (0,255,0)
RED = (255, 50, 10)
BLACK = (0,0,0)

#SEE ALL AVAILABLE SYSTEM FONTS
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)
    
    
#DEFINE FONTS
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('Heartless.ttf', 64)
custom_font2 = pygame.font.Font('Insomnia.ttf', 32)

#DEFINE TEXT
system_text = system_font.render("Ghosts Rules!", True, RED)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render('Move The Ghost Soon', True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

custom_text2 = custom_font2.render('Ghosts Rules', True, GREEN)
custom_text_rect2 = custom_text2.get_rect()
custom_text_rect2.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

#THE MAIN GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #BLIT THE TEXT SURFACES TO THE DISPLAY SURFACE
    #display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)        
    display_surface.blit(custom_text2, custom_text_rect2)           
            
    #UPDATE THE DISPLAY         
    pygame.display.update()
    
#END OF GAME
pygame.quit()


