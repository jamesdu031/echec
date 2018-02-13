import pygame
from pygame.locals import *
import time


BLACK = (150,   150,   150  )
WHITE  = (255,   255,   255)

#constants representing the different resources
B  = 0
W = 1
#a dictionary linking resources to colours
colours =   {
                B  : BLACK,
                W : WHITE,
            }

#a list representing our tilemap
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

#useful game dimensions
TILESIZE  = 100
MAPWIDTH  = 8
MAPHEIGHT = 8

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
reine = []
tour = []
#Ouverture de la fen?tre Pygame
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Echec')
#Chargement et collage du fond

#Chargement et collage des pi?ces
reinep = pygame.image.load("pion/reine.png").convert_alpha()
reine = [0,0]
fenetre.blit(reinep, (reine[0], reine[1]))

tourp = pygame.image.load("pion/tour.png").convert_alpha()
tour = [0,0]
fenetre.blit(tourp, (tour[0], tour[1]))

def pos_piece(piece, abscisse, ordonnee):
    if abscisse <= 7 or ordonnee <= 7:
        piece[0] = abscisse*(800/8)
        piece[1] = ordonnee*(800/8)
    if abscisse > 7 or ordonnee > 7:
        print("Error, piece value is too high")
        piece[0] = 0
        piece[1] = 0


pos_piece(tour, 0, 0)
pos_piece(reine, 3, 0)

pygame.display.flip()

#BOUCLE INFINIE
continuer = True
while (continuer):
	for event in pygame.event.get():	#Attente des evenements
		if event.type == pygame.QUIT:
                    continuer = False
		if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                            if reinepo.collidepoint(event.pos[0],event.pos[1]):          #Prend le pion
                                print("Select G")
                                time.sleep(2)                                           #Attend 2s avant annulation
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:                  #Pose le pion
                                            if event.button == 1:
                                                print("Select D")
                                                pos_piece(reine,event.pos[0] // 100,event.pos[1] // 100)
                                print("ok reine")
                            if tourpo.collidepoint(event.pos[0],event.pos[1]):         #Prend le pion
                                print("Select G")
                                time.sleep(2)                                          #Attend 2s avant annulation
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:                  #Pose le pion
                                            if event.button == 1:
                                                print("Select D")
                                                pos_piece(tour,event.pos[0] // 100,event.pos[1] // 100)
                                print("ok tour")
        for row in range(MAPHEIGHT):
                 #loop through each column in the row
                for column in range(MAPWIDTH):
                    #draw the resource at that position in the tilemap, using the correct colour
                    pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

	#Re-collage
	reinepo = fenetre.blit(reinep, (reine[0], reine[1]))
	tourpo = fenetre.blit(tourp, (tour[0], tour[1]))
	#Rafraichissement
	pygame.display.flip()
pygame.quit()