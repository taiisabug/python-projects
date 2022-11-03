import pygame   
import pygame.freetype
import random
import math
pygame.init()
pygame.display.set_caption('made by tl sutherland! click on the door for a surprise :) happy halloween!!')
WHITE = (225, 225, 225)
BLACK = (0,0,0)
BLOOD = (139, 0, 0)
BLOODMOON = (123, 24, 24)
OX = (74, 30, 4)
GREY = (169, 169, 169)
STEEL = (113, 121, 126)
ALMOND = (234, 221, 202)
BRONZE = (205, 127, 50)
BURNT = (110, 38, 14)
CHOCOLATE = (123, 63, 0)
CHESTNUT = (149, 69, 53)
COFFEE = (111, 78, 55)
BROWN = (92, 64, 51)
MAROON = (128, 0, 0) #brick 1
OCHRE = (145, 56, 49) #brick 2
WINE = (114, 47, 55) #brick 3
BURGUNDY = (128, 0, 32) #brick 4
COGNAC = (131, 67, 51) #brick 5
DOOR2 = (61, 40, 20)
DOOR3 = (51, 34, 17)
DOOR1 = (71, 47, 23)
CHARCOAL = (54, 69, 79)
GRAY = (128, 128, 128) 
SKY = (21, 34, 56)
TREE1 = (0, 128, 0)
TREE2 = (21, 71, 52)
TREE3 = (78, 91, 49)
TREE4 = (4, 106, 56)
TREE5 = (75, 128, 32)
TREE6 = (20, 103, 42)
TREE7 = (2, 96, 48)
GRASS1 = (9, 34, 21)
GRASS2 = (6, 23, 14)
GRASS3 = (12, 45, 28)
GRASS4 = (34, 43, 19)
PUMPKIN1 = (204, 85, 0)
PUMPKIN2 = (227, 150, 62)
PUMPKIN3 = (242, 140, 40)
PUMPKIN4 = (210, 125, 45)
PUMPKIN5 = (236, 88, 0)
PUMPKIN6 = (255, 117, 24)
STEM1 = (74, 30, 4)
STEM2 = (72, 60, 50)
STEM3 = (90, 60, 50)
STEM4 = (128, 70, 27)
CATNOSE = (248, 131, 121)
CATEYE = (11, 218, 81)
STAR = (255, 229, 180)
MASK = (240, 236, 222)
HAIR = (64, 40, 15)
MIKE = (31, 30, 58)
STONE1 = (137, 148, 153)
STONE2 = (129, 133, 137) 
STONE3 = (113, 121, 126)
GHOST1 = (229, 228, 226)
GHOST2 = (230, 230, 250)
GHOST3 = (249, 246, 220)
WOOD = (99, 75, 59)
W2 = (87, 64, 49)
W3 = (82, 62, 49)
DIRT = (41, 39, 27)
# hex codes from https://htmlcolorcodes.com
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
pygame.draw.rect(screen, SKY, (0, 0, 1000, 700))

#stars
stars = random.randint(100, 300)
counter = 0
while counter != stars:
    x = random.randint(0, 1000)
    y = random.randint(0, 700)
    h = random.randint(3, 6)
    l = random.randint(1, 3)
    pygame.draw.line(screen, STAR, (x, y-h), (x, y+h), 1)
    pygame.draw.line(screen, STAR, (x-l, y), (x+l, y), 1)
    counter = counter + 1


#moon
moonc = [BLOODMOON, GREY, WHITE]
mc = random.choice(moonc)
x = random.randint (75, 900)
y = random.randint (25, 300)
r = random.randint (30, 100)
m = random.randint (20, 60)
pygame.draw.circle(screen, mc, (x, y), r)
pygame.draw.circle(screen, SKY, (x+m, y), r)

#ghosts
counter = 1
ghosts = random.randint (5, 10)
gc = [GHOST1, GHOST2, GHOST3]

