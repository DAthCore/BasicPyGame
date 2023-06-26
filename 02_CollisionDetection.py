import pygame, random
#Before you must install in shell:  python3 -m pip install pygame


#Initialize pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection!!")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Set Game Values
VELOCITY = 5

#Load Images
ghost_image = pygame.image.load("ghost_right.png")
ghost_rect = ghost_image.get_rect()
ghost_rect.topleft = (25, 25)

goal_image = pygame.image.load("goal.png")
goal_rect = goal_image.get_rect()
goal_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

#THE MAIN GAME LOOP
running = True
while running:
    #Loop throught a list of Event objects that have occurred
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
                   
    #Get a List of All Kys Currently Being Pressed Down
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and ghost_rect.left > 0:
        ghost_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and ghost_rect.right < WINDOW_WIDTH:
        ghost_rect.x += VELOCITY
    if keys[pygame.K_UP] and ghost_rect.top > 0:
        ghost_rect.y -= VELOCITY    
    if keys[pygame.K_DOWN] and ghost_rect.bottom < WINDOW_HEIGHT:
        ghost_rect.y += VELOCITY  
        
        
    #Chech For collision Between Two Reacts
    if ghost_rect.colliderect(goal_rect):
        print("Hit")
        goal_rect.x = random.randint(0, WINDOW_WIDTH -32)
        goal_rect.y = random.randint(0, WINDOW_HEIGHT - 32)
        
    #Fill Display Surface
    display_surface.fill((0, 0, 0))
    
    #Draw Rectangles to Represent The Rect's of Each Object
    pygame.draw.rect(display_surface, (0, 255, 0), ghost_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), goal_rect, 1)
    
    #Blit Assets
    display_surface.blit(ghost_image, ghost_rect)
    display_surface.blit(goal_image, goal_rect)
    
    #Update Display
    pygame.display.update()
    
    #Tic The Clock
    clock.tick(FPS)

#End the Game
pygame.quit()
