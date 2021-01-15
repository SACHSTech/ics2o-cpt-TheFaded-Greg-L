""" 
A basic pygame template
"""
 
import pygame
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = [850, 850]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
PLAYER_POS = [800, 800]
#Loop until the user clicks the close button.
DONE = False

MOVEABLE_DOWN = True
MOVEABLE_UP = True
MOVEABLE_LEFT = True
MOVEABLE_RIGHT = True

virus = pygame.image.load("virus.png").convert_alpha()
virus = pygame.transform.scale(virus, (50, 50))
PLAYER_MOVED = False
VIRUS_POS = [0,0]
#if virus can move if there is nothing in its way
VIRUS_UP = True
VIRUS_DOWN =  True
VIRUS_LEFT = True
VIRUS_RIGHT = True



LIVES = 3

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not DONE:

    # --- Main event loop
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            DONE = True # Flag that we are DONE so we exit this loop

        elif event.type == pygame.KEYDOWN:

            if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and MOVEABLE_DOWN == True:
                PLAYER_POS[1] = PLAYER_POS[1] + 50
                PLAYER_MOVED = True

            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and MOVEABLE_UP == True:
                PLAYER_POS[1] = PLAYER_POS[1] - 50
                PLAYER_MOVED = True

            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and MOVEABLE_LEFT == True: 
                PLAYER_POS[0] = PLAYER_POS[0] - 50
                PLAYER_MOVED = True

            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and MOVEABLE_RIGHT == True:
                PLAYER_POS[0] = PLAYER_POS[0] + 50
                PLAYER_MOVED = True

    # --- Game logic should go here
    
    if PLAYER_MOVED is True:

        if VIRUS_UP is True and VIRUS_POS[1] > PLAYER_POS[1]:
            VIRUS_POS[1] = VIRUS_POS[1] - 50

        elif VIRUS_DOWN is True and VIRUS_POS[1] < PLAYER_POS[1]:
            VIRUS_POS[1] = VIRUS_POS[1] + 50    

        elif VIRUS_LEFT is True and VIRUS_POS[0] > PLAYER_POS[0] :
            VIRUS_POS[0] = VIRUS_POS[0] - 50

        elif VIRUS_RIGHT is True and VIRUS_POS[0] < PLAYER_POS[0]:
            VIRUS_POS[0] = VIRUS_POS[0] + 50

        PLAYER_MOVED = False

    #Check If Player Gets Caught By Virus
    if VIRUS_POS == PLAYER_POS:
        VIRUS_POS = [0, 0]
        PLAYER_POS = [800, 800]
        LIVES = LIVES - 1

    # --- Drawing code should go here
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (PLAYER_POS, [50, 50]))
    screen.blit(virus, (VIRUS_POS))    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()