import random
from .p_biomes_creation import *
from .p_classes import Case
from .p_perlin_noise import SimplexNoise
noise = SimplexNoise()

# FONCTIONS DECISIONNELLES
# Fonctions qui servent à gérer l'évolution du terrain et
# à prendre la décisison du type de case à placer en (x,y)


###############################################################
#################### PLACER_CASE #########################
###############################################################
# Génère une case en (x,y)
def Placer_Case(Biomes, x, y, seed):

	Temp = Temp_xy(seed['Tx'] + x/30,seed['Ty'] + y/30)
	PlAn = PlAn_xy(seed['Px'] + x/30,seed['Py'] + y/30, Temp)
	return Choix_Biome(Biomes, Temp, PlAn)

###############################################################
######################### CHOIX_BIOME #########################
###############################################################
# Renvoit l'id du Biome avec les caracteristiques Temperature
# et PlAn correspondantes.
def Choix_Biome(Biomes, Temp, PlAn):
	for Biome in Biomes.values():
		if Biome.in_range(Temp, PlAn):
			return Case(Biome.id, Temp, PlAn)
	return Case("NULL", Temp, PlAn)

###############################################################
########################## Temp ###############################
###############################################################
# Génération de la temperature en utilisant le bruit de Perlin.
# Bruit ensuite échelonné entre -10 et 35
def Temp_xy(x,y):
	return 12 + noise.noise2(x,y) * 22.5

###############################################################
########################## PlAn ###############################
###############################################################
# Génération de la Pluviometrie Annuelle en utilisant le bruit
# de Perlin, de manière coordonnée avec la temperature pour
# éviter les situations impossibles.
# Bruit ensuite  échelonné entre 62 et 16000
def PlAn_xy(x,y,Temp):
	PlAn_min = 62
	PlAn_max = 500

	for i in range(6):
		if Temp <= 1.5 * 2**i :
			return (PlAn_min + PlAn_max)/2 + noise.noise2(x,y) * ((PlAn_max + PlAn_min) / 2 - PlAn_max)
		else :
			PlAn_max = PlAn_max * 2
	return None
