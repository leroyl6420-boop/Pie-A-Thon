# Welcome to the Pie-A-Thon! It's name is a play on the word Python, as, well, this game is coded in Python!
# This is my first software project, and even though I have coded using C++ before for my many Arduino projects,
# coding this game has made me realize that coding a microcontroller and coding a software project are two very 
# different things! I don't have to worry about the computer's speed, storage, and memory, but I need to deal 
# with more complicated rules and ideas!

import pygame
import sys
import time
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
HEIGHT = 600
WIDTH = 800
inminigame = False
clicks = 0
BG = pygame.image.load("Pie-A-Thon_BG.png").convert_alpha()
Bowl1 = pygame.image.load("Bowl1.png").convert_alpha()
Bowl2 = pygame.image.load("Bowl2.png").convert_alpha()
Bowl3 = pygame.image.load("Bowl3.png").convert_alpha()
Bowl4 = pygame.image.load("Bowl3.png").convert_alpha()
FallingFlour = pygame.image.load("FallingFlour.png").convert_alpha()
Flour1u = pygame.image.load("Flour1.png").convert_alpha()
Flour2u = pygame.image.load("Flour2.png").convert_alpha()
Flour3u = pygame.image.load("Flour3.png").convert_alpha()
Flour4u = pygame.image.load("Flour4.png").convert_alpha()
Flour1 = pygame.transform.scale(Flour1u, (350, 350))
Flour2 = pygame.transform.scale(Flour2u, (350, 350))
Flour3 = pygame.transform.scale(Flour3u, (350, 350))
Flour4 = pygame.transform.scale(Flour4u, (350, 350))
Spoon1 = pygame.image.load("Spoon1.png").convert_alpha()
Spoon2 = pygame.image.load("Spoon2.png").convert_alpha()
Spoon3 = pygame.image.load("Spoon3.png").convert_alpha()
Dough0 = pygame.image.load("Dough0.png").convert_alpha()
Dough1 = pygame.image.load("Dough1.png").convert_alpha()
Dough2 = pygame.image.load("Dough2.png").convert_alpha()
Dough3 = pygame.image.load("Dough3.png").convert_alpha()
Dough4 = pygame.image.load("Dough4.png").convert_alpha()
Crust0 = pygame.image.load("Crust0.png").convert_alpha()
Crust1 = pygame.image.load("Crust1.png").convert_alpha()
Crust2 = pygame.image.load("Crust2.png").convert_alpha()
Crust3 = pygame.image.load("Crust3.png").convert_alpha()
Crust4 = pygame.image.load("Crust4.png").convert_alpha()
Crust5 = pygame.image.load("Crust5.png").convert_alpha()
Strawberry0 = pygame.image.load("Strawberry1.png").convert_alpha()
Strawberry1 = pygame.image.load("Strawberry2.png").convert_alpha()
Strawberry2 = pygame.image.load("Strawberry3.png").convert_alpha()
Strawberry3 = pygame.image.load("Strawberry4.png").convert_alpha()
Water0 = pygame.image.load("Water1.png").convert_alpha()
Water1 = pygame.image.load("Water2.png").convert_alpha()
Water2 = pygame.image.load("Water3.png").convert_alpha()
Water3 = pygame.image.load("Water4.png").convert_alpha()
Water4 = pygame.image.load("Water5.png").convert_alpha()
BG_rect = BG.get_rect()
previous_angle = None
rotation_amount = 0
patch = pygame.Rect(50, 50, 750, 100)
pygame.display.set_caption("My First Python Game")
clock = pygame.time.Clock()
minigamescreen = pygame.Rect(50, 50, 700, 500)
player = pygame.Rect(100, 100, 50, 50)
wall1 = pygame.Rect(0, 250, 200, 50)
wall2 = pygame.Rect(0, 50, 800, 50)
crust = pygame.Rect(500, 500, 100, 100)
flour = pygame.Rect(0, 350, 100, 100)
dough = pygame.Rect(350, 500, 100, 100)
strawberries = pygame.Rect(0, 500, 100, 100)
Flour1_rect = Flour1.get_rect(topleft=(50, 200))
Flour2_rect = Flour2.get_rect(topleft=(50, 200))
Flour3_rect = Flour3.get_rect(topleft=(50, 200))
Flour4_rect = Flour4.get_rect(topleft=(50, 200))
Bowl1_rect = Bowl1.get_rect(topleft=(350, 350))
Bowl2_rect = Bowl2.get_rect(topleft=(350, 350))
Bowl3_rect = Bowl3.get_rect(topleft=(350, 350))
Bowl4_rect = Bowl4.get_rect(topleft=(350, 350))
Dough0_rect = Dough0.get_rect(topleft=(200, 100))
Dough1_rect = Dough1.get_rect(topleft=(200, 100))
Dough2_rect = Dough2.get_rect(topleft=(200, 100))
Dough3_rect = Dough3.get_rect(topleft=(200, 100))
Dough4_rect = Dough4.get_rect(topleft=(200, 100))
Curst0_rect = Crust0.get_rect(topleft=(200, 100))
Crust1_rect = Crust1.get_rect(topleft=(200, 100))
Crust2_rect = Crust2.get_rect(topleft=(200, 100))
Crust3_rect = Crust3.get_rect(topleft=(200, 100))
Crust4_rect = Crust4.get_rect(topleft=(200, 100))
Crust5_rect = Crust5.get_rect(topleft=(200, 100))
Strawberry0_rect = Strawberry0.get_rect(topleft=(200, 100))
Strawberry1_rect = Strawberry1.get_rect(topleft=(200, 100))
Strawberry2_rect = Strawberry2.get_rect(topleft=(200, 100))
Strawberry3_rect = Strawberry3.get_rect(topleft=(200, 100))

