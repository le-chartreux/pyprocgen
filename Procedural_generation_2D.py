from packages.Biomes_creation import *
from packages.Decisional import *
from packages.Board_functions import *
from packages.Perlin_noise import SimplexNoise

###############################################################
##################### CORPS DU PROGRAMME ######################
###############################################################

Biomes = Creation_Constantes_Biomes()
Plateau = Creer_Plateau_Vide()
Plateau = Placer_1ere_Case(Plateau, Biomes)
Afficher_Plateau(Plateau)

## DEBUG ##
noise = SimplexNoise()
value = noise.noise2(68189, 5198481)

print("Noise value : ", value)