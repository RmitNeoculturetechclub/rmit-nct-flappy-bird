import pygame  # use pygame module
from random import randint

GREEN = (0, 200, 0)  # RGB color selector
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


def level(speed, acceleration):
    pygame.init()  # initialise pygame functions
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))  # set the width and height of the game screen
    pygame.display.set_caption("Flappy Bird")  # set the game caption
    clock = pygame.time.Clock()  # use clock function in pygame
    running = True  # while the game is running, the while loop is infinity

    tube_width = 50  # tube width
    tube_velocity = speed  # tube speed
    acceleration = acceleration
    tube_gap = 150
    tube1_x = width + 300
    tube2_x = width + 600
    tube3_x = width + 900
    tube_y = 0
    tube1_height = randint(100, 400)
    tube2_height = randint(100, 400)
    tube3_height = randint(100, 400)
    tube1_pass = False  # at the beginning, the bird does not pass the tube
    tube2_pass = False
    tube3_pass = False

    bird_x = 50
    bird_y = 400
    bird_width = 35
    bird_height = 35
    bird_drop_velocity = 0
    gravity = 0.3

    score = 0
    font = pygame.font.SysFont("san", 20)  # create font and size for text on screen

    pausing = False  # haven't lost the game
    background_image = pygame.image.load("images/background.png")
    bird_image = pygame.image.load("images/bird.png")
    bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))

    while running:  # game running process
        clock.tick(60)  # 1 sec run 60 frames
        screen.fill(GREEN)  # screen background color
        screen.blit(background_image, (0, 0))

        ''' Draw tubes '''
        tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, tube_y, tube_width, tube1_height))
        tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, tube_y, tube_width, tube2_height))
        tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, tube_y, tube_width, tube3_height))

        ''' Draw inverse tubes '''
        tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + tube_gap, tube_width, height - tube1_height - tube_gap))
        tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + tube_gap, tube_width, height - tube2_height - tube_gap))
        tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + tube_gap, tube_width, height - tube3_height - tube_gap))

        ''' Move faster '''
        tube_velocity += acceleration

        ''' Move tubes on Ox '''
        tube1_x = tube1_x - tube_velocity
        tube2_x = tube2_x - tube_velocity
        tube3_x = tube3_x - tube_velocity

        ''' Draw sand '''
        sand_rect = pygame.draw.rect(screen, YELLOW, (0, height - 50, width, 50))

        ''' Create new tubes when old tubes disappear'''
        if tube1_x < -tube_width:
            tube1_x = width + 50
            tube1_height = randint(100, 400)
            tube1_pass = False  # reset the tube pass
        if tube2_x < -tube_width:
            tube2_x = width + 50
            tube2_height = randint(100, 400)
            tube2_pass = False  # reset the tube pass
        if tube3_x < -tube_width:
            tube3_x = width + 50
            tube3_height = randint(100, 400)
            tube3_pass = False  # reset the tube pass

        ''' Draw bird'''
        bird_rect = screen.blit(bird_image, (bird_x, bird_y))

        ''' Bird fall '''
        bird_y += bird_drop_velocity
        bird_drop_velocity += gravity

        ''' Update score '''
        score_txt = font.render("Score: " + str(score), True, BLACK)  # render text with color
        screen.blit(score_txt, (5, 5))  # write text on screen
        if tube1_x + tube_width <= bird_x and tube1_pass is False:  # 1 point for each time pass the tube
            score += 1
            tube1_pass = True
        if tube2_x + tube_width <= bird_x and tube2_pass is False:
            score += 1
            tube2_pass = True
        if tube3_x + tube_width <= bird_x and tube3_pass is False:
            score += 1
            tube3_pass = True

        ''' Check collision '''
        for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect]:
            if bird_rect.colliderect(tube):
                pausing = True  # lost the game
                tube_velocity = 0  # tubes stop moving
                bird_drop_velocity = 0  # bird stops dropping
                game_over_txt = font.render("GAME OVER, YOUR SCORE: " + str(score), True, RED)
                screen.blit(game_over_txt, (300, 300))
                press_space_txt = font.render("PRESS SPACE TO CONTINUE", True, RED)
                screen.blit(press_space_txt, (300, 320))

        ''' Set event such as mouseclick, keyboard buttons, quit'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you click on X button, it will exit the game
                running = False
            elif event.type == pygame.KEYDOWN:  # use keyboard
                if event.key == pygame.K_SPACE:  # space button
                    # reset
                    if pausing:  # if player lost the game, reset all
                        bird_y = 400
                        tube_velocity = 3
                        tube1_x = width + 300
                        tube2_x = width + 600
                        tube3_x = width + 900
                        score = 0
                        pausing = False  # start again
                    bird_drop_velocity = 0  # reset the bird's drop speed (no gravity)
                    bird_drop_velocity -= 5  # make the bird jump

        pygame.display.flip()  # apply the colors changes to the screen

    pygame.quit()  # finish using pygame


def main():
    while True:
        lvl = input("Enter the level you want (easy, medium, hard): ")
        if lvl == "easy":
            level(1, 0.001)  # easy
            break
        elif lvl == "medium":
            level(2, 0.002)  # medium
            break
        elif lvl == "hard":
            level(3, 0.003)  # hard
            break
        else:
            print("Invalid syntax, please enter again: ")
            continue


main()
