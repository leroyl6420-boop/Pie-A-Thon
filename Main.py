# Welcome to the Pie-A-Thon! It's name is a play on the word Python, as, well, this game is coded in Python!
# This is my first software project, and even though I have coded using C++ before for my many Arduino projects,
# coding this game has made me realize that coding a microcontroller and coding a software project are two very 
# different things! I don't have to worry about the computer's speed, storage, and memory, but I need to deal 
# with more complicated rules and ideas!

import pygame
import sys
import time
import math
import os 
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)
pygame.init()
screen = pygame.display.set_mode((800, 600))
HEIGHT = 600
WIDTH = 800
inminigame = False

# Change to True if you want cheats! 

CHEATS = False

clicks = 0
BG = pygame.image.load("Pie-A-Thon_BG.png").convert_alpha()
Bowl1 = pygame.image.load("Bowl1.png").convert_alpha()
Bowl2 = pygame.image.load("Bowl2.png").convert_alpha()
Bowl3 = pygame.image.load("Bowl3.png").convert_alpha()
Bowl4 = pygame.image.load("Bowl4.png").convert_alpha()
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
Pumpkin = pygame.image.load("Pumpkin.png").convert_alpha()
Apple = pygame.image.load("Apples.png").convert_alpha()
Blueberry = pygame.image.load("Blueberries.png").convert_alpha()
Cherry = pygame.image.load("Cherries.png").convert_alpha()                 
Machine  = pygame.image.load("Machine.png").convert_alpha()
Cranku = pygame.image.load("Crank.png").convert_alpha()           
Oven = pygame.image.load("Oven.png").convert_alpha()
Crank = pygame.transform.scale(Cranku, (25, 200))
Pumpkind = pygame.transform.scale(Pumpkin, (50, 100))
Appled = pygame.transform.scale(Apple, (50, 100))
Blueberryd = pygame.transform.scale(Blueberry, (50, 100))
Cherryd = pygame.transform.scale(Cherry, (50, 100))
Blueberryjam = pygame.image.load("Blueberryjam.png").convert_alpha()
Cherryjam = pygame.image.load("Cherryjam.png").convert_alpha()
Pumpkinjam = pygame.image.load("Pumpkinjam.png").convert_alpha()
Applejam = pygame.image.load("Applejam.png").convert_alpha()
Customer1u = pygame.image.load("Customer1.png").convert_alpha()
Customer2u = pygame.image.load("Customer2.png").convert_alpha()
Customer3u = pygame.image.load("Customer3.png").convert_alpha()
Customer4u = pygame.image.load("Customer4.png").convert_alpha()
Customer5u = pygame.image.load("Customer5.png").convert_alpha()
Customer6u = pygame.image.load("Customer6.png").convert_alpha()
Customer7u = pygame.image.load("Customer7.png").convert_alpha()
Customer8u = pygame.image.load("Customer8.png").convert_alpha()
Customer9u = pygame.image.load("Customer9.png").convert_alpha()
Customer1 = pygame.transform.scale(Customer1u, (50, 50))
Customer2 = pygame.transform.scale(Customer2u, (50, 50))
Customer3 = pygame.transform.scale(Customer3u, (50, 50))
Customer4 = pygame.transform.scale(Customer4u, (50, 50))
Customer5 = pygame.transform.scale(Customer5u, (50, 50))
Customer6 = pygame.transform.scale(Customer6u, (50, 50))
Customer7 = pygame.transform.scale(Customer7u, (50, 50))
Customer8 = pygame.transform.scale(Customer8u, (50, 50))
Customer9 = pygame.transform.scale(Customer9u, (50, 50))
pivotx = 13
pivoty = 13
pivot_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
pivot_center = pivot_surface.get_rect().center
pivot_surface.blit(
    Crank,
    (
        pivot_center[0] - pivotx,
        pivot_center[1] - pivoty
    )
)
axlex = 475
axley = 325
crank_angle = 269
BG_rect = BG.get_rect()
previous_angle = None
rotation_amount = 0
patch = pygame.Rect(50, 50, 750, 100)
pygame.display.set_caption("My First Python Game")
clock = pygame.time.Clock()
minigamescreen = pygame.Rect(50, 50, 700, 500)
player = pygame.Rect(100, 100, 50, 50)
playerup = pygame.image.load("Up.png").convert_alpha()
playerright = pygame.image.load("Right.png").convert_alpha()
playerdown = pygame.image.load("Down.png").convert_alpha()
playerleft = pygame.image.load("Left.png").convert_alpha()
wall2 = pygame.Rect(0, 50, 800, 50)
crust = pygame.Rect(450, 500, 100, 100)
flour = pygame.Rect(0, 350, 100, 100)
dough = pygame.Rect(300, 500, 100, 100)
strawberries = pygame.Rect(0, 500, 100, 100)
shelf1 = pygame.Rect(50, 50, 50, 500)
shelf2 = pygame.Rect(100, 50, 600, 50)
shelf3 = pygame.Rect(700, 50, 50, 500)
shelf4 = pygame.Rect(100, 400, 600, 50)
jam = pygame.Rect(150, 500, 100, 100)
trash = pygame.Rect(0, 200, 100, 100)
assembly = pygame.Rect(600, 500, 100, 100)
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
Oven1_rect = Oven.get_rect(topleft=(700, 200))
Oven2_rect = Oven.get_rect(topleft=(700, 350))
Oven1_hitbox = pygame.Rect(650, 200, 50, 100)
Oven2_hitbox = pygame.Rect(650, 350, 50, 100)
Serve_hitbox = pygame.Rect(50, 100, 50, 50)