while counter != ghosts:
    GHOST = random.choice(gc)
    xg = random.randint (300, 900)
    yg = random.randint (100, 300)
    r = random.randint (15, 25)
    r2 = random.randint (5, 8)
    l = random.randint (1, 5)
    h = random.randint (15, 30)
    e = random.randint (2, 4)
    de = random.randint (7, 10)
    mi = random.randint (1, 3)
    pygame.draw.circle(screen, GHOST, (xg, yg), r)
    pygame.draw.polygon(screen, GHOST, ((xg-r, yg), (xg+r, yg), (xg+r+l, yg+h), (xg-r-l, yg+h)))
    pygame.draw.circle(screen, GHOST, ((xg-r-l)+r2, yg+h), r2)
    pygame.draw.circle(screen, GHOST, ((xg+r+l)-r2, yg+h), r2)
    pygame.draw.circle(screen, GHOST, (xg, yg+h), r2)
    pygame.draw.circle(screen, BLACK, (xg-de, yg), e)
    pygame.draw.circle(screen, BLACK, (xg+de, yg), e)
    pygame.draw.circle(screen, BLACK, (xg, yg+(mi*3)), e-mi)
    counter = counter + 1

#grass & path
grasscolour = [GRASS3, GRASS4]
grassc = random.choice(grasscolour)
pygame.draw.circle(screen, grassc, (300, 4500), 4000)
pygame.draw.polygon(screen, DIRT, ((400, 580), (610, 580), (650, 516), (400, 500)))
pygame.draw.circle(screen, DIRT, (410, 580), 7)
pygame.draw.circle(screen, DIRT, (420, 580), 8)
pygame.draw.circle(screen, DIRT, (435, 580), 6)
pygame.draw.circle(screen, DIRT, (450, 580), 7)
pygame.draw.circle(screen, DIRT, (468, 580), 9)
pygame.draw.circle(screen, DIRT, (490, 580), 6)
pygame.draw.circle(screen, DIRT, (520, 580), 11)
pygame.draw.circle(screen, DIRT, (540, 580), 7)
pygame.draw.circle(screen, DIRT, (566, 580), 9)
pygame.draw.circle(screen, DIRT, (588, 580), 6)
pygame.draw.circle(screen, DIRT, (600, 580), 7)
pygame.draw.circle(screen, DIRT, (610, 580), 8)
pygame.draw.circle(screen, DIRT, (620, 560), 9)
pygame.draw.circle(screen, DIRT, (630, 540), 11)
pygame.draw.circle(screen, DIRT, (640, 520), 6)

#gravestones
counter = 1
graves = random.randint (3, 6)
gc = [STONE1, STONE2, STONE3]

while counter < graves:
    if counter < graves:
        GRAVE = random.choice(gc)
        gi = random.randint(10, 15)
        gx = random.randint(400, 600)
        gy = random.randint(480, 520)
        gh = random.randint(20, 40)
        pygame.draw.circle(screen, GRAVE, (gx, gy), gi)
        pygame.draw.circle(screen, BLACK, (gx, gy), gi, 1)    
        pygame.draw.rect(screen, GRAVE, (gx-gi, gy, gi*2, gh))
        pygame.draw.rect(screen, BLACK, (gx-gi, gy, gi*2, gh), 1)  
        pygame.draw.rect(screen, GRAVE, (gx-gi, gy, gi*2, 1))
        counter = counter + 1
    if counter < graves:
        GRAVE = random.choice(gc)
        gw = random.randint(10, 15)
        gx = random.randint(400, 600)
        gy = random.randint(460, 500)
        gh = random.randint(40, 70)
        gi = random.randint(10, 20)
        gd = random.randint(10, 15)
        pygame.draw.rect(screen, GRAVE, (gx, gy, gw, gh))
        pygame.draw.rect(screen, BLACK, (gx, gy, gw, gh), 1)        
        pygame.draw.rect(screen, GRAVE, (gx-gi, gy+gd, gi*2+gw, gw))
        pygame.draw.rect(screen, BLACK, (gx-gi, gy+gd, gi*2+gw, gw), 1)  
        pygame.draw.rect(screen, GRAVE, (gx+gd/gi, gy+gd, gw, gw))
        counter = counter + 1

