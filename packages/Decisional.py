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
	aleatTemp = random.randint(0,100)

	if 0 <= aleatTemp <= 15 :
		Temperature = "polaire"

	elif 15 < aleatTemp <= 25 :
		Temperature = "sous-polaire"

	else :
		Temperature = random.choice(["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"])

	# Génération de la Pluviometrie Annuelle de manière coordonnée
	# avec la temperature pour éviter les situations impossibles
	if Temperature == "polaire":
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500)])

	elif Temperature == "sous-polaire" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000)])

	elif Temperature == "boreal" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000)])

	elif Temperature == "tempere_frais" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000)])

	elif Temperature == "tempere_tiede" or Temperature == "sous-tropical" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000)])

	elif Temperature == "tropical" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000),random.randint(8000,16000)])

	# Placement de la 1ere case
	Plateau[0][0]=Choix_Biome(Biomes, Temperature, PlAn)
	return Plateau

###############################################################
######################### CHOIX_BIOME #########################
###############################################################
# Renvoit l'id du Biome avec les caracteristiques Temperature
# et PlAn correspondantes
def Choix_Biome(Biomes, Temperature, PlAn):
	for Biome in Biomes.values():
		if Biome.in_range(Temperature, PlAn):
			return Case(Biome.id, Temperature, PlAn)
	return Case("NULL", Temperature, PlAn)
