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

end = False

circle_pos = (1280/2, 720/2)

pygame.font.init()
font = pygame.font.Font(None, 50)  

Score = 0

def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= 50:
        return True
    return False

clock = pygame.time.Clock()

clicks = 0
time_taken = 0

text = font.render('', True, (0, 0, 0), (255, 255, 255))
text2 = font.render('', True, (0, 0, 0), (255, 255, 255))
text3 = font.render('', True, (0, 0, 0), (255, 255, 255))

while True:
    font = pygame.font.Font(None, 50)  
    text_rect = text.get_rect()
    text_rect.center = (500, 500)
    text2_rect = text2.get_rect()
    text2_rect.center = (500, 500)
    text3_rect = text3.get_rect()
    text3_rect.center = (500, 500)
    clock = pygame.time.Clock()
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

        
    for event in events:
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button  == 1: #left click
                if check_circle_collision():
                    Score += 1
                    clicks +=1
                    circle_pos = (random.randint(0, 1280), random.randint(0,720))
                    if clicks == 10:
                        #screen.fill('white')
                        unaverage = time_taken/10
                        average = round(unaverage, 3)
                        font = pygame.font.Font(None, 50)  
                        text = font.render(str(average), True, (0, 255, 0), (0, 0, 255))
                        text_rect = text.get_rect()
                        text_rect.center = (640, 360)
                        screen.blit(text, text_rect)
                        text2 = font.render(str('Your average time to whack a mole is (s) ='), True, (0, 255, 0), (0, 0, 255))
                        text2_rect = text2.get_rect()
                        text2_rect.center = (640, 360)
                        screen.blit(text2, text2_rect)
                        text3 = font.render(str('Try again? Press space'), True, (0, 255, 0), (0, 0, 255))
                        text3_rect = text3.get_rect()
                        text3_rect.center = (640, 360)
                        screen.blit(text3, text3_rect)
                        text_rect.center = (950, 360)
                        screen.blit(text, text_rect)
                        text2_rect.center = (500, 360)
                        screen.blit(text2, text2_rect)
                        #text3_rect.center = (640, 400)
                        #screen.blit(text3, text3_rect)

            

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

    clock.tick(60)
    time_taken += 1/60
    #text_rect.center = (950, 360)
    #screen.blit(text, text_rect)
    #text2_rect.center = (500, 360)
    #screen.blit(text2, text2_rect)
    #text3_rect.center = (640, 400)
    #screen.blit(text3, text3_rect)

    #if keys[pygame.K_UP]:
        #score = 0

    text_rect.center = (950, 360)
    screen.blit(text, text_rect)
    text2_rect.center = (500, 360)
    screen.blit(text2, text2_rect)

    pygame.display.update()