#fencing
pygame.draw.line(screen, WOOD, (600, 500), (600, 575), 10)
pygame.draw.line(screen, WOOD, (540, 500), (540, 575), 10)
pygame.draw.arc(screen, WOOD, (536, 475, 70, 50), 0, math.pi,10)
pygame.draw.line(screen, WOOD, (480, 520), (480, 575), 10)
pygame.draw.line(screen, WOOD, (630, 500), (630, 540), 10)
pygame.draw.line(screen, W2, (400, 535), (490, 530), 4)
pygame.draw.line(screen, W3, (400, 553), (488, 558), 4)
pygame.draw.line(screen, W3, (470, 532), (543, 539), 4)
pygame.draw.line(screen, W2, (475, 558), (547, 553), 4)
pygame.draw.line(screen, W3, (595, 556), (638, 528), 4)
pygame.draw.line(screen, W2, (592, 534), (639, 501), 4)

#bricks

brickcolour = [MAROON, OCHRE, WINE, BURGUNDY, COGNAC]
pygame.draw.rect(screen, BROWN, (100, 300, 300, 200))


x = 100
y = 280
counter = 1

while y < 590:
    y = y + 10
    if counter == 1:
        x = 100
        while x < 400:
            bc = random.choice(brickcolour)        
            pygame.draw.rect(screen, bc, (x, y, 20, 10))
            pygame.draw.rect(screen, GREY, (x, y, 20, 10), 1)
            x = x + 20
        counter = 2
    elif counter == 2:
        x = 100
        bc = random.choice(brickcolour)        
        pygame.draw.rect(screen, bc, (x, y, 10, 10))
        pygame.draw.rect(screen, GREY, (x, y, 10, 10), 1)   
        x = 110
        while x < 380:
            bc = random.choice(brickcolour)        
            pygame.draw.rect(screen, bc, (x, y, 20, 10))
            pygame.draw.rect(screen, GREY, (x, y, 20, 10), 1)
            x = x + 20
        bc = random.choice(brickcolour)        
        pygame.draw.rect(screen, bc, (x, y, 10, 10))
        pygame.draw.rect(screen, GREY, (x, y, 10, 10), 1)
        counter = 1

pygame.draw.rect(screen, BLACK, (100, 300, 305, 300), 4)


#door

pygame.draw.rect(screen, DOOR1, (150, 500, 50, 100))
pygame.draw.rect(screen, BLACK, (150, 500, 50, 100), 3)
pygame.draw.rect(screen, DOOR2, (160, 510, 10, 20))
pygame.draw.rect(screen, DOOR2, (178, 510, 10, 20))
pygame.draw.rect(screen, DOOR2, (160, 535, 10, 20))
pygame.draw.rect(screen, DOOR2, (178, 535, 10, 20))                       
pygame.draw.rect(screen, DOOR2, (160, 560, 10, 25))
pygame.draw.rect(screen, DOOR2, (178, 560, 10, 25))
pygame.draw.rect(screen, DOOR3, (160, 510, 10, 20), 2)
pygame.draw.rect(screen, DOOR3, (178, 510, 10, 20), 2)
pygame.draw.rect(screen, DOOR3, (160, 535, 10, 20), 2)
pygame.draw.rect(screen, DOOR3, (178, 535, 10, 20), 2)                       
pygame.draw.rect(screen, DOOR3, (160, 560, 10, 25), 2)
pygame.draw.rect(screen, DOOR3, (178, 560, 10, 25), 2)
pygame.draw.circle(screen, CHARCOAL, (174, 532), 2) 
pygame.draw.circle(screen, CHARCOAL, (190, 555), 4)


#roof

pygame.draw.line(screen, BROWN, (230, 214), (270, 214), 15)
pygame.draw.line(screen, BROWN, (205, 228), (295, 228), 15)
pygame.draw.line(screen, BROWN, (182, 242), (315, 242), 15)
pygame.draw.line(screen, BROWN, (162, 256), (340, 256), 15)
pygame.draw.line(screen, BROWN, (140, 270), (362, 270), 15)
pygame.draw.line(screen, BROWN, (116, 284), (385, 284), 15)
pygame.draw.line(screen, BROWN, (92, 298), (405, 298), 15)
pygame.draw.line(screen, BLACK, (70, 305), (430, 305), 3)
pygame.draw.line(screen, OX, (90, 295), (410, 295), 1)
pygame.draw.line(screen, OX, (110, 285), (390, 285), 1)
pygame.draw.line(screen, OX, (130, 275), (370, 275), 1)
pygame.draw.line(screen, OX, (150, 265), (350, 265), 1)
pygame.draw.line(screen, OX, (170, 255), (330, 255), 1)
pygame.draw.line(screen, OX, (190, 245), (310, 245), 1)
pygame.draw.line(screen, OX, (205, 235), (295, 235), 1)
pygame.draw.line(screen, OX, (220, 225), (287, 225), 1)

