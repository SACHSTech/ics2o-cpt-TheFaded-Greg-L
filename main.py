import pygame
import time
# Define some colors
BLACK             = (   0,   0,   0)
WHITE             = ( 255, 255, 255)
OFF_WHITE         = ( 230, 230, 230)
GREEN             = (   0, 255,   0)
RED               = ( 255,   0,   0)
BLUE              = (   0,   0, 255)
DARK_RED          = ( 191,   4,   4)
YELLOW            = ( 245, 206,  66)
DARK_GREY         = ( 100, 100, 100)
REALLY_DARK_GREY  = (  50,  50,  50)
LIGHT_GREY        = ( 125, 125, 125)
BACKGROUND_COLOUR = ( 200, 200, 200)

# Define Units that the game will be displayed on per pixel.
UNIT_OF_MEASUREMENT = 50 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = [800, 800]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Escape-ware")


#Loop until the user clicks the close button.
DONE = False

WALL_POS = [0, 1]

PLAYER_POS = [15, 8]
MOVEABLE_DOWN = True
MOVEABLE_UP = True
MOVEABLE_LEFT = True
MOVEABLE_RIGHT = True
PLAYER_MOVED = False
GOAL_TRIGGERED = False

virus = pygame.image.load("images/virus.png").convert_alpha()
virus = pygame.transform.scale(virus, (UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT))
VIRUS_POS = [0 , 0 ]
VIRUS_TRIGGERED = False
#if virus can move if there is nothing in its way
VIRUS_UP = True
VIRUS_DOWN =  True
VIRUS_LEFT = True
VIRUS_RIGHT = True

EXIT_POS = [0, 0]

LEVEL = 1

LEVEL_ONE = [
"vooooxxxxxxxoooo", 
"xxxoooooxooooxxo", 
"ohxoxxxoxoxxoxxo", 
"oxxoxoxoooxoooxo",
"ooooxoxoxoxoxoxo",
"oxxoxoxoxoxoooxo",
"ooooxoxoooxxoxxo",
"xxxxxoxxoxxxoxxo",
"xexoooxooxxxoxxp",
"xoxxxxxoxxxxoxxx",
"xoxoooxoxxxxoxxx",
"xoooxooooxxxoxhx",
"xxxoxoxxoooooxox",
"xoxoxoxxxxxxxxox",
"xoooxoooooooooox",
"xxxxxxxxxxxxxxxx"
            ]
LEVEL_ONE_PLAYER = [15, 8]
LEVEL_ONE_VIRUS = [0, 0]

LEVEL_TWO = [
"xxxxxxxxxxxxxxxx",
"xexoxooxxooxoxvx",
"xoxoxooxxooxoxox",
"xooooooxxoooooox",
"xoxoxooxxooxoxox",
"xooooooxxoooooox",
"xoxoxooxxooxoxox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoxoxooxxooxoxox",
"xooooooxxoooooox",
"xoxoxooxxooxoxox",
"xooooooxxoooooox",
"xoxoxooxxooxoxox",
"xhxoxooxxooxoxpx",
"xxxxxxxxxxxxxxxx",
            ]
LEVEL_TWO_PLAYER = [14, 14]
LEVEL_TWO_VIRUS = [14, 1]

LEVEL_THREE = [
"oooooxxooooohxoo",
"xxoxxxxooxxxxxoo",
"ooooxooooooooooo",
"oxxxxoooxxoooooo",
"ooooxxooxxoooooo",
"oxooexooxxooxxxo",
"oxxxxxooxxooxooo",
"ooxxooooxxooxooo",
"oooxoooxxxooxxxo",
"oxoooooxxxooooxo",
"oxoxooooxxoooooo",
"oxxxoxooxxooxxoo",
"oxhxoxooxxooxpxo",
"oxoooxooooooxooo",
"oxxxxxxxxxxoxxxo",
"oooooooooooooooo",
            ]
LEVEL_THREE_PLAYER = [13, 12]
LEVEL_THREE_VIRUS = [0, 0]

LEVEL_FOUR = [
"xxxxxxxxxxxxxxxx",
"xoooooooooooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxpooooox",
"xooooovxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xoooooooooooooox",
"xxxxxxxxxxxxxxxx",
            ]
LEVEL_FOUR_PLAYER = [15, 8]
LEVEL_FOUR_VIRUS = [0, 0]

LEVEL_FIVE = [
"xxxxxxxxxxxxxxxx",
"xoooooooooooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxpooooox",
"xooooovxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xooooooxxoooooox",
"xoooooooooooooox",
"xxxxxxxxxxxxxxxx",
            ]
LEVEL_FIVE_PLAYER = [15, 8]
LEVEL_FIVE_VIRUS = [0, 0]






