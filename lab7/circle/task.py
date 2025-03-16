import pygame

pygame.init()

screen = pygame.display.set_mode((800,500))
running = True
FPS = 60
clock = pygame.time.Clock()
circle_x=400
circle_y=250
speed = 20
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill('White')
    circle = pygame.draw.circle(screen, 'Red', (circle_x,circle_y), 25)

    py_keys = pygame.key.get_pressed()
    
    if py_keys[pygame.K_UP] and circle_y-25-speed >= 0:
        circle_y-=speed
    if py_keys[pygame.K_DOWN] and circle_y+25+speed <= 500:
        circle_y+=speed
    if py_keys[pygame.K_RIGHT] and circle_x+25+speed <= 800:
        circle_x+=speed
    if py_keys[pygame.K_LEFT] and circle_x-25-speed >= 0:
            circle_x-=speed
    
    


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
