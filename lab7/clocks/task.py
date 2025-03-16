import pygame, datetime
pygame.init() 

screen = pygame.display.set_mode((1000, 800))
WHITE = (255,255,255)

clock_x, clock_y = screen.get_width() // 2, screen.get_height() // 2


running = True
clock = pygame.time.Clock()

clocks = pygame.image.load('lab7/clocks/clock.png')
min_hand = pygame.image.load('lab7/clocks/min_hand.png')
sec_hand = pygame.image.load('lab7/clocks/sec_hand.png')

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    screen.blit(clocks, (clock_x - clocks.get_width() // 2, clock_y - clocks.get_height() // 2))

    now = datetime.datetime.now()
    sec_angle = 360 -(now.second*6)
    sec_x = clock_x
    sec_y = clock_y

    min_angle = 360 - (now.minute*6)
    min_x = clock_x
    min_y = clock_y


    rotated_sec_hand, new_sec_hand = rot_center(sec_hand, sec_angle, sec_x, sec_y)
    screen.blit(rotated_sec_hand, new_sec_hand)
    
    rotated_min_hand, new_min_hand = rot_center(min_hand, min_angle, min_x, min_y)
    screen.blit(rotated_min_hand, new_min_hand)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