speed = 5

running = True

Flour = [Flour1, Flour2, Flour3, Flour4]
Flourstate = 0
Spoon = [Spoon1, Spoon2, Spoon3]
Spoonstate = 0
Bowlstate = 0
Bowl = [Bowl1, Bowl2, Bowl3, Bowl4]
Doughstate = 0
Dough = [Dough0, Dough1, Dough2, Dough3, Dough4]
Crust = [Crust0, Crust1, Crust2, Crust3, Crust4, Crust5]
Cruststate = 0
Water = [Water0, Water1, Water2, Water3, Water4]
Waterstate = 0
Strawberry = [Strawberry0, Strawberry1, Strawberry2, Strawberry3]
Strawberrystate = 0

# Font, Text, & Stuff

font = pygame.font.Font(None, 36)
crusttext1 = font.render("Crust", True, (255, 255, 255))
crusttext2 = font.render("Making", True, (255, 255, 255))
crusttext3 = font.render("Press E", True, (255, 255, 255))
flourtext1 = font.render("Flour", True, (255, 255, 255))
flourtext2 = font.render("Press E", True, (255, 255, 255))
doughtext1 = font.render("Dough", True, (255, 255, 255))
doughtext2 = font.render("Making", True, (255, 255, 255))
doughtext3 = font.render("Press E", True, (255, 255, 255))
crusttext4 = font.render("Cricle Mouse to Oil Dish!", True, (255, 255, 255))
crusttext5 = font.render("Left Click to Shape Crust!", True, (255, 255, 255))
flourtext3 = font.render("Scoop Flour!", True, (255, 255, 255))
doughtext4 = font.render("Circle Mouse to Knead!", True, (255, 255, 255))
strawberrytext1 = font.render("Straw-", True, (255, 255, 255))
strawberrytext2 = font.render("berries", True, (255, 255, 255))
strawberrytext3 = font.render("Press E", True, (255, 255, 255))
strawberrytext4 = font.render("Wash the Strawberries!", True, (255, 255, 255))
strawberrytext5 = font.render("Left Click to Mash!", True, (255, 255, 255))

fa = font.render("Flour Aquired!", True, (0, 255, 0))
da = font.render("Dough Aquired!", True, (0, 255, 0))
ca = font.render("Crust Aquried!", True, (0, 255, 0))
sa = font.render("+1 Strawberry!", True, (0, 255, 0))
missingflour = font.render("Missing Flour!", True, (255, 0, 0))
missingdough = font.render("Missing Dough!", True, (255, 0, 0))

dd = False
cd = False
fd = False
sd = False
hasflour = False
hasdough = False
hascrust = False
Strawberryammount = 0
clean = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("left click")
                clicks += 1
            if event.button == 3:
                print("right click")
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if player.colliderect(flour) or player.colliderect(crust) or player.colliderect(dough) or player.colliderect(strawberries):
                    inminigame = not inminigame