speed = 5
earliestspot = 30
progress1 = 0
progress2 = 0
pumpkinjamclickareaxstart = 0
pumpkinjamclickareaxend = 0
cherryjamclickareaxstart = 0
cherryjamclickareaxend = 0
blueberryjamclickareaxstart = 0
blueberryjamclickareaxend = 0
applejamclickareaxstart = 0
applejamclickareaxend = 0
assemblydisplayleft = 0
assemblydisplayright = 0
assemblydisplayleftlist = []
assemblydisplayrightlist = []
assemblydisplayleftliststate = -1
assemblydisplayrightliststate = -1
pielist = []
pieliststate = -1
pa = False
running = True
oven1on = False
oven2on = False
oven1count = 9999999999999
oven2count = 9999999999999
progress1color = 0
progress2color = 0
customerx = 750
lastcustomerspawntimer = -1
linestate = 0
haspie = False
customerdisplaystate = 0
Customerstate = [Customer1, Customer2, Customer3, Customer4, Customer5, Customer6, Customer7, Customer8, Customer9]
Customerstatestate = 0
playerpielist = []
hasbakedpie = False

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
LeftClick = False
LastClick = False

# Font, Text, & Stuff 

font = pygame.font.Font(None, 36)
assemblytext4 = font.render("Missing Crust!", True, (255, 0, 0))
assemblytext5 = font.render("Missing Jams!", True, (255, 0, 0))
assemblytext6 = font.render("Missing Crust and Jams!", True, (255, 0, 0))
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
strawberrytext1 = font.render("Ingred-", True, (255, 255, 255))
strawberrytext2 = font.render("ients", True, (255, 255, 255))
strawberrytext3 = font.render("Press E", True, (255, 255, 255))
jamtext1 = font.render("Jam", True, (255, 255, 255))
jamtext2 = font.render("Making", True, (255, 255, 255))
jamtext3 = font.render("Press E", True, (255, 255, 255))
jamtext4 = font.render("Turn Crank Clockwise to Make Jam!", True, (255, 255, 255))
trashtext1 = font.render("Trash", True, (255, 255, 255))
trashtext2 = font.render("Press E", True, (255, 255, 255))
assemblytext1 = font.render("Assem-", True, (255, 255, 255))
assemblytext2 = font.render("bly", True, (255, 255, 255))
assemblytext3 = font.render("Press E", True, (255, 255, 255))
assemblytext7 = font.render("Acquired Assembled Pie!", True, (0, 255, 0))
servetext1 = font.render("Served a Pie!", True, (0, 255, 0))
bakedpieacquiredtext = font.render("Acquired Baked Pie!", True, (0, 255, 0))
points = 0

fa = font.render("Flour Aquired!", True, (0, 255, 0))
da = font.render("Dough Aquired!", True, (0, 255, 0))
ca = font.render("Crust Aquried!", True, (0, 255, 0))
missingflour = font.render("Missing Flour!", True, (255, 0, 0))
missingdough = font.render("Missing Dough!", True, (255, 0, 0))
jamtext5 = font.render("Missing Ingredients!", True, (255, 0, 0))
strawberrytext4 = font.render("Max Ingredients!", True, (255, 0, 0))
alreadyhavepietext = font.render("Maxxed Pies!", True, (255, 0, 0))
alreadyhavepie = False

served = False
dd = False
cd = False
fd = False
sd = False
td = False
hasflour = False
hasdough = False
hascrust = False
Strawberryammount = 0
clean = 0
jd = False
bakedpieacquired = False

blueberries = 0
pumpkins = 0
apples = 0
cherries = 0
blueberryjam = 0
pumpkinjam = 0
cherryjam = 0
applejam = 0
assemblydisplay = 0
spawn = False

fruits = []
fruitstate = -1
playerstate = 0
oven1pie = []
oven2pie = []

rotated_crank = pygame.transform.rotate(
    pivot_surface,
    crank_angle
    )
rotated_rect = rotated_crank.get_rect(
    center=(axlex, axley)
    )