"""
DESIGN YOUR OWN LEVEL!
type in the desired letters to place walls, the heart and the exit!
x = wall
h = heart
e = exit

For Player and Virus Location Change the two Variables below, LEVEL_SIX_PLAYER and LEVEL_SIX_VIRUS
"""
LEVEL_SIX = [
"xxxxxxxxxxxxxxxx",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xoooooooooooooox",
"xxxxxxxxxxxxxxxx",
            ]

LEVEL_SIX_PLAYER = [15, 8]
LEVEL_SIX_VIRUS = [0, 0]







CURRENT_POS = LEVEL_ONE_PLAYER
CURRENT_VIRUS_POS = LEVEL_ONE_VIRUS
CURRENT_LEVEL = LEVEL_ONE
level_font = pygame.font.SysFont("Arial", 20, True)


SCENE = 0
MENU_SCENE = 1

#TITLE
TITLE_FONT = pygame.font.SysFont("Bauhaus 93", 200, False, False)
TITLE_TEXT_1 = TITLE_FONT.render("ESCAPE", True, BLACK)
TITLE_TEXT_2 = TITLE_FONT.render("-WARE", True, BLACK)

#BACK BUTTOM
BACK_BUTTON_POS = [675, 25]
BACK_BUTTON_SIZE = [100, 50]
BACK_BUTTON_COLOUR = DARK_RED
BACK_BUTTON_TEXT_COLOUR = OFF_WHITE
BACK_BUTTON_FONT = pygame.font.SysFont("Aharoni", 40, False, False)
BACK_BUTTON_TEXT = BACK_BUTTON_FONT.render("BACK", True, BACK_BUTTON_TEXT_COLOUR)

#START BUTTON
START_BUTTON_POS = [150, 430]
START_BUTTON_SIZE = [250, 100]
START_BUTTON_COLOUR = DARK_RED
START_BUTTON_TEXT_COLOUR = OFF_WHITE
START_BUTTON_FONT = pygame.font.SysFont("Aharoni", 60, False, False)
START_BUTTON_TEXT = START_BUTTON_FONT.render("START", True, START_BUTTON_TEXT_COLOUR)

#HELP MENU
HELP_BUTTON_POS = [500, 550]
HELP_BUTTON_SIZE = [250, 100]
HELP_BUTTON_COLOUR = DARK_RED
HELP_BUTTON_TEXT_COLOUR = OFF_WHITE
HELP_BUTTON_FONT = pygame.font.SysFont("Aharoni", 60, False, False)
HELP_BUTTON_TEXT = HELP_BUTTON_FONT.render("HELP", True, HELP_BUTTON_TEXT_COLOUR)

HELP_FONT = pygame.font.SysFont("Arial", 30, True)
HELP_KEY_TEXT_W = HELP_FONT.render("W", True, BLACK)
HELP_KEY_TEXT_A = HELP_FONT.render("A", True, BLACK)
HELP_KEY_TEXT_S = HELP_FONT.render("S", True, BLACK)
HELP_KEY_TEXT_D = HELP_FONT.render("D", True, BLACK)
KEY_LOCATION_X = 550
KEY_LOCATION_Y = 325

HELP_TEXT_1 = HELP_FONT.render("Use  W  A  S  D  To  Move", True, BLACK)
HELP_TEXT_2 = HELP_FONT.render("Or The Arrow Keys", True, BLACK)
HELP_TEXT_3 = HELP_FONT.render("The Virus Will Move When You Move.", True, BLACK)
HELP_TEXT_4 = HELP_FONT.render("Reach The Goal First Before", True, BLACK)
HELP_TEXT_5 = HELP_FONT.render("The Virus Catches You!", True, BLACK)

HELP_TEXT_6 = HELP_FONT.render("This Is You --->", True, BLACK)

HELP_TITLE_FONT = pygame.font.SysFont("Bauhaus 93", 120)
HELP_TITLE_1 = HELP_TITLE_FONT.render("HOW TO", True, DARK_RED)
HELP_TITLE_2 = HELP_TITLE_FONT.render("PLAY", True, DARK_RED)

#COLOUR SELECTION MENU 
COLOUR_SELECTION_BUTTON_POS = [100, 650]
COLOUR_SELECTION_BUTTON_SIZE = [250, 100]
COLOUR_SELECTION_BUTTON_COLOUR = RED
CS_BUTTION_TEXT_COLOUR = OFF_WHITE
COLOUR_SELECTION_BUTTON_FONT = pygame.font.SysFont("Aharoni", 60, False, False)
COLOUR_SELECTION_BUTTON_TEXT_1 = COLOUR_SELECTION_BUTTON_FONT.render("CHANGE", True, CS_BUTTION_TEXT_COLOUR)
COLOUR_SELECTION_BUTTON_TEXT_2 = COLOUR_SELECTION_BUTTON_FONT.render("COLOUR", True, CS_BUTTION_TEXT_COLOUR)