# MOVEMENT

    if inminigame == False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.y -= speed
            if player.colliderect(wall1):
                player.top = wall1.bottom
            if player.colliderect(wall2):
                player.top = wall2.bottom
        if keys[pygame.K_s]:
            player.y += speed
            if player.colliderect(wall1):
                player.bottom = wall1.top
            if player.colliderect(wall2):
                player.bottom = wall2.top
        if keys[pygame.K_a]:
            player.x -= speed
            if player.colliderect(wall1):
                player.left = wall1.right
            if player.colliderect(wall2):
                player.left = wall2.right
        if keys[pygame.K_d]:
            player.x += speed
            if player.colliderect(wall1):
                player.right = wall1.left
            if player.colliderect(wall2):
                player.right = wall2.left
        if keys[pygame.K_UP]:
            player.y -= speed
            if player.colliderect(wall1):
                player.top = wall1.bottom
            if player.colliderect(wall2):
                player.top = wall2.bottom
        if keys[pygame.K_DOWN]:
            player.y += speed
            if player.colliderect(wall1):
                player.bottom = wall1.top
            if player.colliderect(wall2):
                player.bottom = wall2.top
        if keys[pygame.K_RIGHT]:
            player.x += speed
            if player.colliderect(wall1):
                player.right = wall1.left
            if player.colliderect(wall2):
                player.right = wall2.left
        if keys[pygame.K_LEFT]:
            player.x -= speed
            if player.colliderect(wall1):
                player.left = wall1.right
            if player.colliderect(wall2):
                player.left = wall2.right
    else:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        Spoon1_rect = Spoon1.get_rect(topleft=(mouse_x, mouse_y))
        Spoon2_rect = Spoon2.get_rect(topleft=(mouse_x, mouse_y))
        Spoon3_rect = Spoon3.get_rect(topleft=(mouse_x, mouse_y))

# COLLISION

    if player.left < 0:
        player.left = 0
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.right > WIDTH:
        player.right = WIDTH

# MSC.



