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
########################## Temp ###############################
###############################################################
# Génération de la temperature en utilisant le bruit de Perlin.
def Temp_xy(x,y):
	return noise.noise2(x,y) * 3

###############################################################
########################## PlAn ###############################
###############################################################
# Génération de la Pluviometrie Annuelle en utilisant le bruit
# de Perlin, de manière coordonnée avec la temperature pour
# éviter les situations impossibles.
def PlAn_xy(x,y,Temp):
	for i in range(7) :
		if i-3 <= Temp <= i - 2:
			return noise.noise2(x,y) * 0.5 * (i + 3) + (-2.5 + 0.5 * i)

	return 5




###############################################################
######################### CHOIX_BIOME #########################
###############################################################
# Renvoit l'id du Biome avec les caracteristiques Temperature
# et PlAn correspondantes.
def Choix_Biome(Biomes, Temp, PlAn):
	for Biome in Biomes.values():
		if Biome.in_range(Temp, PlAn):
			return Case(Biome.id, Temp, PlAn)
	print(Temp,PlAn)
	return Case("NULL", Temp, PlAn)
