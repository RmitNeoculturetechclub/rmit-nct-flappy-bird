import pygame  # use pygame module
from random import randint

pygame.init()  # initialise pygame functions
WIDTH, HEIGHT = 450, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set the width and height of the game screen
pygame.display.set_caption("Flappy Bird")  # set the game caption
running = True  # while the game is running, the while loop is infinity

GREEN = (0, 200, 0)  # RGB color selector
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()  # use clock function in pygame

# constant variables
TUBE_WIDTH = 50  # tube width
TUBE_VELOCITY = 3  # tube speed
TUBE_GAP = 150

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.3

score = 0
font = pygame.font.SysFont("san", 20)  # create font and size for text on screen

tube1_pass = False  # at the beginning, the bird does not pass the tube
tube2_pass = False
tube3_pass = False

pausing = False  # haven't lost the game
background_image = pygame.image.load("background.png")
bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

while running:  # game running process
    clock.tick(60)  # 1 sec run 60 frames
    screen.fill(GREEN)  # screen background color
    screen.blit(background_image, (0, 0))

    # draw tubes
    tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

    # draw tubes inverse
    tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
    tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
    tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))

    # move tubes on Ox
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    # draw sand
    sand_rect = pygame.draw.rect(screen, YELLOW, (0, HEIGHT - 50, WIDTH, 50))

    # create new tubes when old tubes disappear
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100, 400)
        tube1_pass = False  # reset the tube pass
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_pass = False  # reset the tube pass
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100, 400)
        tube3_pass = False  # reset the tube pass

    # draw bird
    bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))

    # bird falls
    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAVITY

    # update score
    score_txt = font.render("Score: " + str(score), True, BLACK)  # render text with color
    screen.blit(score_txt, (5, 5))  # write text on screen
    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass is False:  # 1 point for each time pass the tube
        score += 1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass is False:
        score += 1
        tube2_pass = True
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass is False:
        score += 1
        tube3_pass = True

    # check collision
    for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect]:
        if bird_rect.colliderect(tube):
            pausing = True  # lost the game
            TUBE_VELOCITY = 0  # tubes stop moving
            bird_drop_velocity = 0  # bird stops dropping
            game_over_txt = font.render("GAME OVER, YOUR SCORE: " + str(score), True, RED)
            screen.blit(game_over_txt, (100, 300))
            press_space_txt = font.render("PRESS SPACE TO CONTINUE", True, RED)
            screen.blit(press_space_txt, (100, 400))

    for event in pygame.event.get():  # set the event such as mouseclick, quit, keyboard clicks
        if event.type == pygame.QUIT:  # when you click on X button, it will exit the game
            running = False
        elif event.type == pygame.KEYDOWN:  # use keyboard
            if event.key == pygame.K_SPACE:  # space button
                # reset
                if pausing:  # if player lost the game, reset all
                    bird_y = 400
                    TUBE_VELOCITY = 3
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    score = 0
                    pausing = False  # start again

                bird_drop_velocity = 0  # reset the bird's drop speed (no gravity)
                bird_drop_velocity -= 5  # make the bird jump

    pygame.display.flip()  # apply the colors changes to the screen

pygame.quit()  # finish using pygame
