from packages.Classes import *
from packages.Biomes_creation import *
from packages.Decisional import *
from packages.Board_functions import *



###############################################################
##################### CORPS DU PROGRAMME ######################
###############################################################

Plateau = Creer_Plateau_Vide()
Plateau = Placer_1ere_Case(Plateau, Biomes)
Afficher_Plateau(Plateau)