prevoius_crank_angle = 269
crank_angle = 269

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("left click")
                clicks += 1

                #CHEATS
                if CHEATS == True:
                    if player.colliderect(trash):    
                        hascrust = True
                        applejam = 3
                        blueberryjam = 3
                        pumpkinjam = 2
                        cherryjam = 2
                    linestate += 1

                
            if event.button == 3:
                print("right click")
                if CHEATS == True:
                    linestate -= 1
                    Customerstatestate += 1

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if player.colliderect(flour) or player.colliderect(jam) or player.colliderect(assembly) or player.colliderect(crust) or player.colliderect(dough) or player.colliderect(strawberries):
                    inminigame = not inminigame
                if player.colliderect(assembly) and inminigame == False and pieliststate > -1:
                    pa = True
                    text_cooldown = pygame.time.get_ticks() + 1000
                    haspie = True
                    hascrust = False
                if player.colliderect(strawberries) and inminigame == False:
                    sd = True
                    pumpa = font.render(f"Acquired {pumpkins} Pumpkins!", True, (0, 255, 0))
                    if pumpkins == 1:
                        pumpa = font.render(f"Acquired a Pumpkin!", True, (0, 255, 0))
                    applea = font.render(f"Acquired {apples} Apples!", True, (0, 255, 0))
                    if apples == 1:
                        applea = font.render(f"Acquired an Apple!", True, (0, 255, 0))
                    cherrya = font.render(f"Acquired {cherries} Cherries!", True, (0, 255, 0))
                    if cherries == 1:
                        cherrya = font.render(f"Acquired a Cherry!", True, (0, 255, 0))
                    bluea = font.render(f"Acquired {blueberries} Blueberries!", True, (0, 255, 0))
                    if blueberries == 1:
                        bluea = font.render(f"Acquired a Blueberry!", True, (0, 255, 0))
                    text_cooldown = pygame.time.get_ticks() + 1000
                if player.colliderect(trash):
                    pumpn = font.render(f"Trashed {pumpkins} Pumpkins!", True, (255, 0, 0))
                    if pumpkins == 1:
                        pumpn = font.render(f"Trashed a Pumpkin!", True, (255, 0, 0))
                    bluen = font.render(f"Trashed {blueberries} Blueberries!", True, (255, 0, 0))
                    if blueberries == 1:
                        bluen = font.render(f"Trashed a Blueberry!", True, (255, 0, 0))
                    applen = font.render(f"Trashed {apples} Apples!", True, (255, 0, 0))
                    if apples == 1:
                        applen = font.render(f"Trashed an Apple!", True, (255, 0, 0))
                    cherryn = font.render(f"Trashed {cherries} Cherries!", True, (255, 0, 0))
                    if cherries == 1:
                        cherryn = font.render(f"Trashed a Cherry!", True, (255, 0, 0))
                    pumpkins = 0
                    blueberries = 0
                    apples = 0
                    cherries = 0
                    fruitstate = -1
                    td = True
                    text_cooldown = pygame.time.get_ticks() + 1000
                    inminigame = False
                if player.colliderect(jam) and inminigame == False:
                    applejama = font.render(f"Acquired {applejam} Apple Jams!", True, (0, 255, 0))
                    if applejam == 1:
                        applejama = font.render(f"Acquired an Apple Jam!", True, (0, 255, 0))
                    cherryjama = font.render(f"Acquired {cherryjam} Cherry Jams!", True, (0, 255, 0))
                    if cherryjam == 1:
                        cherryjama = font.render(f"Acquired a Cherry Jam!", True, (0, 255, 0))
                    pumpkinjama = font.render(f"Acquired {pumpkinjam} Pumpkin Jams!", True, (0, 255, 0))
                    if pumpkinjam == 1:
                        pumpkinjama = font.render(f"Acquired a Pumpkin Jam!", True, (0, 255, 0))
                    blueberryjama = font.render(f"Acquired {blueberryjam} Blueberry Jams!", True, (0, 255, 0))
                    if blueberryjam == 1:
                        blueberryjama = font.render(f"Acquired a Blueberry Jam!", True, (0, 255, 0))
                    jd == True
                    text_cooldown = pygame.time.get_ticks() + 1000
                if player.colliderect(Oven1_hitbox) and pieliststate > -1 and not oven1on:
                    oven1pie = pielist.copy()
                    pielist.clear()
                    assemblydisplayright = 0
                    assemblydisplayleft = 0
                    assemblydisplayleftlist.clear()
                    assemblydisplayrightlist.clear()
                    assemblydisplayleftliststate = -1
                    assemblydisplayrightliststate = -1
                    hascrust = False
                    pieliststate = -1
                    oven1on = True
                    oven1count = pygame.time.get_ticks() + 8000
                if player.colliderect(Oven2_hitbox) and pieliststate > -1 and not oven2on:
                    pielist.clear()
                    assemblydisplayright = 0
                    assemblydisplayleft = 0
                    assemblydisplayleftlist.clear()
                    assemblydisplayrightlist.clear()
                    assemblydisplayleftliststate = -1
                    assemblydisplayrightliststate = -1
                    hascrust = False
                    oven2pie = pielist.copy()
                    pieliststate = -1
                    oven2on = True
                    oven2count = pygame.time.get_ticks() + 8000
                if oven1count - pygame.time.get_ticks() < 2000 and player.colliderect(Oven1_hitbox):
                    if hasbakedpie == False:
                        oven1on = False
                        hasbakedpie = True
                        bakedpieacquired = True
                        text_cooldown = pygame.time.get_ticks() + 1000
                    else: 
                        alreadyhavepie = True
                        text_cooldown = pygame.time.get_ticks() + 1000
                if oven2count - pygame.time.get_ticks() < 2000 and player.colliderect(Oven2_hitbox):
                    if hasbakedpie == False:
                        hasbakedpie = True
                        bakedpieacquired = True
                        oven2on = False
                        text_cooldown = pygame.time.get_ticks() + 1000
                    else:
                        alreadyhavepie = True
                        text_cooldown = pygame.time.get_ticks() + 1000
                if player.colliderect(Serve_hitbox) and hasbakedpie == True:
                    hasbakedpie = False
                    served = True
                    linestate -= 1
                    Customerstatestate += 1
                    points += 1
                    text_cooldown = pygame.time.get_ticks() + 1000

