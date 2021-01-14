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
 
PLAYER_POS = [0, 0]
#Loop until the user clicks the close button.
DONE = False
MOVEABLE_DOWN = True
MOVEABLE_UP = True
MOVEABLE_LEFT = True
MOVEABLE_RIGHT = True

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
            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and MOVEABLE_UP == True:
                PLAYER_POS[1] = PLAYER_POS[1] - 50
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and MOVEABLE_LEFT == True:
                PLAYER_POS[0] = PLAYER_POS[0] - 50
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and MOVEABLE_RIGHT == True:
                PLAYER_POS[0] = PLAYER_POS[0] + 50
            print(PLAYER_POS[0], PLAYER_POS[1])
    # --- Game logic should go here
 
    # --- Drawing code should go here
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (PLAYER_POS, [50, 50]))    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()