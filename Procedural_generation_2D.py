from packages.Biomes_creation import *
from packages.Decisional import *
from packages.Board_functions import *

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.


Biomes = Creation_Constantes_Biomes()
Plateau = Creer_Plateau_Vide()

for i in range (len(Plateau)) :
	for j in range (len(Plateau[0])) :
			Placer_Case(Plateau, Biomes, i, j)

Afficher_Plateau(Plateau)