# MOVEMENT 

    if inminigame == False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.y -= speed
            playerstate = 1
            if player.colliderect(wall2):
                player.top = wall2.bottom
            if player.colliderect(Oven1_rect):
                player.top = Oven1_rect.bottom
            if player.colliderect(Oven2_rect):
                player.top = Oven2_rect.bottom
        if keys[pygame.K_s]:
            player.y += speed
            playerstate = 3
            if player.colliderect(wall2):
                player.bottom = wall2.top
            if player.colliderect(Oven1_rect):
                player.bottom = Oven1_rect.top
            if player.colliderect(Oven2_rect):
                player.bottom = Oven2_rect.top
        if keys[pygame.K_a]:
            player.x -= speed
            playerstate = 2
            if player.colliderect(wall2):
                player.left = wall2.right
            if player.colliderect(Oven1_rect):
                player.left = Oven1_rect.right
            if player.colliderect(Oven2_rect):
                player.left = Oven2_rect.right
        if keys[pygame.K_d]:
            player.x += speed
            playerstate = 0
            if player.colliderect(wall2):
                player.right = wall2.left
            if player.colliderect(Oven1_rect):
                player.right = Oven1_rect.left
            if player.colliderect(Oven2_rect):
                player.right = Oven2_rect.left
        if keys[pygame.K_UP]:
            player.y -= speed
            playerstate = 1
            if player.colliderect(wall2):
                player.top = wall2.bottom
            if player.colliderect(Oven1_rect):
                player.top = Oven1_rect.bottom
            if player.colliderect(Oven2_rect):
                player.top = Oven2_rect.bottom
        if keys[pygame.K_DOWN]:
            player.y += speed
            playerstate = 3
            if player.colliderect(wall2):
                player.bottom = wall2.top
            if player.colliderect(Oven1_rect):
                player.bottom = Oven1_rect.top
            if player.colliderect(Oven2_rect):
                player.bottom = Oven2_rect.top
        if keys[pygame.K_RIGHT]:
            player.x += speed
            playerstate = 0
            if player.colliderect(wall2):
                player.right = wall2.left
            if player.colliderect(Oven1_rect):
                player.right = Oven1_rect.left
            if player.colliderect(Oven2_rect):
                player.right = Oven2_rect.left
        if keys[pygame.K_LEFT]:
            player.x -= speed
            playerstate = 2
            if player.colliderect(wall2):
                player.left = wall2.right
            if player.colliderect(Oven1_rect):
                player.left = Oven1_rect.right
            if player.colliderect(Oven2_rect):
                player.left = Oven2_rect.right
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

    customerspawntimer = pygame.time.get_ticks() // 20000
    if customerspawntimer > lastcustomerspawntimer:
        spawn = True
        linestate += 1
    lastcustomerspawntimer = customerspawntimer


