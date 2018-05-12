import pygame
from pygame.locals import *
import time

BLACK = (150,   150,   150  )
WHITE  = (255,   255,   255)

#Variables des couleurs
B  = 0
W = 1
#Creation d'un dictionnaire pour les couleurs utilises
colours =   {
                B  : BLACK,
                W : WHITE,
            }

#Une liste qui represente l'echiquier
tilemap = [
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B],
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B],
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B],
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B]
          ]

#Dimension de l'echiquier
TILESIZE  = 100
MAPWIDTH  = 8
MAPHEIGHT = 8

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
reine = []
tour = []
#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Echec')
#Chargement et collage du fond

#Chargement et collage des pieces
reinep = pygame.image.load("pion/reine.png").convert_alpha()
reine = [0,0]
fenetre.blit(reinep, (reine[0], reine[1]))

roip = pygame.image.load("pion/roi.png").convert_alpha()
roi = [0,0]
fenetre.blit(roip, (roi[0], roi[1]))

tourp = pygame.image.load("pion/tour.png").convert_alpha()
tour = [0,0]
fenetre.blit(tourp, (tour[0], tour[1]))

chavalierp = pygame.image.load("pion/chavalier.png").convert_alpha()
chavalier = [0,0]
fenetre.blit(chavalierp, (chavalier[0], chavalier[1]))

foup = pygame.image.load("pion/fou.png").convert_alpha()
fou = [0,0]
fenetre.blit(foup, (fou[0], fou[1]))

tourp2 = pygame.image.load("pion/tour.png").convert_alpha()
tour2 = [0,0]
fenetre.blit(tourp2, (tour2[0], tour2[1]))

chavalierp2 = pygame.image.load("pion/chavalier.png").convert_alpha()
chavalier2 = [0,0]
fenetre.blit(chavalierp2, (chavalier2[0], chavalier2[1]))

foup2 = pygame.image.load("pion/fou.png").convert_alpha()
fou2 = [0,0]
fenetre.blit(foup2, (fou2[0], fou2[1]))

pionp = pygame.image.load("pion/pion.png").convert_alpha()
pion = [0,0]
fenetre.blit(pionp, (pion[0], pion[1]))

def pos_piece(piece, abscisse, ordonnee):
    if abscisse <= 7 or ordonnee <= 7:
        piece[0] = abscisse*(800/8)
        piece[1] = ordonnee*(800/8)
    if abscisse > 7 or ordonnee > 7:
        print("Erreur, valeur de la piece trop haute")
        piece[0] = 0
        piece[1] = 0

def deplacement(piece, piecepo):
    global event
    if piecepo.collidepoint(event.pos[0],event.pos[1]):         #Prend le pion
        print("Selectionne la destination")
        time.sleep(2)                                          #Attend 2s avant annulation
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:                  #Pose le pion
                if event.button == 1:
                    print("Position de destination")
                    pos_piece(piece,event.pos[0] // 100,event.pos[1] // 100)
        print("ok piece")

pos_piece(reine, 3, 0)
pos_piece(roi, 4, 0)
pos_piece(chavalier, 1, 0)
pos_piece(fou, 2, 0)
pos_piece(tour, 0, 0)
pos_piece(chavalier2, 6, 0)
pos_piece(fou2, 5, 0)
pos_piece(tour2, 7, 0)
pos_piece(pion, 0, 1)


pygame.display.flip()

#BOUCLE INFINIE
continuer = True
while (continuer):
	for event in pygame.event.get():	#Attente des evenements
		if event.type == pygame.QUIT:
                    continuer = False
		if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                            deplacement(reine, reinepo)
                            deplacement(roi, roipo)
                            deplacement(tour, tourpo)
                            deplacement(chavalier, chavalierpo)
                            deplacement(fou, foupo)
                            deplacement(tour2, tourpo2)
                            deplacement(chavalier2, chavalierpo2)
                            deplacement(fou2, foupo2)

                            deplacement(pion, pionpo)
        for row in range(MAPHEIGHT):
                 #Creation de l'echiquier
                for column in range(MAPWIDTH):
                    #Dessine les cases a la bonne place et en utilisant le bonnes couleurs (noirs et blancs)
                    pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

	#Re-collage
	reinepo = fenetre.blit(reinep, (reine[0], reine[1]))
	tourpo = fenetre.blit(tourp, (tour[0], tour[1]))
        chavalierpo = fenetre.blit(chavalierp, (chavalier[0], chavalier[1]))
        foupo = fenetre.blit(foup, (fou[0], fou[1]))
        roipo = fenetre.blit(roip, (roi[0], roi[1]))
        pionpo = fenetre.blit(pionp, (pion[0], pion[1]))
        chavalierpo2 = fenetre.blit(chavalierp2, (chavalier2[0], chavalier2[1]))
        tourpo2 = fenetre.blit(tourp2, (tour2[0], tour2[1]))
        foupo2 = fenetre.blit(foup2, (fou2[0], fou2[1]))
    #Rafraichissement
	pygame.display.flip()
pygame.quit()