COLOUR_SELECTION_FONT = pygame.font.SysFont("Bauhaus 93", 120)
COLOUR_SELECTION_TEXT_1 = COLOUR_SELECTION_FONT.render("Choose", True, DARK_RED)
COLOUR_SELECTION_TEXT_2 = COLOUR_SELECTION_FONT.render("a Colour:", True, DARK_RED)
COLOUR_SELECTION_ARROW = COLOUR_SELECTION_FONT.render("^", True, DARK_RED)

RED_COLOUR = [25, 400]
YELLOW_COLOUR = [150,400]
GREEN_COLOUR = [275, 400]
BLUE_COLOUR = [425, 400]
BLACK_COLOUR = [550, 400]
WHITE_COLOUR = [675, 400]

COLOUR_SELECTION_ARROW_POS = [RED_COLOUR[0] + 20, 475]

help_virus = pygame.image.load("images/virus.png").convert_alpha()
help_virus = pygame.transform.scale(help_virus, (UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT))

PLAYER_COLOUR_PRIMARY = RED
PLAYER_COLOUR_SECONDARY = LIGHT_GREY

heart = pygame.image.load("images/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT))
HEART_POS = [0, 0]
HEART_TRIGGERED = False

LIVES = 3
lives_font = pygame.font.SysFont("Arial", 20, True)


TEST_RESTART = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not DONE:
    MOUSE_POS = pygame.mouse.get_pos()
    screen.fill(BACKGROUND_COLOUR)
    # --- Main event loop   
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            DONE = True # Flag that we are DONE so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(CURRENT_POS, CURRENT_VIRUS_POS)
            #Menu
            if SCENE == 0 and MENU_SCENE == 1:

                #Start Button
                if MOUSE_POS[0] > START_BUTTON_POS[0] and MOUSE_POS[0] < START_BUTTON_POS[0] + START_BUTTON_SIZE[0] and MOUSE_POS[1] > START_BUTTON_POS[1] and MOUSE_POS[1] < START_BUTTON_POS[1] + START_BUTTON_SIZE[1]:
                    SCENE = 1

                #Help Button
                elif MOUSE_POS[0] > HELP_BUTTON_POS[0] and MOUSE_POS[0] < HELP_BUTTON_POS[0] + HELP_BUTTON_SIZE[0] and MOUSE_POS[1] > HELP_BUTTON_POS[1] and MOUSE_POS[1] < HELP_BUTTON_POS[1] + HELP_BUTTON_SIZE[1]:
                    MENU_SCENE = 2

                #Colour Selection
                elif MOUSE_POS[0] > COLOUR_SELECTION_BUTTON_POS[0] and MOUSE_POS[0] < COLOUR_SELECTION_BUTTON_POS[0] + COLOUR_SELECTION_BUTTON_SIZE[0] and MOUSE_POS[1] > COLOUR_SELECTION_BUTTON_POS[1] and MOUSE_POS[1] < COLOUR_SELECTION_BUTTON_POS[1] + COLOUR_SELECTION_BUTTON_SIZE[1]:
                    MENU_SCENE = 3

                #Go Back Button
            elif SCENE == 0 and MENU_SCENE != 1:
                if MOUSE_POS[0] > BACK_BUTTON_POS[0] and MOUSE_POS[0] < BACK_BUTTON_POS[0] + BACK_BUTTON_SIZE[0] and MOUSE_POS[1] > BACK_BUTTON_POS[1] and MOUSE_POS[1] < BACK_BUTTON_POS[1] + BACK_BUTTON_SIZE[1]:
                    MENU_SCENE = 1

            if SCENE == 0 and MENU_SCENE == 3:
                if MOUSE_POS[0] > RED_COLOUR[0] and MOUSE_POS[0] < RED_COLOUR[0] + 100 and MOUSE_POS[1] > RED_COLOUR[1] and MOUSE_POS[1] < RED_COLOUR[1] + 100:
                    PLAYER_COLOUR_PRIMARY = RED
                    PLAYER_COLOUR_SECONDARY = LIGHT_GREY
                    COLOUR_SELECTION_ARROW_POS[0] = RED_COLOUR[0] + 20

                if MOUSE_POS[0] > YELLOW_COLOUR[0] and MOUSE_POS[0] < YELLOW_COLOUR[0] + 100 and MOUSE_POS[1] > YELLOW_COLOUR[1] and MOUSE_POS[1] < YELLOW_COLOUR[1] + 100:
                    PLAYER_COLOUR_PRIMARY = YELLOW
                    PLAYER_COLOUR_SECONDARY = BLACK
                    COLOUR_SELECTION_ARROW_POS[0] = YELLOW_COLOUR[0] + 20

                if MOUSE_POS[0] > GREEN_COLOUR[0] and MOUSE_POS[0] < GREEN_COLOUR[0] + 100 and MOUSE_POS[1] > GREEN_COLOUR[1] and MOUSE_POS[1] < GREEN_COLOUR[1] + 100:
                    PLAYER_COLOUR_PRIMARY = GREEN
                    PLAYER_COLOUR_SECONDARY = BLACK
                    COLOUR_SELECTION_ARROW_POS[0] = GREEN_COLOUR[0] + 20

                if MOUSE_POS[0] > BLUE_COLOUR[0] and MOUSE_POS[0] < BLUE_COLOUR[0] + 100 and MOUSE_POS[1] > BLUE_COLOUR[1] and MOUSE_POS[1] < BLUE_COLOUR[1] + 100:
                    PLAYER_COLOUR_PRIMARY = BLUE
                    PLAYER_COLOUR_SECONDARY = BLACK
                    COLOUR_SELECTION_ARROW_POS[0] = BLUE_COLOUR[0] + 20

                if MOUSE_POS[0] > BLACK_COLOUR[0] and MOUSE_POS[0] < BLACK_COLOUR[0] + 100 and MOUSE_POS[1] > BLACK_COLOUR[1] and MOUSE_POS[1] < BLACK_COLOUR[1] + 100:
                    PLAYER_COLOUR_PRIMARY = BLACK
                    PLAYER_COLOUR_SECONDARY = WHITE
                    COLOUR_SELECTION_ARROW_POS[0] = BLACK_COLOUR[0] + 20

                if MOUSE_POS[0] > WHITE_COLOUR[0] and MOUSE_POS[0] < WHITE_COLOUR[0] + 100 and MOUSE_POS[1] > WHITE_COLOUR[1] and MOUSE_POS[1] < WHITE_COLOUR[1] + 100:
                    PLAYER_COLOUR_PRIMARY = WHITE
                    PLAYER_COLOUR_SECONDARY = BLACK    
                    COLOUR_SELECTION_ARROW_POS[0] = WHITE_COLOUR[0] + 20

        elif event.type == pygame.KEYDOWN:

            #Always go back to main menu
            if event.key == pygame.K_ESCAPE:
                SCENE = 0
                MENU_SCENE = 1
            if SCENE != 0:
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and MOVEABLE_DOWN == True:
                    PLAYER_POS[1] = PLAYER_POS[1] + 1
                    PLAYER_MOVED = True

                elif (event.key == pygame.K_w or event.key == pygame.K_UP) and MOVEABLE_UP == True:
                    PLAYER_POS[1] = PLAYER_POS[1] - 1
                    PLAYER_MOVED = True

                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and MOVEABLE_LEFT == True: 
                    PLAYER_POS[0] = PLAYER_POS[0] - 1
                    PLAYER_MOVED = True

                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and MOVEABLE_RIGHT == True:
                    PLAYER_POS[0] = PLAYER_POS[0] + 1
                    PLAYER_MOVED = True

    # --- Game logic should go here


    #Button Highlight Fuction
    #Start Button
    if MOUSE_POS[0] > START_BUTTON_POS[0] and MOUSE_POS[0] < START_BUTTON_POS[0] + START_BUTTON_SIZE[0] and MOUSE_POS[1] > START_BUTTON_POS[1] and MOUSE_POS[1] < START_BUTTON_POS[1] + START_BUTTON_SIZE[1]:
        START_BUTTON_COLOUR = YELLOW
        START_BUTTON_TEXT = START_BUTTON_FONT.render("START", True, START_BUTTON_TEXT_COLOUR)
        START_BUTTON_TEXT_COLOUR = REALLY_DARK_GREY

    #Help Button
    elif MOUSE_POS[0] > HELP_BUTTON_POS[0] and MOUSE_POS[0] < HELP_BUTTON_POS[0] + HELP_BUTTON_SIZE[0] and MOUSE_POS[1] > HELP_BUTTON_POS[1] and MOUSE_POS[1] < HELP_BUTTON_POS[1] + HELP_BUTTON_SIZE[1]:
        HELP_BUTTON_COLOUR = YELLOW
        HELP_BUTTON_TEXT = HELP_BUTTON_FONT.render("HELP", True, HELP_BUTTON_TEXT_COLOUR)
        HELP_BUTTON_TEXT_COLOUR = REALLY_DARK_GREY

    #Colour Selection
    elif MOUSE_POS[0] > COLOUR_SELECTION_BUTTON_POS[0] and MOUSE_POS[0] < COLOUR_SELECTION_BUTTON_POS[0] + COLOUR_SELECTION_BUTTON_SIZE[0] and MOUSE_POS[1] > COLOUR_SELECTION_BUTTON_POS[1] and MOUSE_POS[1] < COLOUR_SELECTION_BUTTON_POS[1] + COLOUR_SELECTION_BUTTON_SIZE[1]:
        COLOUR_SELECTION_BUTTON_COLOUR = YELLOW   
        COLOUR_SELECTION_BUTTON_TEXT_1 = COLOUR_SELECTION_BUTTON_FONT.render("CHANGE", True, CS_BUTTION_TEXT_COLOUR)
        COLOUR_SELECTION_BUTTON_TEXT_2 = COLOUR_SELECTION_BUTTON_FONT.render("COLOUR", True, CS_BUTTION_TEXT_COLOUR)
        CS_BUTTION_TEXT_COLOUR = REALLY_DARK_GREY

    #Go Back Button    
    elif MOUSE_POS[0] > BACK_BUTTON_POS[0] and MOUSE_POS[0] < BACK_BUTTON_POS[0] + BACK_BUTTON_SIZE[0] and MOUSE_POS[1] > BACK_BUTTON_POS[1] and MOUSE_POS[1] < BACK_BUTTON_POS[1] + BACK_BUTTON_SIZE[1]:
        BACK_BUTTON_COLOUR = YELLOW
        BACK_BUTTON_TEXT = BACK_BUTTON_FONT.render("BACK", True, BACK_BUTTON_TEXT_COLOUR)
        BACK_BUTTON_TEXT_COLOUR = REALLY_DARK_GREY

    #Reset Colour Back To Red
    else:
        START_BUTTON_COLOUR = DARK_RED
        HELP_BUTTON_COLOUR = DARK_RED
        COLOUR_SELECTION_BUTTON_COLOUR = DARK_RED
        BACK_BUTTON_COLOUR = DARK_RED

        START_BUTTON_TEXT_COLOUR = OFF_WHITE
        HELP_BUTTON_TEXT_COLOUR = OFF_WHITE
        CS_BUTTION_TEXT_COLOUR = OFF_WHITE
        BACK_BUTTON_TEXT_COLOUR = OFF_WHITE

        START_BUTTON_TEXT = START_BUTTON_FONT.render("START", True, START_BUTTON_TEXT_COLOUR)
        HELP_BUTTON_TEXT = HELP_BUTTON_FONT.render("HELP", True, HELP_BUTTON_TEXT_COLOUR)
        COLOUR_SELECTION_BUTTON_TEXT_1 = COLOUR_SELECTION_BUTTON_FONT.render("CHANGE", True, CS_BUTTION_TEXT_COLOUR)
        COLOUR_SELECTION_BUTTON_TEXT_2 = COLOUR_SELECTION_BUTTON_FONT.render("COLOUR", True, CS_BUTTION_TEXT_COLOUR)
        BACK_BUTTON_TEXT = BACK_BUTTON_FONT.render("BACK", True, BACK_BUTTON_TEXT_COLOUR)

    #Menu
    if SCENE == 0 and MENU_SCENE == 1:
        pygame.draw.rect(screen, START_BUTTON_COLOUR, ((START_BUTTON_POS), (START_BUTTON_SIZE)))
        pygame.draw.rect(screen, BLACK, ((START_BUTTON_POS), (START_BUTTON_SIZE)), 5, 1)
        screen.blit(START_BUTTON_TEXT, (210, 460))

        pygame.draw.rect(screen, HELP_BUTTON_COLOUR, ((HELP_BUTTON_POS), (HELP_BUTTON_SIZE)))
        pygame.draw.rect(screen, BLACK, ((HELP_BUTTON_POS), (HELP_BUTTON_SIZE)), 5, 1)
        screen.blit(HELP_BUTTON_TEXT, (572, 580))
        
        pygame.draw.rect(screen, COLOUR_SELECTION_BUTTON_COLOUR, ((COLOUR_SELECTION_BUTTON_POS), (COLOUR_SELECTION_BUTTON_SIZE)))
        pygame.draw.rect(screen, BLACK, ((COLOUR_SELECTION_BUTTON_POS), (COLOUR_SELECTION_BUTTON_SIZE)), 5, 1)
        screen.blit(COLOUR_SELECTION_BUTTON_TEXT_1, (130, 663))
        screen.blit(COLOUR_SELECTION_BUTTON_TEXT_2, (130, 705))

        screen.blit(TITLE_TEXT_1, (50, 25))
        screen.blit(TITLE_TEXT_2, (225, 200))        

    #Draw Go Back Button
    if SCENE == 0 and MENU_SCENE != 1:
        pygame.draw.rect(screen, BACK_BUTTON_COLOUR, ((BACK_BUTTON_POS), (BACK_BUTTON_SIZE)))
        pygame.draw.rect(screen, BLACK, ((BACK_BUTTON_POS), (BACK_BUTTON_SIZE)), 3, 1)
        screen.blit(BACK_BUTTON_TEXT, (685, 37))


    #Help Page
    if SCENE == 0 and MENU_SCENE == 2:
        pygame.draw.rect(screen, BLACK, ((KEY_LOCATION_X, KEY_LOCATION_Y), (50, 50)), 3, 5)
        screen.blit(HELP_KEY_TEXT_A, (16 + KEY_LOCATION_X, 6 + KEY_LOCATION_Y))
        
        pygame.draw.rect(screen, BLACK, ((KEY_LOCATION_X + 50, KEY_LOCATION_Y), (50, 50)), 3, 5)
        screen.blit(HELP_KEY_TEXT_S, (17 + 50 + KEY_LOCATION_X, 6 + KEY_LOCATION_Y))

        pygame.draw.rect(screen, BLACK, ((KEY_LOCATION_X + 50, KEY_LOCATION_Y - 50), (50, 50)), 3, 5)
        screen.blit(HELP_KEY_TEXT_W, (13 + KEY_LOCATION_X + 50, 6 + KEY_LOCATION_Y - 50))        

        pygame.draw.rect(screen, BLACK, ((KEY_LOCATION_X + 100, KEY_LOCATION_Y), (50, 50)), 3, 5)
        screen.blit(HELP_KEY_TEXT_D, (17 + KEY_LOCATION_X + 100, 6 + KEY_LOCATION_Y))

        screen.blit(HELP_TEXT_1, (100, 300))
        screen.blit(HELP_TEXT_2, (100, 325))

        screen.blit(HELP_TEXT_3, (100, 410))
        screen.blit(help_virus, (600, 405))

        screen.blit(HELP_TEXT_4, (100, 495))
        screen.blit(HELP_TEXT_5, (100, 520))
        pygame.draw.rect(screen, YELLOW, ((600, 495), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]))
        pygame.draw.rect(screen, LIGHT_GREY, ((600, 495), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 2)

        screen.blit(HELP_TEXT_6, (200, 620))
        pygame.draw.rect(screen, PLAYER_COLOUR_PRIMARY, ((400, 615), [UNIT_OF_MEASUREMENT,UNIT_OF_MEASUREMENT]))
        pygame.draw.rect(screen, PLAYER_COLOUR_SECONDARY, ((400, 615), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 2)

        screen.blit(HELP_TITLE_1, (25, 25))
        screen.blit(HELP_TITLE_2, (75, 125))

    #Colour selection Page
    if SCENE == 0 and MENU_SCENE == 3:
        screen.blit(COLOUR_SELECTION_TEXT_1, (50, 50))
        screen.blit(COLOUR_SELECTION_TEXT_2, (50, 150))

        screen.blit(COLOUR_SELECTION_ARROW, COLOUR_SELECTION_ARROW_POS)

        pygame.draw.rect(screen, RED, ((RED_COLOUR), (100, 100)))
        pygame.draw.rect(screen, BLACK, ((RED_COLOUR), (100, 100)), 3, 2)

        pygame.draw.rect(screen, YELLOW, ((YELLOW_COLOUR), (100, 100)))
        pygame.draw.rect(screen, BLACK, ((YELLOW_COLOUR), (100, 100)), 3, 2)
        
        pygame.draw.rect(screen, GREEN, ((GREEN_COLOUR), (100, 100)))
        pygame.draw.rect(screen, BLACK, ((GREEN_COLOUR), (100, 100)), 3, 2)

        pygame.draw.rect(screen, BLUE, ((BLUE_COLOUR), (100, 100)))
        pygame.draw.rect(screen, BLACK, ((BLUE_COLOUR), (100, 100)), 3, 2)

        pygame.draw.rect(screen, BLACK, ((BLACK_COLOUR), (100, 100)))
        pygame.draw.rect(screen, WHITE, ((BLACK_COLOUR), (100, 100)), 3, 2)

        pygame.draw.rect(screen, WHITE, ((WHITE_COLOUR), (100, 100)))
        pygame.draw.rect(screen, BLACK, ((WHITE_COLOUR), (100, 100)), 3, 2)

    if SCENE != 0:
        #LEVEL DESIGN
            #LEVEL 2
        if LEVEL == 1 and GOAL_TRIGGERED == True:
            CURRENT_LEVEL = LEVEL_TWO
            LEVEL = LEVEL + 1
            GOAL_TRIGGERED = False
            CURRENT_POS = LEVEL_TWO_PLAYER
            CURRENT_VIRUS_POS = LEVEL_TWO_VIRUS
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS

            #LEVEL 3
        elif LEVEL == 2 and GOAL_TRIGGERED == True:
            CURRENT_LEVEL = LEVEL_THREE
            LEVEL = LEVEL + 1
            GOAL_TRIGGERED = False
            CURRENT_POS = LEVEL_THREE_PLAYER
            CURRENT_VIRUS_POS = LEVEL_THREE_VIRUS
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS

            #LEVEL 4
        elif LEVEL == 3 and GOAL_TRIGGERED == True:
            CURRENT_LEVEL = LEVEL_FOUR
            LEVEL = LEVEL + 1
            GOAL_TRIGGERED = False
            CURRENT_POS = LEVEL_FOUR_PLAYER
            CURRENT_VIRUS_POS = LEVEL_FOUR_VIRUS
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS   

            #LEVEL 5
        elif LEVEL == 5 and GOAL_TRIGGERED == True:
            CURRENT_LEVEL = LEVEL_FIVE
            LEVEL = LEVEL + 1
            GOAL_TRIGGERED = False
            CURRENT_POS = LEVEL_FIVE_PLAYER
            CURRENT_VIRUS_POS = LEVEL_FIVE_VIRUS
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS       

            #LEVEL 6    
        elif LEVEL == 5 and GOAL_TRIGGERED == True:
            CURRENT_LEVEL = LEVEL_SIX
            LEVEL = LEVEL + 1
            GOAL_TRIGGERED = False
            CURRENT_POS = LEVEL_SIX_PLAYER
            CURRENT_VIRUS_POS = LEVEL_SIX_VIRUS
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS     
        """
        if HEART_TRIGGERED == True:      
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS     
            LIVES = LIVES + 1
            HEART_TRIGGERED = False

        if VIRUS_TRIGGERED == True:
            PLAYER_POS = CURRENT_POS
            VIRUS_POS = CURRENT_VIRUS_POS
            LIVES = LIVES - 1
            VIRUS_TRIGGERED = False
        """
        for row in range(len(CURRENT_LEVEL)):
            for column in range(16):
                if CURRENT_LEVEL[row][column] == "x":
                    # Draw Wall
                    WALL_POS[0] = column
                    WALL_POS[1] = row
                    pygame.draw.rect(screen, DARK_GREY, ((WALL_POS[0] *  50, WALL_POS[1] * 50), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]))
                    pygame.draw.rect(screen, LIGHT_GREY, ((WALL_POS[0] *  50, WALL_POS[1] * 50), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 4, 1)
                

                elif CURRENT_LEVEL[row][column] == "e":
                    EXIT_POS[0] = column
                    EXIT_POS[1] = row
                    pygame.draw.rect(screen, YELLOW, ((EXIT_POS[0] * 50, EXIT_POS[1] * 50), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]))
                    pygame.draw.rect(screen, LIGHT_GREY, ((EXIT_POS[0] * 50, EXIT_POS[1] * 50), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 2)


                elif CURRENT_LEVEL[row][column] == "h":
                    HEART_POS[0] = column
                    HEART_POS[1] = row
                    screen.blit(heart, (HEART_POS[0] * 50, HEART_POS[1] * 50))

            # Player Collision 
                if LIVES <= 0:
                    CURRENT_LEVEL = LEVEL_ONE
                    MENU_SCENE = 1
                    SCENE = 0
                    LIVES = 3
                    CURRENT_POS = [15, 8]
                    CURRENT_VIRUS_POS = [0, 0]
                    PLAYER_POS = CURRENT_POS
                    VIRUS_POS = CURRENT_VIRUS_POS
                
                #Wall
                if (PLAYER_POS[0] - 1) == WALL_POS[0] and (PLAYER_POS[1]) == WALL_POS[1]:
                    MOVEABLE_LEFT = False
                elif PLAYER_POS[0] == (WALL_POS[0] - 1) and (PLAYER_POS[1]) == WALL_POS[1]:
                    MOVEABLE_RIGHT = False
                elif PLAYER_POS[0] == WALL_POS[0] and (PLAYER_POS[1] - 1) == WALL_POS[1]:
                    MOVEABLE_UP = False
                elif PLAYER_POS[0] == WALL_POS[0] and PLAYER_POS[1] == (WALL_POS[1] - 1):
                    MOVEABLE_DOWN = False

            # Virus Collision 
                #Wall
                if (VIRUS_POS[0] - 1) == WALL_POS[0] and VIRUS_POS[1] == WALL_POS[1]:
                    VIRUS_LEFT = False
                elif VIRUS_POS[0] == (WALL_POS[0] - 1) and VIRUS_POS[1] == WALL_POS[1]:
                    VIRUS_RIGHT = False
                elif VIRUS_POS[0] == WALL_POS[0] and (VIRUS_POS[1] - 1) == WALL_POS[1]:
                    VIRUS_UP = False
                elif VIRUS_POS[0] == WALL_POS[0] and VIRUS_POS[1] == (WALL_POS[1] - 1):
                    VIRUS_DOWN = False

                # Collision With Exit
                if PLAYER_POS == EXIT_POS:
                    GOAL_TRIGGERED = True

                # Collision with Heart
                elif PLAYER_POS == HEART_POS:
                    LIVES = LIVES + 1
                    PLAYER_POS = CURRENT_POS
                    VIRUS_POS = CURRENT_VIRUS_POS
                    HEART_TRIGGERED = True

                # Collision with Virus
                elif PLAYER_POS == VIRUS_POS:

                    LIVES = LIVES - 1
                    PLAYER_POS = CURRENT_POS
                    VIRUS_POS = CURRENT_VIRUS_POS
                    VIRUS_TRIGGERED = True


        if PLAYER_MOVED is True:
            if VIRUS_UP is True and VIRUS_POS[1] > PLAYER_POS[1]:
                VIRUS_POS[1] = VIRUS_POS[1] - 1

            elif VIRUS_DOWN is True and VIRUS_POS[1] < PLAYER_POS[1]:
                VIRUS_POS[1] = VIRUS_POS[1] + 1    

            elif VIRUS_LEFT is True and VIRUS_POS[0] > PLAYER_POS[0]:
                VIRUS_POS[0] = VIRUS_POS[0] - 1

            elif VIRUS_RIGHT is True and VIRUS_POS[0] < PLAYER_POS[0]:
                VIRUS_POS[0] = VIRUS_POS[0] + 1

            #BOTTOM CORNER
            elif VIRUS_RIGHT is False and VIRUS_DOWN is False and VIRUS_LEFT is False:
                VIRUS_POS[1] = VIRUS_POS[1] - 1

            elif VIRUS_RIGHT is False and VIRUS_UP is False and VIRUS_LEFT is False:
                VIRUS_POS[1] = VIRUS_POS[1] + 1
            
            #RIGHT CORNER
            elif VIRUS_UP is False and VIRUS_DOWN is False and VIRUS_RIGHT is False:
                VIRUS_POS[0] = VIRUS_POS[0] - 1

            #LEFT CORNER
            elif VIRUS_UP is False and VIRUS_DOWN is False and VIRUS_LEFT is False:
                VIRUS_POS[0] = VIRUS_POS[0] + 1
 
            PLAYER_MOVED = False
            
            #Resets movement options
            MOVEABLE_UP = True
            MOVEABLE_DOWN = True
            MOVEABLE_LEFT = True
            MOVEABLE_RIGHT = True

            VIRUS_LEFT = True
            VIRUS_RIGHT = True
            VIRUS_DOWN = True
            VIRUS_UP = True

        #Border 
        if PLAYER_POS[0] <= 0:
            MOVEABLE_LEFT = False
        if PLAYER_POS[0] + 1 >= 16:
            MOVEABLE_RIGHT = False
        if PLAYER_POS[1] <= 0:
            MOVEABLE_UP = False
        if PLAYER_POS[1]  + 1 >= 16:
            MOVEABLE_DOWN = False
            

        
        #Border
        elif VIRUS_POS[0] <= 0:
            VIRUS_LEFT = False
        elif VIRUS_POS[0] + 50 >= 850:
            VIRUS_RIGHT = False
        elif VIRUS_POS[1] <= 0:
            VIRUS_UP = False
        elif VIRUS_POS[1] + 50  >= 850:
            VIRUS_DOWN = False

                    
        #Check if testing restart
        if TEST_RESTART is True:
            PLAYER_POS = [15, 8]
            VIRUS_POS = [0, 0]
            TEST_RESTART = False


    # --- Drawing code should go here
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.

    # Draw the current amount of lives
        lives_text = lives_font.render("LIVES: " + str(LIVES), True, BLACK)
        screen.blit(lives_text, (700, 0))

    # Draw the current level
        level_text = level_font.render("LEVEL: " + str(LEVEL), True, BLACK)
        screen.blit(level_text, (700, 30))
        
        pygame.draw.rect(screen, PLAYER_COLOUR_PRIMARY, ((PLAYER_POS[0] * 50, PLAYER_POS[1] * 50), [UNIT_OF_MEASUREMENT,UNIT_OF_MEASUREMENT]))
        pygame.draw.rect(screen, PLAYER_COLOUR_SECONDARY, ((PLAYER_POS[0] * 50, PLAYER_POS[1] * 50), [UNIT_OF_MEASUREMENT, UNIT_OF_MEASUREMENT]), 2)
        screen.blit(virus, (VIRUS_POS[0] * 50, VIRUS_POS[1] * 50))
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(360)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()