import pygame
import numpy as np
import os
import time


def branch(start, a, b, l=100, angle=0):
    # condition d'arrete de la fonction recursive
    if l < 10:
        return

    x1, y1 = start
    x2 = x1 + np.sin(angle) * l
    y2 = y1 - np.cos(angle) * l

    pygame.draw.line(surface, blanc, (x1, y1), (x2, y2), 2)

    # on reduit la taille de la branche a chaque it?ration
    l = l * b

    # on cr?er 2 branches de meme longueur avec des angles oppos?s
    angle1 = angle + a
    angle2 = angle - a
    branch((x2, y2), a, b, l, angle1)
    branch((x2, y2), a, b, l, angle2)


def save(surface, doc_name):

    path = 'C:/Users/simon/Documents/IPSA/A2/python/Pygame/'

    # creer le dossier parent uniquement s'il n'existe pas
    if doc_name not in os.listdir(path):
        os.chdir(path)
        os.mkdir(doc_name)

    # on enregiste les images
    os.chdir(path + doc_name)
    pygame.image.save(surface, str(round(time.time(), 1)) + ".jpg")


# ----------------------------------------------------------------------------------------------------------------------
# initialisation constante
H = 500
L = 700
a = 0.4
b = 0.67


blanc = (255, 255, 255)
gris = (50, 50, 50)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)

# initialisation environnement
cercles = []

# initialisation fenetre
pygame.init()
pygame.display.set_caption("A*")
surface = pygame.display.set_mode((L, H))


# ----------------------------------------------------------------------------------------------------------------------
# boucle infinie
launched = 1
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = 0

    surface.fill(gris)

    if pygame.mouse.get_pressed()[0]:
        a = pygame.mouse.get_pos()[1] * np.pi / H

    if pygame.mouse.get_pressed()[2]:
        b = pygame.mouse.get_pos()[1] * 0.9 / H

    a += 0.0001
    b += 0.0001
    branch((L // 2, H), a, b)
    
    pygame.display.flip()
