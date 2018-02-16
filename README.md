# Échec
Le jeu d’échec pour un devoir ISN  
**[Wiki & FAQ](https://github.com/jamesdu031/echec/wiki)**

---------
TODO
-

| Point | État |
| --------------------- | :------------------------: |
| Affichage du damier   |☑|
| Affichage des pions   |☑|
| Écran d'accueil       |☑|
| Déplacer les pions    |☑|
| Respect des règles    |☐|
| Affichage de tous les pions  |☐|

**[Voir plus](https://github.com/jamesdu031/echec/projects/1)**
 
 --------
Dépendance
-
 
 
 - Python 2.7
 - Pygame pour Python 2.7

--------
Complie & run
-
**Vous avez besoins de toute les dépendances installer.**  

Télécharger:  

    $ git clone https://github.com/jamesdu031/echec.git

Pour lancer sans compiler:  

    $ python menu.py

Pour complier et lancer:  

    $ python complie.py
	$ python menu.pyc

**Ou sinon vous pouvez toujours télécharger la dernière release:**  
[https://github.com/jamesdu031/echec/releases](https://github.com/jamesdu031/echec/releases)

--------
Fonctionnement
-

Pour le fonctionnement détaillé (Respect des règles, menu...) voir le **[wiki](https://github.com/jamesdu031/echec/wiki)**  

**Importation**


    import pygame
    from pygame.locals import *
    import time
    
**Affichage du damier**
 
 
     BLACK = (150,   150,   150  )  #Set color
     WHITE  = (255,   255,   255)
     
     B  = 0 #Set value
     W = 1
     
     colours =   {
                B  : BLACK,    #Couleur
                W : WHITE,
               }
               
     tilemap = [
            [B,W,B,W,B,W,B,W], #Creation du damier
            [W,B,W,B,W,B,W,B],
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B],
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B],
            [B,W,B,W,B,W,B,W],
            [W,B,W,B,W,B,W,B]
          ]
          
**Initialisation Pygame**
 
 
     TILESIZE  = 100
     MAPWIDTH  = 8
     MAPHEIGHT = 8

     pygame.init()
     DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
     reine = []
     tour = []
              #Ouverture de la fen?ere Pygame
     fenetre = pygame.display.set_mode((800, 800))
     pygame.display.set_caption('Echec')
              #Chargement et collage du fond

              #Chargement et collage des pieces
     reinep = pygame.image.load("pion/reine.png").convert_alpha()
     reine = [0,0]
     fenetre.blit(reinep, (reine[0], reine[1]))

     tourp = pygame.image.load("pion/tour.png").convert_alpha()
     tour = [0,0]
     fenetre.blit(tourp, (tour[0], tour[1]))
     
**Fonction et Initialisation des postions des pièces**


    def pos_piece(piece, abscisse, ordonnee):   #Fonction postion des piece par rapport au damier
        if abscisse <= 7 or ordonnee <= 7:
            piece[0] = abscisse*(800/8)
            piece[1] = ordonnee*(800/8)
        if abscisse > 7 or ordonnee > 7:
            print("Error, piece value is too high")
            piece[0] = 0
            piece[1] = 0


    pos_piece(tour, 0, 0)    #Initialisation des postions des pieces
    pos_piece(reine, 3, 0)

    pygame.display.flip()    #Affichage Fenetre pygame


**Boucle principal**


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
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]],     (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                    
                    
**Affichage des pièces et fin du programme**


      reinepo = fenetre.blit(reinep, (reine[0], reine[1]))
      tourpo = fenetre.blit(tourp, (tour[0], tour[1]))
        #Rafraichissement
      pygame.display.flip()
    pygame.quit()
 
 

----------
Les pièces
-

**Les pièces sont de 100x100 pixels au format PNG et avec une couche alpha:**

![](https://raw.githubusercontent.com/jamesdu031/echec/master/pion/chavalier.png)
![](https://raw.githubusercontent.com/jamesdu031/echec/master/pion/fou.png)
![](https://raw.githubusercontent.com/jamesdu031/echec/master/pion/pion.png)
![](https://raw.githubusercontent.com/jamesdu031/echec/master/pion/reine.png)
![](https://raw.githubusercontent.com/jamesdu031/echec/master/pion/roi.png)
![](https://raw.githubusercontent.com/jamesdu031/echec/master/pion/tour.png)


----------
Le damier
-

**Le damier est générer par le programme (voir [#fonctionnement](#fonctionnement))**

Les cases noirs ont une couleur (RGB) de: **150 150 150**  
Les cases blanches ont une couleur (RGB) de: **255 255 255**  
Pour plus de détail voir le **[wiki](https://github.com/jamesdu031/echec/wiki)**.  


----------
Capture
-

**Voici des captures (v0.1-alpha.1)** 
 
<img src="https://raw.githubusercontent.com/jamesdu031/echec/master/screen.PNG" alt="" width="200" height="200"/>

----------
**Pour toutes questions, erreur/bug voir [issues](https://github.com/jamesdu031/echec/issues).**  

MIT License Copyright (c) 2018
