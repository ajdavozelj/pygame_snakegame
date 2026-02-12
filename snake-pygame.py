#okiren plan

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
polozajX = None
polozajY = None
barva = (200,0,233)
hitrost = 1
exit = False
hrana = [120,87]
kaca = [[250, 250, "D"], [230,250, "D"], [210,250, "D"]]
smeri = ["D", "D", "D"]
while not exit:
    pygame.time.wait(5)
    canvas.fill((0,0,0))

    """
    if smer == "D":
        for j in kaca:
            smeri.append("D")
            smeri.pop()

    elif smer == "A":
        for j in kaca:
            smeri.append("A")
            smeri.pop()
            j[0] -= hitrost
    elif smer == "W":
        for j in kaca:
            j[1] -= hitrost
            smeri.append("W")
            smeri.pop()
    elif smer == "S":
        for j in kaca:
            smeri.append("S")
            smeri.pop()
            j[1] += hitrost
    """


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        smerN ="W"
        polozajY = kaca[0][1]

        smeri.append("W")
        smeri.pop(0)
    if keys[pygame.K_s]:
        smeri.append("S")
        smeri.pop(0)
        smerN = "S"
        polozajY = kaca[0][1]
        print(kaca[0],[0])
    if keys[pygame.K_d]:
        smeri.append("D")
        smeri.pop(0)
        smerN = "D"
        polozajX = kaca[0][0]
    if keys[pygame.K_a]:
        smerN = "A"
        polozajX = kaca[0][0]

        smeri.pop(0)
        smeri.append("A")

    for i in range(len(kaca)):
        x = kaca[i][0]
        y = kaca[i][1]
        smerk = kaca[i][2]
        print(smerN, polozajX)
        if smerN == "D" and y == polozajY:
            smerk ="D"

        if smerN == "S" and x == polozajX:
            smerk = "S"

        if smerN == "A" and y == polozajX:
            smerk = "A"

        if smerN == "W" and x == polozajX:
            smerk = "W"


        if smerk == "D":
            x += hitrost
        if smerk == "A":
            x -= hitrost
        if smerk == "W":
            y -= hitrost
        if smerk == "S":
            y += hitrost


        kaca[i] = [x,y,smerk]
        pygame.draw.rect(canvas, barva,pygame.Rect(x,y,15, 15))

        if x > 585 or x<0 or y>585 or y<0:
            exit = True
    print(kaca)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas, (50,250,50), pygame.Rect(hrana[0],hrana[1], 10, 10))
    pygame.display.update()