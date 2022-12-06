import pygame
import button

pygame.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
start_img = pygame.image.load("Images/Start Button.png").convert_alpha()
video_img = pygame.image.load('Images/button_video.png').convert_alpha()
audio_img = pygame.image.load('Images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('Images/button_keys.png').convert_alpha()
quit_img = pygame.image.load('Images/Quit Button.png').convert_alpha()

# create button instances
start_button = button.Button(250, 150, start_img, 0.5)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
quit_button = button.Button(250, 300, quit_img, 0.5)