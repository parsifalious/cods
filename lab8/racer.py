from PIL import Image
img=Image.open("/Users/alialesov/Desktop/labs/lab8/racer_textures/coin.png")
img_resized=img.resize((30,30))
img_resized.save("/Users/alialesov/Desktop/labs/lab8/racer_textures/coin_resized.png")
img=Image.open("/Users/alialesov/Desktop/labs/lab8/racer_textures/AnimatedStreet.png")
img_resized=img.resize((400,600))
img_resized.save("/Users/alialesov/Desktop/labs/lab8/racer_textures/AnimatedStreet_resized.png")
img=Image.open("/Users/alialesov/Desktop/labs/lab8/racer_textures/coin2.png")
img_resized=img.resize((45,45))
img_resized.save("/Users/alialesov/Desktop/labs/lab8/racer_textures/coin_resized.png")

import pygame, sys
from pygame.locals import *
import random, time


# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("/Users/alialesov/Desktop/labs/lab8/racer_textures/AnimatedStreet_resized.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/alialesov/Desktop/labs/lab8/racer_textures/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(70, 250), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 250), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/alialesov/Desktop/labs/lab8/racer_textures/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/alialesov/Desktop/labs/lab8/racer_textures/coin_resized.png")
        self.rect = self.image.get_rect(center=(random.randint(70, 330), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        while True:
            new_x = random.randint(70, 330)
            self.rect.center = (new_x, 0)
            if not self.rect.colliderect(E1.rect):
                  # Проверяем пересечение с врагом
                break

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    
    # Display score and coins
    score_text = font_small.render(str(SCORE), True, BLACK)
    coin_text = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(score_text, (10,10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH-20,10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/alialesov/Desktop/labs/lab8/racer_textures/crash.wav').play()
        time.sleep(1.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.mixer.Sound('/Users/alialesov/Desktop/labs/lab8/racer_textures/Losing.wav').play()

        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2.5)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        COINS += (random.randint(1,2))
        C1.reset_position()
        pygame.mixer.Sound('/Users/alialesov/Desktop/labs/lab8/racer_textures/coin.wav').play()
          
    pygame.display.update()
    FramePerSec.tick(FPS)
