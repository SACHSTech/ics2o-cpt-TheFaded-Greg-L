""" 
A basic pygame template
"""
 
import pygame
import random
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
YELLOW   = ( 245, 206,  66)
DARK_GREY = ( 100, 100, 100)
LIGHT_GREY = ( 125, 125, 125)

# Define Units that the game will be displayed on per pixel.
UNIT_OF_MEASUREMENT = 50 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = [850, 850]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

WALL_POS = [15 * UNIT_OF_MEASUREMENT, 16 * UNIT_OF_MEASUREMENT]

#Loop until the user clicks the close button.
DONE = False


PLAYER_POS = [16 * UNIT_OF_MEASUREMENT, 16 * UNIT_OF_MEASUREMENT]
MOVEABLE_DOWN = True
MOVEABLE_UP = True
MOVEABLE_LEFT = True
MOVEABLE_RIGHT = True

virus = pygame.image.load("images/virus.png").convert_alpha()
virus = pygame.transform.scale(virus, (UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT))
PLAYER_MOVED = False
VIRUS_POS = [0 * UNIT_OF_MEASUREMENT, 0 * UNIT_OF_MEASUREMENT]



#if virus can move if there is nothing in its way
VIRUS_UP = True
VIRUS_DOWN =  True
VIRUS_LEFT = True
VIRUS_RIGHT = True

EXIT_POS = [1 * UNIT_OF_MEASUREMENT, 16 * UNIT_OF_MEASUREMENT]

LEVEL = 0
level_font = pygame.font.SysFont("Arial", 20, True)