pygame.draw.line(screen, OX, (250, 200), (70, 310), 15)
pygame.draw.line(screen, OX, (250, 200), (430, 310), 15)
pygame.draw.line(screen, BLACK, (250, 207), (70, 317), 2)
pygame.draw.line(screen, BLACK, (250, 207), (430, 317), 3)
pygame.draw.line(screen, BLACK, (250, 193), (70, 303), 3)
pygame.draw.line(screen, BLACK, (250, 193), (430, 303), 2)
pygame.draw.line(screen, BLACK, (430, 303), (430, 317), 2)
pygame.draw.line(screen, BLACK, (70, 303), (70, 317), 2)

pygame.draw.circle(screen, STEEL, (250, 270), 25)
pygame.draw.circle(screen, CHARCOAL, (250, 270), 25, 3)
pygame.draw.line(screen, CHARCOAL, (249, 295), (249, 245), 3)
pygame.draw.line(screen, CHARCOAL, (275, 270), (225, 270), 3)

#windows

pygame.draw.rect(screen, STEEL, (300, 500, 50, 70))
pygame.draw.rect(screen, CHARCOAL, (300, 500, 50, 70), 3)
pygame.draw.line(screen, CHARCOAL, (300, 535), (350, 535), 3)
pygame.draw.line(screen, CHARCOAL, (325, 500), (325, 570), 3)

pygame.draw.rect(screen, STEEL, (300, 360, 50, 70))
pygame.draw.rect(screen, CHARCOAL, (300, 360, 50, 70), 3)
pygame.draw.line(screen, CHARCOAL, (300, 395), (350, 395), 3)
pygame.draw.line(screen, CHARCOAL, (325, 360), (325, 430), 3)

pygame.draw.rect(screen, STEEL, (150, 360, 50, 70))
pygame.draw.rect(screen, CHARCOAL, (150, 360, 50, 70), 3)
pygame.draw.line(screen, CHARCOAL, (150, 395), (200, 395), 3)
pygame.draw.line(screen, CHARCOAL, (175, 360), (175, 430), 3)

#window shutters

