import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

# COLORS
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorPINK = (255, 192, 203)

colors = {
    pygame.K_1: colorBLACK,
    pygame.K_2: colorRED,
    pygame.K_3: colorBLUE,
    pygame.K_4: colorPINK

} # dictionary assigning colors for each number on keyboard

picked_color = colorBLACK # default option

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(colorWHITE)
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)

pygame.display.set_caption("Paint")


clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5


currX = currY = prevX = prevY = 0

running = True

current_tool = 'line'

# calculation of pos and size of rectangle 
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

        if event.type == pygame.KEYDOWN:
            # Selecting Color
            if event.key in colors:
                picked_color = colors[event.key]

            # Picking drawing tool
            if event.key == pygame.K_l:
                current_tool = 'line'
            if event.key == pygame.K_r:
                current_tool = 'rectangle'
            if event.key == pygame.K_e:
                current_tool = 'eraser'
            if event.key == pygame.K_c:
                current_tool = 'circle'

            # Thickness regulator
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            currX = event.pos[0]
            currY = event.pos[1]
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                if current_tool == 'rectangle':
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.rect(screen, picked_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                if current_tool == 'circle':
                    screen.blit(base_layer, (0, 0))
                    radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                    pygame.draw.circle(screen, picked_color, (prevX, prevY), radius, THICKNESS)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos

            if current_tool == 'rectangle':
                pygame.draw.rect(base_layer, picked_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)  
            if current_tool == 'circle':
                radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                pygame.draw.circle(base_layer, picked_color, (prevX, prevY), radius, THICKNESS)
        

        if current_tool == 'line' and LMBpressed:
            pygame.draw.line(screen, picked_color, (prevX, prevY), (currX, currY), THICKNESS)
            pygame.draw.line(base_layer, picked_color, (prevX, prevY), (currX, currY), THICKNESS) 
        if current_tool == 'eraser' and LMBpressed:
            pygame.draw.line(screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
            pygame.draw.line(base_layer, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
        


    if current_tool == 'line' or current_tool == 'eraser':
        prevX = currX
        prevY = currY


    # mini squares of available colors to pick
    pygame.draw.rect(screen, colorBLACK, (20, 10, 20, 20))
    pygame.draw.rect(screen, colorRED, (50, 10, 20, 20))
    pygame.draw.rect(screen, colorBLUE, (80, 10, 20, 20))
    pygame.draw.rect(screen, colorPINK, (110, 10, 20, 20))

    pygame.display.flip()
    clock.tick(60)
