#okiren plan
import random

#I. Naredi ogrodje -> while zanka, canvas, eventi za exit itd


#II. Naredi kvadrat -> ta kvadrat bo v prihodnisti ratala kača, zaenkrat naj bo samo kvadrat
#	naredi logiko da ta kvadrat lahko zavija levo desno z kliki na gumne na tipkovnici
#	naredi logiko, da se nakej izpiše, ko se ta kvadrat dotakne stene
#	naredi logiko, da se ta kvadrat premika po nekem "gridu" -> hint nastavi clock.tick na nekaj malega,
#		vsak frame premakni kaco za nekaj pixlov, ta premik predstavlja sirino vsake celice


#III. Kvdrat spremeni v seznam kvadratov, ki predstavljajo kaco


#IV. Naredi logiko, da se nekaj izpiše, ce se kace zabije sama vase


#V. Naredi nek nov kvadrat ki predstavlja hrano
#	-> naredi da se vsakic ko ga kaca poje z glavo prestavi na nakljucno mesto in kaca zrasta


#od tu naprej je treba samo še štet score, kej izpiovat na ekrat, dt kk gumb za game over pa restart itd... neke olepšave


#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov

import pygame


pygame.init()
canvas = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake game")

x = 200
y = 200

#def hranjenje():
smerN = "A"
smerD = "right"
barvaE = (200,0,233)
barvaD = (0,230,230)
hitrost = 10
exit = False
hranakoordinate = [120,87]
kaca = [[250, 400], [235,400]]
kacaD = [[250,200], [265,200]]

while not exit:
    pygame.time.wait(75)
    canvas.fill((0,0,0))

    #kaca ena
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        barvaE = (random.randint(0,255), random.randint(0,255), random.randint(0,255)  )
        barvaD = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    if keys[pygame.K_w] and smerN != "S":
        smerN ="W"
    if keys[pygame.K_s]and smerN != "W":
        smerN = "S"
    if keys[pygame.K_d] and smerN != "A":
        smerN = "D"
    if keys[pygame.K_a] and smerN != "D":
        smerN = "A"


    if keys[pygame.K_UP] and smerD != "down":
        smerD ="up"
    if keys[pygame.K_DOWN]and smerD != "up":
        smerD = "down"
    if keys[pygame.K_LEFT] and smerD != "right":
        smerD = "left"
    if keys[pygame.K_RIGHT] and smerD != "left":
        smerD = "right"


    for i in range(len(kaca)-1):
        kaca[-1-i][0] =  kaca[-2-i][0]
        kaca[-1-i][1] = kaca[-2-i][1]

    if smerN == "D":
        print(hitrost)
        kaca[0][0] += hitrost
    if smerN == "A":
        kaca[0][0] -= hitrost
    if smerN == "W":
        kaca[0][1] -= hitrost
    if smerN == "S":
        kaca[0][1] += hitrost

    #kaca Dve

    for k in range(len(kacaD) - 1):
        kacaD[-1 - k][0] = kacaD[-2 - k][0]
        kacaD[-1 - k][1] = kacaD[-2 - k][1]

    if smerD == "right":
        kacaD[0][0] += hitrost
    elif smerD == "left":
        kacaD[0][0] -= hitrost
    elif smerD == "up":
        kacaD[0][1] -= hitrost
    elif smerD == "down":
        kacaD[0][1] += hitrost

    kaca[0][0] +=1
    #izrisovanje kac
    glavaE = pygame.Rect(kaca[0][0], kaca[0][1], 15, 15)
    glavaD = pygame.Rect(kacaD[0][0], kacaD[0][1], 15, 15)


    for j in kaca:
        kacica = pygame.Rect(j[0], j[1], 15, 15)
        pygame.draw.rect(canvas, barvaE, kacica)
        if glavaD.colliderect(kacica):
            exit = True
        if j[0] > 585 or j[0] < 0 or j[1] > 585 or j[1] < 0:
            exit = True


    for l in kacaD:
        kacicaD = pygame.Rect(l[0], l[1], 15, 15)
        pygame.draw.rect(canvas, barvaD, kacicaD)
        if glavaE.colliderect(kacicaD):
            exit = True
        if l[0] > 585 or l[0] < 0 or l[1] > 585 or l[1] < 0:
            exit = True


    hrana = pygame.Rect(hranakoordinate[0], hranakoordinate[1], 15, 15)
    pygame.draw.rect(canvas, (50, 250, 50),hrana)

    if glavaE.colliderect(hrana):

        hranakoordinate[0] = random.randint(50,550)
        hranakoordinate[1] = random.randint(50, 550)
        kaca.append([1, 1])
    elif glavaD.colliderect(hrana):
        hranakoordinate[0] = random.randint(50,550)
        hranakoordinate[1] = random.randint(50, 550)
        kacaD.append([1,1])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


    pygame.display.update()