# DISPLAY

    screen.fill ((30, 30, 30))
    screen.blit(BG, (0, 0))    
    pointstext = font.render(f"Points: {points}", True, (0, 255, 0))
    screen.blit(pointstext, (650, 0))

    Customerstatestatequotient = Customerstatestate // 9
    Customerstatestateremainder = Customerstatestate - (Customerstatestatequotient * 9)
    endshow = Customerstatestateremainder + linestate
    Customercount = Customerstatestateremainder
    Cycle = Customerstatestateremainder
    linestatecount = 1
    while Cycle < endshow:
        linex = linestatecount * 50
        screen.blit(Customerstate[(Customercount)], (linex, 0))
        if Customercount < 8:
            Customercount += 1
        else:
            Customercount = 0
        linestatecount += 1
        Cycle += 1
    print (Customerstatestateremainder)

    pygame.draw.rect(screen, (0, 0, 255), crust)
    screen.blit(crusttext1, (450, 500))
    screen.blit(crusttext2, (450, 520))
    screen.blit(crusttext3, (450, 540))
    pygame.draw.rect(screen, (0, 0, 255), Serve_hitbox)
    pygame.draw.rect(screen, (0, 0, 255), flour)
    screen.blit(flourtext1, (0, 350))
    screen.blit(flourtext2, (0, 370))
    pygame.draw.rect(screen, (0, 0, 255), dough)
    screen.blit(doughtext1, (300, 500))
    screen.blit(doughtext2, (300, 520))
    screen.blit(doughtext3, (300, 540))
    pygame.draw.rect(screen, (0, 0, 255), strawberries)
    screen.blit(strawberrytext1, (0, 500))
    screen.blit(strawberrytext2, (0, 520))
    screen.blit(strawberrytext3, (0, 540))
    pygame.draw.rect(screen, (0, 0, 255), jam)
    screen.blit(jamtext1, (150, 500))
    screen.blit(jamtext2, (150, 520))
    screen.blit(jamtext3, (150, 540))
    pygame.draw.rect(screen, (0, 0, 255), trash)
    screen.blit(trashtext1, (0, 200))
    screen.blit(trashtext2, (0, 220))
    pygame.draw.rect(screen, (0, 0, 255), assembly)
    screen.blit(assemblytext1, (600, 500))
    screen.blit(assemblytext2, (600, 520))
    screen.blit(assemblytext3, (600, 540))
    if playerstate == 0:
        screen.blit(playerright, (player.x, player.y))
    if playerstate == 1:
        screen.blit(playerup, (player.x, player.y))
    if playerstate == 2:
        screen.blit(playerleft, (player.x, player.y))
    if playerstate == 3:
        screen.blit(playerdown, (player.x, player.y))
    pygame.draw.rect(screen, (115, 133, 149), wall2)
    screen.blit(Oven, (700, 200))
    if bakedpieacquired == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(bakedpieacquiredtext, (player.x - 100, player.y - 30))
        else:
            bakedpieacquired = False
    if alreadyhavepie == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(alreadyhavepietext, (player.x - 100, player.y - 30))
        else:
            alreadyhavepie = False
    if oven1on == True:
        if oven1count - pygame.time.get_ticks() > 6000:
            progress1 = 20
            progress1color = (255, 255, 0)
        if oven1count - pygame.time.get_ticks() > 4000 and oven1count - pygame.time.get_ticks() < 6000:
            progress1 = 40
            progress1color = (255, 255, 0)
        if oven1count - pygame.time.get_ticks() > 2000 and oven1count - pygame.time.get_ticks() < 4000:
            progress1 = 60
            progress1color = (255, 255, 0)
        if oven1count - pygame.time.get_ticks() > 0 and oven1count- pygame.time.get_ticks() < 2000:
            progress1 = 80
            progress1color = (0, 255, 0)
        if oven1count - pygame.time.get_ticks() < -7000:
            progress1 = 80
            progress1color = (255, 0, 0)
        bar1 = pygame.Rect(730, 210, 10, progress1)
        pygame.draw.rect(screen, (progress1color), bar1)
    screen.blit(Oven, (700, 350))
    if oven2on == True:
        if oven2count - pygame.time.get_ticks() > 6000:
            progress2 = 20
            progress2color = (255, 255, 0)
        if oven2count - pygame.time.get_ticks() > 4000 and oven2count - pygame.time.get_ticks() < 6000:
            progress2 = 40
            progress2color = (255, 255, 0)
        if oven2count - pygame.time.get_ticks() > 2000 and oven2count - pygame.time.get_ticks() < 4000:
            progress2 = 60
            progress2color = (255, 255, 0)
        if oven2count - pygame.time.get_ticks() > 0 and oven2count - pygame.time.get_ticks() < 2000:
            progress2 = 80
            progress2color = (0, 255, 0)
        if oven2count - pygame.time.get_ticks() < -7000:
            progress2 = 80
            progress2color = (255, 0, 0)
        bar2 = pygame.Rect(730, 360, 10, progress2)
        pygame.draw.rect(screen, (progress2color), bar2)
    if served == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(servetext1, (player.x - 50, player.y - 30))
        else:
            served = False
    if pa == True:
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(assemblytext7, (player.x - 120, player.y - 30))
        else:
            pa = False
    if jd == True:
        earliestspot = 30
        if pygame.time.get_ticks() < text_cooldown:
            if pumpkinjam > 0:
                screen.blit(pumpkinjama, (player.x - 100, player.y - earliestspot))
                earliestspot += 20
            if blueberryjam > 0:
                screen.blit(blueberryjama, (player.x - 100, player.y - earliestspot))
                earliestspot += 20
            if cherryjam > 0:
                screen.blit(cherryjama, (player.x - 100, player.y - earliestspot))
                earliestspot += 20
            if applejam > 0:
                screen.blit(applejama, (player.x - 100, player.y - earliestspot))
        else:
            jd = False
    if td == True:
        earliestspot = 30
        if pygame.time.get_ticks() < text_cooldown:
            screen.blit(pumpn, (player.x - 80, player.y - earliestspot))
            earliestspot += 20
            screen.blit(bluen, (player.x - 80, player.y - earliestspot))
            earliestspot += 20
            screen.blit(cherryn, (player.x - 80, player.y - earliestspot))
            earliestspot += 20
            screen.blit(applen, (player.x - 80, player.y - earliestspot))
        else:
            td = False
    if sd == True:
        earliestspot = 30
        if pygame.time.get_ticks() < text_cooldown:
            if pumpkins > 0:
                screen.blit(pumpa, (player.x - 80, player.y - earliestspot))
                earliestspot += 20
            if blueberries > 0:
                screen.blit(bluea, (player.x - 80, player.y - earliestspot))
                earliestspot += 20
            if cherries > 0:
                screen.blit(cherrya, (player.x - 80, player.y - earliestspot))
                earliestspot += 20
            if apples > 0:
                screen.blit(applea, (player.x - 80, player.y - earliestspot))
        else: 
            sd = False
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

        if player.colliderect(strawberries) and fruitstate < 9:
            pygame.draw.rect(screen, (193, 154, 107), shelf1)
            pygame.draw.rect(screen, (193, 154, 107), shelf2)
            pygame.draw.rect(screen, (193, 154, 107), shelf3)
            pygame.draw.rect(screen, (193, 154, 107), shelf4)
            screen.blit(font.render(f"Blueberries: {blueberries}", True, (255, 255, 255)), (100, 475))
            screen.blit(font.render(f"Pumpkins: {pumpkins}", True, (255, 255, 255)), (100, 450))
            screen.blit(font.render(f"Apples: {apples}", True, (255, 255, 255)), (100, 525))
            screen.blit(font.render(f"Cherries: {cherries}", True, (255, 255, 255)), (100, 500))
            screen.blit(Pumpkin, (100, 100))
            screen.blit(Blueberry, (250, 100))
            screen.blit(Cherry, (400, 100))
            screen.blit(Apple, (550, 100))
            LeftClick = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    LeftClick = True
            if LastClick == False and LeftClick == True:
                if mouse_y > 100 and mouse_y < 400 and fruitstate < 9:
                    if mouse_x > 100 and mouse_x < 250:
                        pumpkins += 1
                        fruits.append("pumpkin")
                        fruitstate += 1
                        if fruitstate > 8:
                            inminigame = False
                            pumpa = font.render(f"Acquired {pumpkins} Pumpkins!", True, (0, 255, 0))
                            if pumpkins == 1:
                                pumpa = font.render(f"Acquired a Pumpkin!", True, (0, 255, 0))
                            bluea = font.render(f"Acquired {blueberries} Blueberries!", True, (0, 255, 0))
                            if blueberries == 1:
                                bluea = font.render(f"Acquired a Blueberry!", True, (0, 255, 0))
                            cherrya = font.render(f"Acquired {cherries} Cherries!", True, (0, 255, 0))
                            if cherries == 1: 
                                font.render(f"Acquried a Cherry!", True, (0, 255, 0))
                            applea = font.render(f"Acquired {apples} Apples!", True, (0, 255, 0))
                            if apples == 1:
                                applea = font.render(f"Acquired an Apple!", True, (0, 255, 0))
                            text_cooldown = pygame.time.get_ticks() + 1000
                            sd = True
                    if mouse_x > 250 and mouse_x < 400:
                        blueberries += 1
                        fruits.append("blueberry")
                        fruitstate += 1
                        if fruitstate > 8:
                            inminigame = False
                            pumpa = font.render(f"Acquired {pumpkins} Pumpkins!", True, (0, 255, 0))
                            if pumpkins == 1:
                                pumpa = font.render(f"Acquired a Pumpkin!", True, (0, 255, 0))
                            applea = font.render(f"Acquired {apples} Apples!", True, (0, 255, 0))
                            if apples == 1:
                                applea = font.render(f"Acquired an Apple!", True, (0, 255, 0))
                            bluea = font.render(f"Acquired {blueberries} Blueberries!", True, (0, 255, 0))
                            if blueberries == 1:
                                bluea = font.render(f"Acquired a Bluebery!", True, (0, 255, 0))
                            cherrya = font.render(f"Acquired {cherries} Cherries!", True, (0, 255, 0))
                            if cherries == 1:
                                cherrya = font.render(f"Acquried a Cherry!", True, (0, 255, 255))
                            text_cooldown = pygame.time.get_ticks() + 1000
                            sd = True
                    if mouse_x > 400 and mouse_x < 550:
                        cherries += 1
                        fruits.append("cherry")
                        fruitstate += 1
                        if fruitstate > 8:
                            inminigame = False
                            sd = True
                            pumpa = font.render(f"Acquired {pumpkins} Pumpkins!", True, (0, 255, 0))
                            if pumpkins == 1:
                                pumpa = font.render(f"Acquired a Pumpkin!", True, (0, 255, 0))
                            applea = font.render(f"Acquried {apples} Apples!", True, (0, 255, 0))
                            if apples == 1:
                                applea = font.render(f"Acquired an Apple!", True, (0, 255, 0))
                            bluea = font.render(f"Acquired {blueberries} Blueberries!", True, (0, 255, 0))
                            if blueberries == 1:
                                bluea = font.render(f"Acquired a Blueberry!", True, (0, 255, 0))
                            cherrya = font.render(f"Acquired {cherries} Cherries!", True, (0, 255, 0))
                            if cherries == 1:
                                cherrya = font.render(f"Acquired a Cherry!", True, (0, 255, 0))
                            text_cooldown = pygame.time.get_ticks() + 1000
                    if mouse_x > 550 and mouse_x < 700:
                        apples += 1
                        fruits.append("apple")
                        fruitstate+=1
                        if fruitstate > 8:
                            inminigame = False
                            sd = True
                            pumpa = font.render(f"Acquired {pumpkins} Pumpkins!", True, (0, 255, 0))
                            if pumpkins == 1:
                                pumpa = font.render(f"Acquired a Pumpkin!", True, (0, 255, 0))
                            applea = font.render(f"Acquired {apples} Apples!", True, (0, 255, 0))
                            if apples == 1:
                                applea = font.render(f"Acquired an Apple!", True, (0, 255, 0))
                            cherrya = font.render(f"Acquired {cherries} Cherries!", True, (0, 255, 0))
                            if cherries == 1:
                                cherrya = font.render(f"Acquired a Cherry!", True, (0, 255, 0))
                            bluea = font.render(f"Acquired {blueberries} Blueberries!", True, (0, 255, 0))
                            if blueberries == 1:
                                bluea = font.render(f"Acquired a Blueberry!", True, (0, 255, 0))
                            text_cooldown = pygame.time.get_ticks() + 1000

            LastClick = LeftClick

        if player.colliderect(jam) and fruitstate == -1:
            screen.blit(jamtext5, (280, 290))

        if player.colliderect(jam) and fruitstate > -1:
                screen.blit(jamtext4, (50, 50))
                fruitdisplay = fruitstate
                while fruitdisplay > -1:
                    fruitdisplayx = fruitdisplay * 40
                    if fruits[fruitdisplay] == "pumpkin":
                        screen.blit(Pumpkind, (fruitdisplayx + 200, 150))
                    if fruits[fruitdisplay] == "blueberry":
                        screen.blit(Blueberryd, (fruitdisplayx + 200, 150))
                    if fruits[fruitdisplay] == "cherry":
                        screen.blit(Cherryd, (fruitdisplayx + 200, 150))
                    if fruits[fruitdisplay] == "apple":
                        screen.blit(Appled, (fruitdisplayx + 200, 130))
                    fruitdisplay -= 1
                screen.blit(Machine, (100, 100))
                dx = mouse_x - axlex
                dy = mouse_y - axley
                mouse_angle = 90 - math.degrees(math.atan2(dy, dx))
                
                if math.sqrt(dx * dx + dy * dy) > 150 and math.sqrt(dx * dx + dy * dy) < 250:
                    rotated_crank = pygame.transform.rotate(
                    pivot_surface,
                    crank_angle
                    )
                    rotated_rect = rotated_crank.get_rect(
                        center=(axlex, axley)
                    )
                    if prevoius_crank_angle >= -90 and mouse_angle > 260 and prevoius_crank_angle <= -89:
                        crank_angle = mouse_angle 
                        print(fruits[fruitstate])
                        if fruits[fruitstate] == "apple":
                            apples -= 1
                            applejam += 1
                        if fruits[fruitstate] == "pumpkin":
                            pumpkins -= 1
                            pumpkinjam += 1
                        if fruits[fruitstate] == "cherry":
                            cherries -= 1
                            cherryjam += 1
                        if fruits[fruitstate] == "blueberry":
                            blueberries -= 1
                            blueberryjam += 1
                        fruits.pop(fruitstate)
                        fruitstate -= 1
                        if fruitstate == -1:
                            inminigame = False
                            crank_angle = 269
                            prevoius_crank_angle = 269
                            jd = True
                            applejama = font.render(f"Acquired {applejam} Apple Jams!", True, (0, 255, 0))
                            if applejam == 1:
                                applejama = font.render(f"Acquired an Apple Jam!", True, (0, 255, 0))
                            blueberryjama = font.render(f"Acquired {blueberryjam} Blueberry Jams!", True, (0, 255, 0))
                            if blueberryjam == 1:
                                blueberryjama = font.render(f"Acquired a Blueberry Jam!", True, (0, 255, 0))
                            pumpkinjama = font.render(f"Acquired {pumpkinjam} Pumpkin Jams!", True, (0, 255, 0))
                            if pumpkinjam == 1:
                                pumpkinjama = font.render(f"Acquired a Pumpkin Jam!", True, (0, 255, 0))
                            cherryjama = font.render(f"Acquired {cherryjam} Cherry Jams!", True, (0, 255, 0))
                            if cherryjam == 1:
                                cherryjama = font.render(f"Acquired a Cherry Jam!", True, (0, 255, 0))
                            text_cooldown = pygame.time.get_ticks() + 1000
                    if prevoius_crank_angle >= mouse_angle and mouse_angle + 10 > prevoius_crank_angle:
                        crank_angle = mouse_angle
                    prevoius_crank_angle = crank_angle
                screen.blit(rotated_crank, rotated_rect)

        if player.colliderect(assembly) and hascrust == True:
            if applejam > 0 or blueberryjam > 0 or pumpkinjam > 0 or cherryjam > 0:
                screen.blit(Crust5, (200, 62.5))
                assemblydisplay = blueberryjam + pumpkinjam + cherryjam + applejam
                while assemblydisplay > 0:
                    assemblydisplayx = assemblydisplay * 50
                    if pumpkinjam > 0:
                        pumpkindisplay = pumpkinjam
                        assemblydisplayx = assemblydisplay * 50
                        pumpkinjamclickareaxend = assemblydisplayx + 150
                        while pumpkindisplay > 0:
                            assemblydisplayx = assemblydisplay * 50
                            screen.blit(Pumpkinjam, (assemblydisplayx + 100, 475))
                            pumpkindisplay -= 1
                            assemblydisplay -= 1
                        pumpkinjamclickareaxstart = assemblydisplay * 50 + 150
                    if cherryjam > 0:
                        cherrydisplay = cherryjam
                        assemblydisplayx = assemblydisplay * 50
                        cherryjamclickareaxend = assemblydisplayx + 150
                        while cherrydisplay > 0:
                            assemblydisplayx = assemblydisplay * 50
                            screen.blit(Cherryjam, (assemblydisplayx + 100, 475))
                            cherrydisplay -= 1
                            assemblydisplay -= 1
                        cherryjamclickareaxstart = assemblydisplay * 50 + 150
                    if blueberryjam > 0:
                        blueberrydisplay = blueberryjam
                        assemblydisplayx = assemblydisplay * 50
                        blueberryjamclickareaxend = assemblydisplayx + 150
                        while blueberrydisplay > 0:
                            assemblydisplayx = assemblydisplay * 50
                            screen.blit(Blueberryjam, (assemblydisplayx + 100, 475))
                            blueberrydisplay -= 1
                            assemblydisplay -= 1
                        blueberryjamclickareaxstart = assemblydisplay * 50 + 150
                    if applejam > 0:
                        appledisplay = applejam
                        assemblydisplayx = assemblydisplay * 50
                        applejamclickareaxend = assemblydisplayx + 150
                        while appledisplay > 0:
                            assemblydisplayx = assemblydisplay * 50
                            screen.blit(Applejam, (assemblydisplayx + 100, 475))
                            appledisplay -= 1
                            assemblydisplay -= 1
                        applejamclickareaxstart = assemblydisplay * 50 + 150
                assemblydisplayleftcount = assemblydisplayleft
                assemblydisplayleftliststatecount = assemblydisplayleftliststate
                assemblydisplaylefty = assemblydisplayleftcount * 75
                while assemblydisplayleftcount > 0:
                    assemblydisplaylefty = assemblydisplayleftcount * 75
                    if assemblydisplayleftlist[assemblydisplayleftliststatecount] == "applejam":
                        screen.blit(Applejam, (75, assemblydisplaylefty))
                    if assemblydisplayleftlist[assemblydisplayleftliststatecount] == "blueberryjam":
                        screen.blit(Blueberryjam, (75, assemblydisplaylefty))
                    if assemblydisplayleftlist[assemblydisplayleftliststatecount] == "cherryjam":
                        screen.blit(Cherryjam, (75, assemblydisplaylefty))
                    if assemblydisplayleftlist[assemblydisplayleftliststatecount] == "pumpkinjam":
                        screen.blit(Pumpkinjam, (75, assemblydisplaylefty))
                    assemblydisplayleftcount -= 1
                    assemblydisplayleftliststatecount -= 1
                assemblydisplayrightcount = assemblydisplayright
                assemblydisplayrightliststatecount = assemblydisplayrightliststate
                assemblydisplayrighty = assemblydisplayrightcount * 75
                while assemblydisplayrightcount > 0:
                    assemblydisplayrighty = assemblydisplayrightcount * 75
                    if assemblydisplayrightlist[assemblydisplayrightliststatecount] == "applejam":
                        screen.blit(Applejam, (675, assemblydisplayrighty))
                    if assemblydisplayrightlist[assemblydisplayrightliststatecount] == "blueberryjam":
                        screen.blit(Blueberryjam, (675, assemblydisplayrighty))
                    if assemblydisplayrightlist[assemblydisplayrightliststatecount] == "cherryjam":
                        screen.blit(Cherryjam, (675, assemblydisplayrighty))
                    if assemblydisplayrightlist[assemblydisplayrightliststatecount] == "pumpkinjam":
                        screen.blit(Pumpkinjam, (675, assemblydisplayrighty))
                    assemblydisplayrightcount -= 1
                    assemblydisplayrightliststatecount -= 1
                LeftClick = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        LeftClick = True
                if LeftClick == True and mouse_y > 475 and mouse_y < 550 and LastClick == False:
                    if applejam > 0 and mouse_x > applejamclickareaxstart and mouse_x < applejamclickareaxend:
                        print("Apple Jam Selected")
                        if assemblydisplayleft < 5:
                            assemblydisplayleft += 1
                            assemblydisplayleftlist.append("applejam")
                            assemblydisplayleftliststate += 1
                        else:
                            assemblydisplayright += 1
                            assemblydisplayrightlist.append("applejam")
                            assemblydisplayrightliststate += 1
                        applejam -= 1
                        pielist.append("applejam")
                        pieliststate += 1
                    if blueberryjam > 0 and mouse_x > blueberryjamclickareaxstart and mouse_x < blueberryjamclickareaxend:
                        print("Blueberry Jam Selected")
                        if assemblydisplayleft < 5:
                            assemblydisplayleft += 1
                            assemblydisplayleftlist.append("blueberryjam")
                            assemblydisplayleftliststate += 1
                        else: 
                            assemblydisplayright += 1
                            assemblydisplayrightlist.append("blueberryjam")
                            assemblydisplayrightliststate += 1
                        blueberryjam -= 1
                        pielist.append("blueberryjam")
                        pieliststate += 1
                    if cherryjam > 0 and mouse_x > cherryjamclickareaxstart and mouse_x < cherryjamclickareaxend:
                        print("Cherry Jam Selected")
                        if assemblydisplayleft < 5:
                            assemblydisplayleft += 1
                            assemblydisplayleftlist.append("cherryjam")
                            assemblydisplayleftliststate += 1
                        else:
                            assemblydisplayright += 1
                            assemblydisplayrightlist.append("cherryjam")
                            assemblydisplayrightliststate += 1
                        cherryjam -= 1
                        pielist.append("cherryjam")
                        pieliststate += 1
                    if pumpkinjam > 0 and mouse_x > pumpkinjamclickareaxstart and mouse_x < pumpkinjamclickareaxend:
                        print("Pumpkin Jam Selected")
                        if assemblydisplayleft < 5:
                            assemblydisplayleft += 1
                            assemblydisplayleftlist.append("pumpkinjam")
                            assemblydisplayleftliststate += 1
                        else:
                            assemblydisplayright += 1
                            assemblydisplayrightlist.append("pumpkinjam")
                            assemblydisplayrightliststate += 1
                        pumpkinjam -= 1
                        pielist.append("pumpkinjam")
                        pieliststate += 1
                if blueberryjam + applejam + pumpkinjam + cherryjam == 0:
                    inminigame = False
                    haspie = True
                    hascrust = False
                    pa = True
                    text_cooldown = pygame.time.get_ticks() + 1000
                LastClick = LeftClick
            
        if player.colliderect(assembly) and blueberryjam == 0 and pumpkinjam == 0 and applejam == 0 and cherryjam == 0:
            if hascrust == False:
                screen.blit(assemblytext6, (250, 290))
            else:
                screen.blit(assemblytext5, (310, 290))
        if blueberryjam > 0 or pumpkinjam > 0 or applejam > 0 or cherryjam > 0:
            if player.colliderect(assembly) and hascrust == False:
                screen.blit(assemblytext4, (310, 290))
        if player.colliderect(crust) and hasdough == False:
            screen.blit(missingdough, (310, 290))
        if player.colliderect(dough) and hasflour == False:
            screen.blit(missingflour, (310, 290))
        if player.colliderect(strawberries) and fruitstate > 8:
            screen.blit(strawberrytext4, (290, 290))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
