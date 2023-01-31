import pygame
import button

pygame.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
start_img = pygame.image.load("images/START.png").convert_alpha()
mode_img = pygame.image.load("images/MODE.png").convert_alpha()
quit_img = pygame.image.load("images/QUIT.png").convert_alpha()
easy_img = pygame.image.load('images/EASY.png').convert_alpha()
medium_img = pygame.image.load('images/MEDIUM.png').convert_alpha()
hard_img = pygame.image.load('images/HARD.png').convert_alpha()
back_img = pygame.image.load('images/BACK.png').convert_alpha()

# create button instances
start_button = button.Button(250, 150, start_img, 1)
mode_button = button.Button(250, 250, mode_img, 1)
quit_button = button.Button(250, 350, quit_img, 1)
easy_button = button.Button(250, 100, easy_img, 1)
medium_button = button.Button(250, 200, medium_img, 1)
hard_button = button.Button(250, 300, hard_img, 1)
back_button = button.Button(250, 400, back_img, 1)


def draw_text(text, text_font, text_col, x, y):
    img = text_font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
while run:

    screen.fill((52, 78, 91))

    # check if game is paused
    if game_paused:
        # check menu state
        if menu_state == "main":
            # draw pause screen buttons
            if start_button.draw(screen):
                game_paused = False
            if mode_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        # check if the options menu is open
        if menu_state == "options":
            # draw the different options buttons
            if easy_button.draw(screen):
                print("Video Settings")
            if medium_button.draw(screen):
                print("Audio Settings")
            if hard_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to enter the game", font, TEXT_COL, 60, 250)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
