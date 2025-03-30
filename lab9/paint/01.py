import pygame
import math
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


currX = currY = prevX = prevY = 0 # current and previous mouse coordinates

running = True

current_tool = 'line'

# calculation of pos and size of rectangle 
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# calculating pos and size of square
def calculate_square(x1, y1, x2, y2):
    side = min(abs(x2 - x1), abs(y2 - y1)) 
    return pygame.Rect(min(x1, x2), min(y1, y2), side, side)

def calculate_eq_triangle(x1, y1, x2, y2): # function to return 3 vertices of an eq triangle
    # base midpoint
    midX = (x1 + x2) / 2
    midY = (y1 + y2) / 2

    # side length
    side_length = math.dist((x1, y1), (x2, y2))

    # height
    height = (math.sqrt(3) / 2) * side_length

    # top vertex
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx)

    topX = midX - height * math.sin(angle)
    topY = midY + height * math.cos(angle)

    return [(x1, y1), (x2, y2), (topX, topY)]

# calculating right triangle
def calculate_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2)]

# calculating rhombus
def calculate_rhombus(x1, y1, x2, y2):
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2

    return [(cx - dx, cy), (cx, cy - dy), (cx + dx, cy), (cx, cy + dy)]


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
            if event.key == pygame.K_s:
                current_tool = 'square'
            if event.key == pygame.K_y:
                current_tool = 'right triangle'
            if event.key == pygame.K_t:
                current_tool = 'equilateral triangle'
            if event.key == pygame.K_h:
                current_tool = 'rhombus'
            

            # Thickness regulator
            if event.key == pygame.K_EQUALS:
                print(f"increased thickness: {THICKNESS}")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print(f"reduced thickness: {THICKNESS}")
                THICKNESS -= 1

        # If Left Mouse Button pressed, store ccurent mouse pos to currX(Y) and prevX(Y)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            currX = event.pos[0] # x-coordinate of the mouse
            currY = event.pos[1] # y-coordinate of the mouse
            prevX = event.pos[0]
            prevY = event.pos[1]

        # if LMB pressed and user moves mouse
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos # updating current coordinates
                if current_tool == 'rectangle':
                    screen.blit(base_layer, (0, 0)) # restores the screen to how it looked before drawing
                    # drawing updated shape at current mouse position
                    pygame.draw.rect(screen, picked_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                if current_tool == 'square':
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.rect(screen, picked_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                if current_tool == 'circle':
                    screen.blit(base_layer, (0, 0))
                    radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                    pygame.draw.circle(screen, picked_color, (prevX, prevY), radius, THICKNESS)
                if current_tool == 'equilateral triangle':
                    screen.blit(base_layer, (0, 0))
                    eq_triangle_points = calculate_eq_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, picked_color, eq_triangle_points, THICKNESS)
                if current_tool == 'right triangle':
                    screen.blit(base_layer, (0, 0))
                    right_triangle_points = calculate_right_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, picked_color, right_triangle_points, THICKNESS)
                if current_tool == 'rhombus':
                    screen.blit(base_layer, (0, 0))
                    rhombus_points = calculate_rhombus(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, picked_color, rhombus_points, THICKNESS)

        # when user releases left mouse button:
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos # updating current mouse position
            # drawing shape permanently on a base layer
            if current_tool == 'rectangle':
                pygame.draw.rect(base_layer, picked_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)  
            if current_tool == 'circle':
                radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                pygame.draw.circle(base_layer, picked_color, (prevX, prevY), radius, THICKNESS)
            if current_tool == 'square':
                pygame.draw.rect(base_layer, picked_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
            if current_tool == 'equilateral triangle':
                eq_triangle_points = calculate_eq_triangle(prevX, prevY, currX, currY)
                pygame.draw.polygon(base_layer, picked_color, eq_triangle_points, THICKNESS)
            if current_tool == 'right triangle':
                right_triangle_points = calculate_right_triangle(prevX, prevY, currX, currY)
                pygame.draw.polygon(base_layer, picked_color, right_triangle_points, THICKNESS)
            if current_tool == 'rhombus':
                rhombus_points = calculate_rhombus(prevX, prevY, currX, currY)
                pygame.draw.polygon(base_layer, picked_color, rhombus_points, THICKNESS)


        if current_tool == 'line' and LMBpressed:
            pygame.draw.line(screen, picked_color, (prevX, prevY), (currX, currY), THICKNESS)
            pygame.draw.line(base_layer, picked_color, (prevX, prevY), (currX, currY), THICKNESS) 
            prevX = currX
            prevY = currY
        if current_tool == 'eraser' and LMBpressed:
            pygame.draw.line(screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
            pygame.draw.line(base_layer, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
            prevX = currX
            prevY = currY
        

    # mini squares of available colors
    pygame.draw.rect(screen, colorBLACK, (20, 10, 20, 20))
    pygame.draw.rect(screen, colorRED, (50, 10, 20, 20))
    pygame.draw.rect(screen, colorBLUE, (80, 10, 20, 20))
    pygame.draw.rect(screen, colorPINK, (110, 10, 20, 20))

    pygame.display.flip()
    clock.tick(60)