heart = pygame.image.load("images/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT))
HEART_POS = [random.randint(1,16) * UNIT_OF_MEASUREMENT, random.randint(1,16) * UNIT_OF_MEASUREMENT]

LIVES = 3
lives_font = pygame.font.SysFont("Arial", 20, True)


TEST_RESTART = False

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
                PLAYER_POS[1] = PLAYER_POS[1] + UNIT_OF_MEASUREMENT
                PLAYER_MOVED = True

            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and MOVEABLE_UP == True:
                PLAYER_POS[1] = PLAYER_POS[1] - UNIT_OF_MEASUREMENT
                PLAYER_MOVED = True

            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and MOVEABLE_LEFT == True: 
                PLAYER_POS[0] = PLAYER_POS[0] - UNIT_OF_MEASUREMENT
                PLAYER_MOVED = True

            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and MOVEABLE_RIGHT == True:
                PLAYER_POS[0] = PLAYER_POS[0] + UNIT_OF_MEASUREMENT
                PLAYER_MOVED = True

    # --- Game logic should go here
    
    VIRUS_UP_POS = (sum(PLAYER_POS) - sum(VIRUS_POS) - UNIT_OF_MEASUREMENT) / UNIT_OF_MEASUREMENT
    VIRUS_DOWN_POS = (sum(PLAYER_POS) - sum(VIRUS_POS) + UNIT_OF_MEASUREMENT) / UNIT_OF_MEASUREMENT
    VIRUS_LEFT_POS = (sum(PLAYER_POS) - sum(VIRUS_POS) - UNIT_OF_MEASUREMENT) / UNIT_OF_MEASUREMENT
    VIRUS_RIGHT_POS = (sum(PLAYER_POS) - sum(VIRUS_POS) + UNIT_OF_MEASUREMENT) / UNIT_OF_MEASUREMENT


    if PLAYER_MOVED is True:
        print(PLAYER_POS[0], PLAYER_POS[1])
        """
        if VIRUS_UP is True and (VIRUS_UP_POS <= VIRUS_DOWN_POS or VIRUS_UP_POS <= VIRUS_LEFT_POS or VIRUS_UP_POS <= VIRUS_RIGHT_POS):
            VIRUS_POS[1] = VIRUS_POS[1] - UNIT_OF_MEASUREMENT
        elif VIRUS_DOWN is True and (VIRUS_DOWN_POS <= VIRUS_UP_POS or VIRUS_DOWN_POS <= VIRUS_LEFT_POS or VIRUS_DOWN_POS <= VIRUS_RIGHT_POS):  
            VIRUS_POS[1] = VIRUS_POS[1] + UNIT_OF_MEASUREMENT    
        elif VIRUS_LEFT is True and (VIRUS_LEFT_POS <= VIRUS_UP_POS or VIRUS_LEFT_POS <= VIRUS_DOWN_POS or VIRUS_LEFT_POS <= VIRUS_RIGHT_POS):         
            VIRUS_POS[0] = VIRUS_POS[0] - UNIT_OF_MEASUREMENT
        elif VIRUS_RIGHT is True and (VIRUS_RIGHT_POS <= VIRUS_UP_POS or VIRUS_RIGHT_POS <= VIRUS_DOWN_POS or VIRUS_RIGHT_POS <= VIRUS_LEFT_POS):
            VIRUS_POS[0] = VIRUS_POS[0] + UNIT_OF_MEASUREMENT    
        """
        if VIRUS_UP is True and VIRUS_POS[1] > PLAYER_POS[1]:
            VIRUS_POS[1] = VIRUS_POS[1] - UNIT_OF_MEASUREMENT

        elif VIRUS_DOWN is True and VIRUS_POS[1] < PLAYER_POS[1]:
            VIRUS_POS[1] = VIRUS_POS[1] + UNIT_OF_MEASUREMENT    

        elif VIRUS_LEFT is True and VIRUS_POS[0] > PLAYER_POS[0]:
            VIRUS_POS[0] = VIRUS_POS[0] - UNIT_OF_MEASUREMENT

        elif VIRUS_RIGHT is True and VIRUS_POS[0] < PLAYER_POS[0]:
            VIRUS_POS[0] = VIRUS_POS[0] + UNIT_OF_MEASUREMENT

        PLAYER_MOVED = False

    # Collision With Exit
    if PLAYER_POS == EXIT_POS:
        TEST_RESTART = True
        LEVEL = LEVEL + 1

    # Collision with Heart
    if PLAYER_POS == HEART_POS:
        TEST_RESTART = True
        LIVES = LIVES + 1

    # Collision with Virus[]
    if VIRUS_POS == PLAYER_POS:
        TEST_RESTART = True
        LIVES = LIVES - 1
    
# Player Collision with Wall AND Border

    #WALL
    if (PLAYER_POS[0] - 50) == WALL_POS[0] and (PLAYER_POS[1]) == WALL_POS[1]:
        MOVEABLE_LEFT = False
    elif (PLAYER_POS[0] + 50) == WALL_POS[0] and (PLAYER_POS[1]) == WALL_POS[1]:
        MOVEABLE_RIGHT = False
    elif (PLAYER_POS[0]) == WALL_POS[0] and (PLAYER_POS[1] - 50)== WALL_POS[1]:
        MOVEABLE_UP = False
    elif (PLAYER_POS[0]) == WALL_POS[0] and (PLAYER_POS[1] + 50) == WALL_POS[1]:
        MOVEABLE_DOWN = False 
    #BORDER 
    if (PLAYER_POS[0]) == 0:
        MOVEABLE_LEFT = False
    elif (PLAYER_POS[0] + 50) == size[0]:
        MOVEABLE_RIGHT = False
    if (PLAYER_POS[1]) == 0:
        MOVEABLE_UP = False
    elif (PLAYER_POS[1] + 50) == size[1]:
        MOVEABLE_DOWN = False
    else:
        MOVEABLE_UP = True
        MOVEABLE_DOWN = True
        MOVEABLE_LEFT = True
            MOVEABLE_RIGHT = True



                
    #Check if testing restart
    if TEST_RESTART is True:
        HEART_POS = [random.randint(1,16) * UNIT_OF_MEASUREMENT, random.randint(1,16) * UNIT_OF_MEASUREMENT]
        PLAYER_POS = [16 * UNIT_OF_MEASUREMENT, 16 * UNIT_OF_MEASUREMENT]
        VIRUS_POS = [0 * UNIT_OF_MEASUREMENT, 0 * UNIT_OF_MEASUREMENT]
        TEST_RESTART = False


    # --- Drawing code should go here
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw exit goal
    pygame.draw.rect(screen, YELLOW, (EXIT_POS, [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]))
    pygame.draw.rect(screen, LIGHT_GREY, (EXIT_POS, [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 2)
    # Draw heart
    screen.blit(heart, (HEART_POS))

    # Draw player
    pygame.draw.rect(screen, RED, (PLAYER_POS, [UNIT_OF_MEASUREMENT,UNIT_OF_MEASUREMENT]))
    pygame.draw.rect(screen, LIGHT_GREY, (PLAYER_POS, [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 2)
    
    # Draw virus
    screen.blit(virus, (VIRUS_POS))    

    # Draw Wall
    pygame.draw.rect(screen, DARK_GREY, (WALL_POS, [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]))
    pygame.draw.rect(screen, LIGHT_GREY, (WALL_POS, [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 4)

    # Draw the current amount of lives
    lives_text = lives_font.render("LIVES: " + str(LIVES), True, BLACK)
    screen.blit(lives_text, (750, 0))

    # Draw the current level
    level_text = level_font.render("LEVEL: " + str(LEVEL), True, BLACK)
    screen.blit(level_text, (750, 30))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()