pygame.draw.rect(screen, DOOR1, (200, 355, 30, 80))
pygame.draw.rect(screen, DOOR2, (200, 355, 30, 80), 2)
pygame.draw.rect(screen, DOOR3, (205, 365, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (205, 400, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (205, 365, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (205, 375, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (205, 385, 20, 5), 1)
pygame.draw.rect(screen, DOOR3, (205, 405, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (205, 415, 20, 6), 1)

pygame.draw.rect(screen, DOOR1, (120, 355, 30, 80))
pygame.draw.rect(screen, DOOR2, (120, 355, 30, 80), 2)
pygame.draw.rect(screen, DOOR3, (125, 365, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (125, 400, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (125, 365, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (125, 375, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (125, 385, 20, 5), 1)
pygame.draw.rect(screen, DOOR3, (125, 405, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (125, 415, 20, 6), 1)


pygame.draw.rect(screen, DOOR1, (270, 355, 30, 80))
pygame.draw.rect(screen, DOOR2, (270, 355, 30, 80), 2)
pygame.draw.rect(screen, DOOR3, (275, 365, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (275, 400, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (275, 365, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (275, 375, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (275, 385, 20, 5), 1)
pygame.draw.rect(screen, DOOR3, (275, 405, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (275, 415, 20, 6), 1)

pygame.draw.rect(screen, DOOR1, (350, 355, 30, 80))
pygame.draw.rect(screen, DOOR2, (350, 355, 30, 80), 2)
pygame.draw.rect(screen, DOOR3, (355, 365, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (355, 400, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (355, 365, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (355, 375, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (355, 385, 20, 5), 1)
pygame.draw.rect(screen, DOOR3, (355, 405, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (355, 415, 20, 6), 1)

pygame.draw.rect(screen, DOOR1, (270, 495, 30, 80))
pygame.draw.rect(screen, DOOR2, (270, 495, 30, 80), 2)
pygame.draw.rect(screen, DOOR3, (275, 505, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (275, 540, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (275, 505, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (275, 515, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (275, 525, 20, 5), 1)
pygame.draw.rect(screen, DOOR3, (275, 545, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (275, 555, 20, 6), 1)

pygame.draw.rect(screen, DOOR1, (350, 495, 30, 80))
pygame.draw.rect(screen, DOOR2, (350, 495, 30, 80), 2)
pygame.draw.rect(screen, DOOR3, (355, 505, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (355, 540, 20, 25), 1)
pygame.draw.rect(screen, DOOR3, (355, 505, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (355, 515, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (355, 525, 20, 5), 1)
pygame.draw.rect(screen, DOOR3, (355, 545, 20, 6), 1)
pygame.draw.rect(screen, DOOR3, (355, 555, 20, 6), 1)


#cat

#cat = 1   # if you want it always to work, select blood as the only moon variable and make this variable true
#cat = 2    # if you want it to never work, select this as true
cat = random.randint(1, 2)
if cat == 1:
    xcat = random.randint(100, 400)
    hcat = random.randint(60, 80)
    pygame.draw.polygon(screen, BLACK, ((xcat-1, 540), (xcat-7, 550), (xcat-12, 535)))
    pygame.draw.polygon(screen, CHARCOAL, ((xcat-1, 540), (xcat-7, 550), (xcat-12, 535)), 1)
    pygame.draw.polygon(screen, BLACK, ((xcat+1, 540), (xcat+7, 550), (xcat+12, 535)))
    pygame.draw.polygon(screen, CHARCOAL, ((xcat+1, 540), (xcat+7, 550), (xcat+12, 535)), 1)
    pygame.draw.ellipse(screen, BLACK, (xcat-10, 550, 20, hcat))
    pygame.draw.ellipse(screen, CHARCOAL, (xcat-10, 550, 20, hcat), 1)
    pygame.draw.circle(screen, BLACK, (xcat, 550), 10)
    pygame.draw.circle(screen, CHARCOAL, (xcat, 550), 10, 1)
    pygame.draw.circle(screen, BLACK, (xcat+7, 540+hcat), 5)
    pygame.draw.circle(screen, CHARCOAL, (xcat+7, 540+hcat), 5, 1)
    pygame.draw.circle(screen, BLACK, (xcat-7, 540+hcat), 5)
    pygame.draw.circle(screen, CHARCOAL, (xcat-7, 540+hcat), 5, 1)
    pygame.draw.rect(screen, grassc, (xcat-15, 540+hcat, 40, 10))
    pygame.draw.arc(screen, GREY, (xcat-4, 550, 5, 4), math.pi, math.pi*2)
    pygame.draw.arc(screen, GREY, (xcat, 550, 5, 4), math.pi, math.pi*2)
    pygame.draw.circle(screen, CATNOSE, (xcat, 550), 1)
    pygame.draw.circle(screen, CATEYE, (xcat-4, 548), 2)
    pygame.draw.circle(screen, CATEYE, (xcat+4, 548), 2)
    pygame.draw.line(screen, CHARCOAL, (xcat-4, 546), (xcat-4, 550), 1)
    pygame.draw.line(screen, CHARCOAL, (xcat+4, 546), (xcat+4, 550), 1)
    pygame.draw.arc(screen, BLACK, (xcat-10, 570-hcat, 30, 20+hcat), 3*math.pi/2, 5*math.pi/6, 5)


#pumpkin

pumpkincolour = [PUMPKIN1, PUMPKIN2, PUMPKIN3, PUMPKIN4, PUMPKIN5, PUMPKIN6]
stemcolour = [STEM1, STEM2, STEM3, STEM4]
pump = random.randint(5, 15)
counter = 1

while counter < pump:
    xp = random.randint (50, 950)
    yp = random.randint (580, 650)
    w = random.randint (10, 15)
    h = random.randint (20, 50)
    i = random.randint (2, 5)
    sh = random.randint (1, 4)
    sw = random.randint (3, 5)
    pc = random.choice(pumpkincolour)
    sc = random.choice(stemcolour)
    
    pygame.draw.line (screen, sc, (xp+(w/2),yp-sh), (xp+(w/2), yp+sh), sw)
    pygame.draw.ellipse (screen, pc, (xp-(w/2)*i, yp, w+(w*i), h))
    pygame.draw.ellipse (screen, BLACK, (xp-(w/2)*i, yp, w+(w*i), h), 1)
    pygame.draw.ellipse (screen, pc, (xp-(w/4)*i, yp, w+((w/2)*i), h))
    pygame.draw.ellipse (screen, BLACK, (xp-(w/4)*i, yp, w+((w/2)*i), h), 1)
    pygame.draw.ellipse (screen, pc, (xp, yp, w, h))
    pygame.draw.ellipse (screen, BLACK, (xp, yp, w, h), 1)
    counter = counter + 1

#tree

counter = 1
tree = random.randint (2, 3)
tc = [TREE1, TREE2, TREE3, TREE4, TREE5, TREE6, TREE7]
sc = [CHESTNUT, CHOCOLATE, BURNT]

while counter != tree:
    TREE = random.choice(tc)
    STUMP = random.choice(sc)
    xt = random.randint (650, 1000)
    yt1 = random.randint (100, 300)
    h = random.randint (75, 100)
    i = random.randint (75, 120)
    s = random.randint (0, 30)
    pygame.draw.line(screen, STUMP, (xt, yt1+100), (xt, 650+s), 29)
    pygame.draw.rect(screen, BLACK, (xt-15, yt1+100, 30, 552-yt1+s), 2)
    pygame.draw.polygon(screen, BLACK, ((xt, yt1+100), (xt-100, yt1+h+2*i), (xt+100, yt1+h+2*i)), 6)
    pygame.draw.polygon(screen, BLACK, ((xt, yt1+50), (xt-75, yt1+h+i), (xt+75, yt1+h+i)), 6)
    pygame.draw.polygon(screen, BLACK, ((xt, yt1), (xt-50, yt1+h), (xt+50, yt1+h)), 6)
    pygame.draw.polygon(screen, TREE, ((xt, yt1), (xt-50, yt1+h), (xt+50, yt1+h)))
    pygame.draw.polygon(screen, TREE, ((xt, yt1+50), (xt-75, yt1+h+i), (xt+75, yt1+h+i)))
    pygame.draw.polygon(screen, TREE, ((xt, yt1+100), (xt-100, yt1+h+2*i), (xt+100, yt1+h+2*i)))
    counter = counter + 1
    
#easter egg blood moon rises

bloodmoon = False

if mc == BLOODMOON and cat == 1:
    bloodmoon = True
    y = -500
    while y < 1000:
        pygame.draw.rect(screen, BLOOD, (0, 0, 1000, y))
        pygame.draw.arc(screen, BLOOD, (0, y-100, 50, 200), math.pi, 0, 1000)
        pygame.draw.arc(screen, BLOOD, (40, y-10, 40, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (70, y-25, 50, 50), math.pi, 0, 10000)
        pygame.draw.arc(screen, BLOOD, (110, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (150, y-300, 100, 500), math.pi, 0, 5000)
        pygame.draw.arc(screen, BLOOD, (240, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (280, y-120, 50, 200), math.pi, 0, 5000)
        pygame.draw.arc(screen, BLOOD, (320, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (360, y-350, 100, 500), math.pi, 0, 5000)
        pygame.draw.arc(screen, BLOOD, (450, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (490, y-25, 50, 50), math.pi, 0, 10000)
        pygame.draw.arc(screen, BLOOD, (530, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (570, y-100, 50, 200), math.pi, 0, 5000)
        pygame.draw.arc(screen, BLOOD, (610, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (650, y-400, 100, 700), math.pi, 0, 5000)
        pygame.draw.arc(screen, BLOOD, (740, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (780, y-300, 100, 500), math.pi, 0, 5000)
        pygame.draw.arc(screen, BLOOD, (870, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (910, y-25, 50, 50), math.pi, 0, 10000)
        pygame.draw.arc(screen, BLOOD, (950, y-10, 50, 40), 0, math.pi, 10)
        pygame.draw.arc(screen, BLOOD, (990, y-100, 80, 200), math.pi, 0, 5000)
        y = y + 2
        pygame.time.wait(10)
        pygame.display.flip()    

#easter egg message

if bloodmoon == True:
    display_surface = pygame.display.set_mode((1000, 700))
    font = pygame.font.Font('smackplain.ttf', 50)
    text = font.render('HAPPY HALLOWEEN! (from tl & dodger)', False, BLACK)
    textRect = text.get_rect()
    textRect.center = (1000 // 2, 700 // 2)
    
    if True: 
        display_surface.fill(BLOOD)
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
            
        pygame.time.wait(1000)
        pygame.display.flip()  
        pygame.time.wait(2000)
        pygame.quit()

#door open
if bloodmoon == False:
    x = 0
    y = 0
    clock = pygame.time.Clock()
    opendoor = False
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print (x, y)
        if x >= 150 and x<= 200 and y >= 500 and y <= 600 or opendoor == True:
            opendoor = True
            
            #michael myers
            pygame.draw.rect(screen, BLACK, (150, 500, 50, 100))
            pygame.draw.polygon(screen, DOOR1, ((150, 500), (150, 600), (100, 620), (100, 520)))
            pygame.draw.polygon(screen, DOOR3, ((150, 500), (150, 600), (100, 620), (100, 520)), 2)
            pygame.draw.circle(screen, HAIR, (175, 515), 9)
            pygame.draw.circle(screen, MASK, (175, 520), 7)
            pygame.draw.rect(screen, MASK, (168, 513, 14, 7))
            pygame.draw.circle(screen, BLACK, (170, 519), 3, 1)
            pygame.draw.circle(screen, BLACK, (180, 519), 3, 1)
            pygame.draw.rect(screen, MASK, (168, 513, 14, 7))
            pygame.draw.circle(screen, BLACK, (172, 517), 2)
            pygame.draw.circle(screen, BLACK, (178, 517), 2)
            pygame.draw.line(screen, BLACK, (172, 523), (177, 523), 1)
            pygame.draw.polygon(screen, MIKE, ((160, 530), (190, 530), (185, 550), (165, 550)))
            pygame.draw.polygon(screen, MIKE, ((185, 550), (165, 550), (163, 560), (187, 560)))
            pygame.draw.polygon(screen, MIKE, ((187, 560), (175, 560), (180, 590), (185, 590)))
            pygame.draw.polygon(screen, MIKE, ((163, 560), (175, 560), (170, 590), (165, 590)))
            pygame.draw.line(screen, MIKE, (160, 530), (155, 560), 7)
            pygame.draw.line(screen, MIKE, (190, 530), (195, 560), 7)
            pygame.draw.line(screen, CHARCOAL, (195, 560), (200, 575), 3)
            pygame.draw.circle(screen, MASK, (195, 560), 3)
            pygame.draw.circle(screen, MASK, (155, 560), 3)
            pygame.draw.ellipse(screen, CHARCOAL, (180, 588, 15, 7))
            pygame.draw.ellipse(screen, CHARCOAL, (155, 588, 15, 7))
            
            #handprint
            pygame.draw.circle(screen, BLOOD, (315, 560), 5)
            pygame.draw.line(screen, BLOOD, (310, 550), (313, 560), 2)
            pygame.draw.line(screen, BLOOD, (313, 548), (314, 560), 2)
            pygame.draw.line(screen, BLOOD, (316, 549), (315, 560), 2)
            pygame.draw.line(screen, BLOOD, (319, 552), (316, 560), 2)
            pygame.draw.line(screen, BLOOD, (305, 558), (315, 560), 2)
            
            pygame.draw.circle(screen, BLOOD, (161, 380), 5)
            pygame.draw.line(screen, BLOOD, (155, 370), (158, 380), 2)
            pygame.draw.line(screen, BLOOD, (158, 369), (159, 380), 2)
            pygame.draw.line(screen, BLOOD, (161, 368), (160, 380), 2)
            pygame.draw.line(screen, BLOOD, (164, 370), (161, 380), 2)
            pygame.draw.line(screen, BLOOD, (170, 378), (160, 380), 2)
            
    
        pygame.display.flip()
        clock.tick(30)


#end
    pygame.quit()
