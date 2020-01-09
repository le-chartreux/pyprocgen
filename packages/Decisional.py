import random
from .Biomes_creation import *
from .Classes import Case

###############################################################
################# FONCTIONS DECISIONNELLES ####################
###############################################################

###############################################################
#################### PLACER_1ERE_CASE #########################
###############################################################
# Crée aléatoirement la 1ère case puis la place en (0,0)

def Placer_1ere_Case(Plateau, Biomes):
	# Conditionnement pour éviter la sureprésentation des biomes
	# polaires au spawn
	Temp = random.randint(-10,35)

	# Génération de la Pluviometrie Annuelle de manière coordonnée
	# avec la temperature pour éviter les situations impossibles
	if -10 <= Temp <= 1.5 :
		PlAn = random.choice([random.randint(62,125),random.randint(125,250),random.randint(250,500)])

	elif 1.5 <= Temp <= 3 :
		PlAn = random.choice([random.randint(62,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000)])

	elif 3 <= Temp <= 6 :
		PlAn = random.choice([random.randint(62,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000)])

	elif 6 <= Temp <= 12 :
		PlAn = random.choice([random.randint(62,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000)])

	elif 12 <= Temp <= 24 :
		PlAn = random.choice([random.randint(62,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000)])

	elif 24 <= Temp <= 35 :
		PlAn = random.choice([random.randint(62,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000),random.randint(8000,16000)])

	# Placement de la 1ere case
	Plateau[0][0]=Choix_Biome(Biomes, Temp, PlAn)
	return Plateau

###############################################################
######################### CHOIX_BIOME #########################
###############################################################
# Renvoit l'id du Biome avec les caracteristiques Temperature
# et PlAn correspondantes
def Choix_Biome(Biomes, Temp, PlAn):
	for Biome in Biomes.values():
		if Biome.in_range(Temp, PlAn):
			return Case(Biome.id, Temp, PlAn)
	return Case("NULL", Temp, PlAn)
