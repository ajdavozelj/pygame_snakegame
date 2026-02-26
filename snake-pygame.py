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
smerN = "D"
barva = (200,0,233)
hitrost = 15
exit = False
hranakoordinate = [120,87]
kaca = [[250, 250], [230,250]]

while not exit:
    pygame.time.wait(70)
    canvas.fill((0,0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        barva = (random.randint(0,255), random.randint(0,255), random.randint(0,255)  )
        print(barva)

    if keys[pygame.K_w] and smerN != "S":
        smerN ="W"
    if keys[pygame.K_s]and smerN != "W":
        smerN = "S"
    if keys[pygame.K_d] and smerN != "A":
        smerN = "D"
    if keys[pygame.K_a] and smerN != "D":
        smerN = "A"

    for i in range(len(kaca)-1):
        kaca[-1-i][0] =  kaca [-2-i][0]
        kaca[-1-i][1] = kaca[-2-i][1]


    if smerN == "D":
        kaca[0][0] += hitrost
    if smerN == "A":
        kaca[0][0] -= hitrost
    if smerN == "W":
        kaca[0][1] -= hitrost
    if smerN == "S":
        kaca[0][1] += hitrost

    print(kaca)

    hrana = pygame.Rect(hranakoordinate[0], hranakoordinate[1], 20, 20)
    pygame.draw.rect(canvas, (50, 250, 50),hrana )

    for j in kaca:
        kacica = pygame.Rect(j[0], j[1], 15, 15)
        pygame.draw.rect(canvas, barva, kacica)
        if j[0] > 585 or j[0] < 0 or j[1] > 585 or j[1] < 0:
            exit = True

    glava = pygame.Rect(kaca[0][0], kaca[0][1], 15, 15)
    if glava.colliderect(hrana):
        hranakoordinate[0] = random.randint(50,550)
        hranakoordinate[1] = random.randint(50, 550)

        kaca.append([1,1])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


    pygame.display.update()



