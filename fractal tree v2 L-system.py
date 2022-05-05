import pygame
import numpy as np


def branch(start, phrase, l=5, angle=0):
    # coordonn?es
    x1, y1 = start
    x2 = x1
    y2 = x1

    # i est notre curseur de lecture
    i = 0

    # condition d'arrete de la fonction recursive
    # if l < 10:
    #   return None

    # on lit la phrase pour chaque caractere (F+-[]) on defini une action
    while i < len(phrase):
        var = phrase[i]

        # on creer une ligne sur l'arbre
        if var == 'F':

            # trigonometrie
            x2 = x1 + np.sin(angle) * l
            y2 = y1 - np.cos(angle) * l
            pygame.draw.line(surface, blanc, (x1, y1), (x2, y2), 2)

            # on reduit la taille de la branche a chaque it?ration
            l = l * b

            # on actualise la nouvelle position de base pour la futur branche
            x1 = x2
            y1 = y2

        # on fait changer d'orientation la prochaine branche sens trigo
        if var == '+':
            angle = angle + a

        # on fait changer d'orientation la prochaine branche sens horaire
        if var == '-':
            angle = angle - a

        # on creer une nouvelle branche avec les parametres angle et l deja actualis? par les autres var
        if var == '[':

            # on isole dans la phrase la sous phrase entre les var [ et fin de la phrase
            sub_phrase = phrase[i + 1:]

            # recurence sur une phrase plus petite
            j = branch((x2, y2), sub_phrase, l, angle)

            # on saute le text entre i et j + 1
            i += j + 1

        # c'est le bout d'une branche
        if var == ']':

            # on arr?te la lecture actuelle et on retourne l'indice de la ]
            return i

            # on se replace ou la branche a commenc?
            # print(new_phrase)
            # branch((x2, y2), new_phrase, start_l, start_angle)

        # on passe au caractere suivant
        i += 1


def generate(phrase):
    # on teste tout les caracteres pour savoir s'il y a une regle associ?
    resultat = ''
    for i in phrase:
        if i in regles:
            var = np.random.choice(regles[i])
            resultat += var
        else:
            # si le caractere n'est pas a la base d'une regle, on l'ajoute au resutat quand meme
            resultat += i

    print(resultat)
    print()
    return resultat


# ----------------------------------------------------------------------------------------------------------------------
# initialisation constante
H = 500
L = 700
a = np.pi / 6
b = 1


blanc = (255, 255, 255)
gris = (50, 50, 50)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)

# initialisation environnement
"""
axiom = 'AB'
regles = {'A': 'AB',
         'B': 'A'}
"""
axiom = 'F'
regles = {'F': ['FF+[+F-F-F]-[-F+F+F]']}

# notre premier caractere est l'axiome
phrase = axiom


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

    # on develloppe la phrase si l'on clique
    if pygame.mouse.get_pressed()[0]:
        phrase = generate(phrase)

        # on attend pour eviter de g?n?rer 2 fois pour un meme clique
        pygame.time.wait(500)

    # on appel la fonction recursive
    branch((L // 2, H), phrase)

    pygame.display.flip()
    pygame.time.wait(10)
