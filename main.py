import pygame
import sys
import math 
import random

pygame.init
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Whack-a-Mole")
grass = pygame.image.load("C:\ComputerScience\Whack-a-mole\cartoon-grass-images-background-copy-space_1179130-877214.jpg")
grass_rect = grass.get_rect(topleft=(0, 0))
grass = pygame.transform.scale(grass, (1280, 720))
CircleSurface = pygame.surface.Surface((1280, 720))
hammer_cursor = pygame.image.load("C:\ComputerScience\Whack-a-mole\woodhammer.png")
hammer_cursor = pygame.transform.scale(hammer_cursor, (200, 180))

circle_pos = (1280/2, 720/2)

pygame.font.init()
font = pygame.font.Font(None, 50)  

Score = 0

def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= 50:
        return True
    return False

while True:
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button  == 1: #left click
                if check_circle_collision():
                    Score += 1
                    circle_pos = (random.randint(0, 1280), random.randint(0,720))

        score_surface = font.render(f'Score: {Score}', True, "yellow")

    screen.fill('white')

    screen.blit(grass, grass_rect)

    screen.blit(score_surface, (50, 50))

    circle = pygame.draw.circle(screen, "black", circle_pos, 55)

    CircleImgMole = pygame.image.load("C:\ComputerScience\Whack-a-mole\mole4.png")

    CircleImgMole = pygame.transform.scale(CircleImgMole,(320, 300))

    screen.blit(CircleImgMole, circle) 

    pygame.mouse.set_visible(False)

    screen.blit(hammer_cursor, mouse_pos)

    pygame.display.update()

    pygame.display.update()



