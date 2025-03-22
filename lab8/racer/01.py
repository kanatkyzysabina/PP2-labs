import pygame
import random
import time

pygame.init()

# Screen info
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Score
SCORE = 0
STARCOIN_SCORE = 0

# Images
image_background = pygame.image.load('resources/AnimatedStreet.png').convert_alpha()
image_player = pygame.image.load('resources/Player.png').convert_alpha()
image_enemy = pygame.image.load('resources/Enemy.png').convert_alpha()


# Music/Sound
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('resources/crash.wav')

 # Font/Texts
font = pygame.font.SysFont("Verdana", 60)
font_score = pygame.font.SysFont("Verdana", 20)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

# Classes - Player/Enemy
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            SCORE+=1
            self.generate_random_rect()

# Basic stuff
running = True
clock = pygame.time.Clock()
FPS = 60


# Sprites/Groups
player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

# Coin Stuff
image_coin = pygame.image.load('resources/coin_star.png').convert_alpha()
scaled_image_coin = pygame.transform.scale(image_coin, (40, 40))
image_coin_rect = scaled_image_coin.get_rect()
image_coin_rect.topleft = (random.randint(0, WIDTH-40), -100)

coin_speed = 5
sound_coin = pygame.mixer.Sound('resources/coin.mp3')

def coin_move():
    image_coin_rect.move_ip(0, coin_speed)
    if image_coin_rect.top > HEIGHT:
        image_coin_rect.topleft = (random.randint(0, WIDTH-image_coin_rect.w), -100)

def coin_collision():
    global STARCOIN_SCORE
    if image_coin_rect.colliderect(player.rect):
        sound_coin.play()
        STARCOIN_SCORE += 1
        image_coin_rect.topleft = (random.randint(0, WIDTH-image_coin_rect.w), -100)




#Game loop
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        

    player.move()
    screen.blit(image_background, (0, 0))
    scores = font_score.render(f'Score: {SCORE}', True, "Black")
    screen.blit(scores, (10, 10))

    # COIN SCORE
    coin_score_text = font_score.render(f"x{STARCOIN_SCORE}", True, "Black")
    screen.blit(scaled_image_coin, (320, 3))
    screen.blit(coin_score_text, (360, 13))
    coin_move()
    coin_collision()
    screen.blit(scaled_image_coin, image_coin_rect)

    
    
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)

        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()

        time.sleep(3)
        
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()