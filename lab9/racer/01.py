import pygame
import random
import time

pygame.init()

# Screen info
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Scores
SCORE = 0
STARCOIN_SCORE = 0

# Images (Background, Player, Enemy)
image_background = pygame.image.load('resources/AnimatedStreet.png').convert_alpha()
image_player = pygame.image.load('resources/Player.png').convert_alpha()
image_enemy = pygame.image.load('resources/Enemy.png').convert_alpha()


# Music/Sound
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1) # plays music infinitely
sound_crash = pygame.mixer.Sound('resources/crash.wav')


 # Font/Texts
font = pygame.font.SysFont("Verdana", 60)
font_score = pygame.font.SysFont("Verdana", 20)

image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

# Classes - Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 7

    def move(self):
        keys = pygame.key.get_pressed() # list with keys on keyboard
        if keys[pygame.K_RIGHT]: # when right arrow pressed 
            self.rect.move_ip(self.speed, 0) # moves object to the right
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        # To prevent an object from moving outside the screen
        if self.rect.left < 0: # resets left pos to 0
            self.rect.left = 0
        if self.rect.right > WIDTH: # resets right pos to WIDTH
            self.rect.right = WIDTH

# Class - Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 6
    # generates random position
    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0 #sets object above the screen
    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed) # moves object to the bottom of the screen
        if self.rect.top > HEIGHT: # if object is outside the screen, spawns it back to the top with another position
            SCORE+=1
            self.generate_random_rect()
            if STARCOIN_SCORE >= 20: # speed increase / game becomes more difficult
                self.speed = 15
        



running = True
clock = pygame.time.Clock()
FPS = 60

# class objects
player = Player()
enemy = Enemy()
enemy.rect.centerx = WIDTH // 2 # making car appear at the center when game starts
enemy.rect.bottom = 0



# Coin Image for Star coin score on the screen
image_coins = pygame.image.load('resources/coin_star.png')
scaled_image_coin = pygame.transform.scale(image_coins, (40, 40))


sound_coin = pygame.mixer.Sound('resources/coin.mp3') # sound when star coin received

# Class - Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('resources/coin_star.png')
        self.size = random.choice([30, 40, 50])

        if self.size == 30:
                self.speed = 5
                self.point = 1
        elif self.size == 40:
                self.speed = 7
                self.point = 2
        elif self.size == 50:
                self.speed = 9
                self.point = 3

        self.image = pygame.transform.scale(self.original_image, (self.size, self.size))
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT: 
            self.rect.topleft = (random.randint(0, WIDTH-self.rect.w), -100)

    def reset_pos(self): # resets coins size and position
        self.size = random.choice([30, 40, 50])
        self.image = pygame.transform.scale(self.original_image, (self.size, self.size))

        if self.size == 30:
            self.speed = 5
            self.point = 1
        elif self.size == 40:
            self.speed = 7
            self.point = 2
        elif self.size == 50:
            self.speed = 9
            self.point = 3

        self.rect.topleft = (random.randint(0, WIDTH - self.rect.w), -100)

    def coin_collision(self):
        global STARCOIN_SCORE
        if self.rect.colliderect(player.rect):
            STARCOIN_SCORE += self.point
            sound_coin.play()

            self.reset_pos()


coin = Coin()

# Groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

coin_sprites.add(coin)
all_sprites.add(player, enemy)
enemy_sprites.add(enemy)




#Game loop
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False


    # text for SCORE
    screen.blit(image_background, (0, 0))
    scores = font_score.render(f'Score: {SCORE}', True, "Black")
    screen.blit(scores, (10, 10))

    for sprite in all_sprites:
        sprite.move()
        screen.blit(sprite.image, sprite.rect)

    for c in coin_sprites:
        c.move()
        c.coin_collision()
        screen.blit(c.image, c.rect)


    # text and image for STAR_COIN SCORE
    coin_score_text = font_score.render(f"x{STARCOIN_SCORE}", True, "Black")
    screen.blit(scaled_image_coin, (320, 3))
    screen.blit(coin_score_text, (360, 13))

    # Checking for collision of player and enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(0.2)

        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect) # game over screen appears
        pygame.display.flip()
          
        waiting = True

        while waiting: # loop, waiting for player to press SPACE or QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                         # setting scores to 0 again
                        SCORE = 0
                        STARCOIN_SCORE = 0
                        
                        # creating class objects again
                        player = Player()
                        enemy = Enemy()
                        coin = Coin()

                        # game resets - enemy moves to different pos at the beginning
                        enemy.generate_random_rect()
                        
                        # clering groups
                        all_sprites.empty()
                        enemy_sprites.empty()
                        coin_sprites.empty()

                        # adding class objects to groups
                        all_sprites.add(player, enemy)
                        enemy_sprites.add(enemy)
                        coin_sprites.add(coin)

                        screen.fill("white")
                        waiting = False


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()