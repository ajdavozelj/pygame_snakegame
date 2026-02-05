
import pygame


pygame.init()
canvas = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake game")

x = 200
y = 200

smer = "D"
barva = (200,0,233)
hitrost = 1
exit = False
kaca = [[250, 250]]
while not exit:
    pygame.time.wait(4)
    canvas.fill((0,0,0))

    if smer == "D":
        for j in kaca:
            j[0]+= hitrost
    elif smer == "A":
        for j in kaca:
            j[0] -= hitrost
    elif smer == "W":
        for j in kaca:
            j[1] -= hitrost
    elif smer == "S":
        for j in kaca:
            j[1] += hitrost
    print(kaca)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        smer = "W"
    elif keys[pygame.K_s]:
        smer = "S"
    elif keys[pygame.K_d]:
        smer = "D"
    elif keys[pygame.K_a]:
        smer = "A"


    for i in kaca:
        pygame.draw.rect(canvas, barva,pygame.Rect(i[0],i[1],15, 15))

        if i[0] > 585 or i[0]<0 or i[1]>585 or i[1]<0:
            exit = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()