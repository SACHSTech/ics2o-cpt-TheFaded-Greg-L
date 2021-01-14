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
size = [800, 800]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
PLAYER_X = 0
PLAYER_Y = 0
#Loop until the user clicks the close button.
DONE = False
MOVEABLE = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not DONE:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            DONE = True # Flag that we are DONE so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and MOVEABLE == True:
                PLAYER_Y = PLAYER_Y + 50
            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and MOVEABLE == True:
                PLAYER_Y = PLAYER_Y - 50
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and MOVEABLE == True:
                PLAYER_X = PLAYER_X - 50
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and MOVEABLE == True:
                PLAYER_X = PLAYER_X + 50
            print(PLAYER_X, PLAYER_Y)
    # --- Game logic should go here
 
    # --- Drawing code should go here
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, ([PLAYER_X, PLAYER_Y], [50, 50]))    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()