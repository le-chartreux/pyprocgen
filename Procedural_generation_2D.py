from packages.Biomes_creation import *
from packages.Decisional import *
from packages.Board_functions import *
from image_creation.p_image_creation import *
import random

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.

seed = {}
seed['x'] = random.randint(-100000,100000)
seed['y'] = random.randint(-100000,100000)
print(seed)



Biomes = Creation_Constantes_Biomes()

nbx=eval(input("x = "))
nby=eval(input("y = "))
Plateau = Creer_Plateau_Vide(nbx,nby)

for i in range (len(Plateau)) :
	for j in range (len(Plateau[0])) :
			Plateau[i][j] = Placer_Case(Plateau, Biomes, i, j, seed)

#Afficher_Plateau(Plateau)

Plateau2 = Creer_Plateau_Vide(nbx,nby)

for i in range (len(Plateau)) :
	for j in range (len(Plateau[0])) :
			Plateau2[i][j] = str(Plateau[i][j].type[0:4])

image_creation(Plateau2)