# DISPLAY

    screen.fill ((30, 30, 30))
    screen.blit(BG, (0, 0))
    pygame.draw.rect(screen, (0, 0, 255), crust)
    screen.blit(crusttext1, (500, 500))
    screen.blit(crusttext2, (500, 520))
    screen.blit(crusttext3, (500, 540))
    pygame.draw.rect(screen, (0, 0, 255), flour)
    screen.blit(flourtext1, (0, 350))
    screen.blit(flourtext2, (0, 370))
    pygame.draw.rect(screen, (0, 0, 255), dough)
    screen.blit(doughtext1, (350, 500))
    screen.blit(doughtext2, (350, 520))
    screen.blit(doughtext3, (350, 540))
    pygame.draw.rect(screen, (0, 0, 255), strawberries)
    screen.blit(strawberrytext1, (0, 500))
    screen.blit(strawberrytext2, (0, 520))
    screen.blit(strawberrytext3, (0, 540))
    pygame.draw.rect(screen, (255, 0,  0), player)
    pygame.draw.rect(screen, (193, 154, 107), wall1)
    pygame.draw.rect(screen, (115, 133, 149), wall2)
    if fd == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(fa, (player.x - 50, player.y - 30))
        else:
            fd = False
    if cd == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(ca, (player.x - 50, player.y - 30))
        else: 
            cd = False
    if dd == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(da, (player.x - 50, player.y - 30))
        else:
            dd = False
    if sd == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(sa, (player.x - 50, player.y - 30))
        else: sd = False
    if inminigame == True:
        pygame.draw.rect(screen, (128, 128, 128), minigamescreen)
        if player.colliderect(flour):
            screen.blit(flourtext3, (50, 50))
            screen.blit(Flour[Flourstate], (50, 200))
            screen.blit(Bowl[Bowlstate], (350, 350))
            screen.blit(Spoon[Spoonstate], (mouse_x - 200, mouse_y - 20))
            if Bowlstate >= 3:
                pygame.display.flip()
                time.sleep(1)
                inminigame = False
                hasflour = True
                Bowlstate = 0
                Spoonstate = 0
                Flourstate = 0
                fd = True
                text_cooldown = pygame.time.get_ticks() + 1000
            if Flour1_rect.colliderect(Spoon1_rect) and Spoonstate == 0:
                Flourstate += 1
                Spoonstate = 1
            if Spoonstate == 1 and mouse_x > 675:
                if (
                    Spoon2_rect.colliderect(Bowl1_rect)
                    or Spoon2_rect.colliderect(Bowl2_rect)
                    or Spoon2_rect.colliderect(Bowl3_rect)
                ):
                    Spoonstate = 2
                    Bowlstate += 1
                    Spoon_cooldown = pygame.time.get_ticks() + 1000
            if Spoonstate == 2:
                if pygame.time.get_ticks() >= Spoon_cooldown:
                    Spoonstate = 0

        if player.colliderect(dough) and hasflour == True:
            screen.blit(Dough[Doughstate], (200, 100))
            screen.blit(doughtext4, (50, 50))
            if Doughstate >= 4:
                screen.blit(Dough[4], (200, 100))
                pygame.display.flip()
                Doughstate = 0
                inminigame = False
                time.sleep(1)
                dd = True
                hasflour = False
                hasdough = True
                text_cooldown = pygame.time.get_ticks() + 1000
            dough_center = [400, 300]
            dx = mouse_x - dough_center[0]
            dy = mouse_y - dough_center[1]
            distance = math.sqrt(dx * dx + dy * dy)
            current_angle = math.atan2(dy, dx)
            if 50 < distance < 180:
                if previous_angle is not None:
                    angle_change = current_angle - previous_angle
                    if angle_change > math.pi:
                        angle_change -= 2 * math.pi
                    if angle_change < -math.pi:
                        angle_change += 2 * math.pi
                    rotation_amount += angle_change
            if abs(rotation_amount) >= 2 * math.pi:
                rotation_amount = 0
                Doughstate += 1
            previous_angle = current_angle

        if player.colliderect(crust) and hasdough == True:
            screen.blit(Crust[Cruststate], (200, 100))
            if Cruststate < 2:
                screen.blit(crusttext4, (50, 50))
                crust_center = [400, 300]
                dx = mouse_x - crust_center[0]
                dy = mouse_y - crust_center[1]
                distance = math.sqrt(dx * dx + dy * dy)
                current_angle = math.atan2(dy, dx)
                if 50 < distance < 180:
                    if previous_angle is not None:
                        angle_change = current_angle - previous_angle
                        if angle_change > math.pi:
                            angle_change -= 2 * math.pi
                        if angle_change < - math.pi:
                            angle_change += 2 * math.pi
                        rotation_amount += angle_change
                if abs(rotation_amount) >= 2 * math.pi:
                    rotation_amount = 0
                    Cruststate += 1
                previous_angle = current_angle
            if Cruststate > 1 and Cruststate < 4:
                screen.blit(crusttext5, (50, 50))
                if clicks >= 10:
                    Cruststate += 1
                    clicks = 0
            if Cruststate == 4:
                screen.blit(crusttext5, (50, 50))
                if clicks >= 10:
                    Cruststate = 5
                    screen.blit(Crust[Cruststate], (200, 100))
                    pygame.display.flip()
                    time.sleep(1)
                    Cruststate = 0
                    inminigame = False
                    cd = True
                    hascrust = True
                    hasdough = False
                    text_cooldown = pygame.time.get_ticks() + 1000
                    clicks = 0

        if player.colliderect(strawberries):
            screen.blit(Strawberry[Strawberrystate], (200, 100))
            if Strawberrystate >= 3:
                screen.blit(Strawberry[3], (200, 100))
                screen.blit(strawberrytext5, (50, 50))
                pygame.display.flip()
                time.sleep(1)
                Strawberrystate = 0
                clean = 0
                clicks = 0
                inminigame = False
                Strawberryammount += 1
                text_cooldown = pygame.time.get_ticks() + 1000
                sd = True
            if clean < 300: 
                screen.blit(strawberrytext4, (50, 50))
                if 300 < mouse_x and mouse_x < 500 and mouse_y > 200 and 400 > mouse_y:
                    screen.blit(Water[Waterstate], (mouse_x - 100, mouse_y - 100))
                    if not Waterstate == 4:
                        Waterstate += 1
                    else:
                        Waterstate = 0
                    clean += 1
            if clean >= 300 and Strawberrystate < 3:
                screen.blit(strawberrytext5, (50, 50))
                if clicks >= 10:
                    Strawberrystate += 1
                    clicks = 0
        if player.colliderect(crust) and hasdough == False:
            screen.blit(missingdough, (310, 290))
        if player.colliderect(dough) and hasflour == False:
            screen.blit(missingflour, (310, 290))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
