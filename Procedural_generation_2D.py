from packages.Biomes_creation import *
from packages.Decisional import *
from packages.Board_functions import *
import random

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.

seed = {}
seed['x'] = random.randint(-100000,100000)
seed['y'] = random.randint(-100000,100000)
print(seed)

Biomes = Creation_Constantes_Biomes()
Plateau = Creer_Plateau_Vide()

for i in range (len(Plateau)) :
	for j in range (len(Plateau[0])) :
			Placer_Case(Plateau, Biomes, i, j, seed)

Afficher_Plateau(Plateau)
