import random
import math

###############################################################
########################## CLASSES ############################
###############################################################

######################### BIOME ###############################
# Classe définisant un biome, caractérisé par :
# - son identifiant (en 4 caractères)
# - sa temperature
# - sa Pluviometrie Annuelle Minimale
# - sa Pluviometrie Annuelle Minimale
class Biome:

	def __init__(self, id, Temperature, PlAnMin, PlAnMax):
		self.id = id
		self.Temperature = Temperature
		self.PlAnMin = PlAnMin
		self.PlAnMax = PlAnMax

	def in_range(self, Temperature, PlAn):
		return Temperature in self.Temperature and self.PlAnMin <= PlAn < self.PlAnMax


########################## CASE ##############################
# Classe définissant une case, caractérisée par :
# - son type
# - sa Température
# - sa Pluviometrie Annuelle
class Case:

	def __init__(self, type, Temperature, PlAn):
		# CONSTRUCTION DE LA CLASSE #
		self.type = type
		self.Temperature = Temperature
		self.PlAn = PlAn


###############################################################
########################## FONCTIONS ##########################
###############################################################

########################## BETWEEN ############################
# Regarde si val est compris entre min et max

def Between(val,min,max):
 	return min <= val <= max


######################### AJOUT_BIOME #########################
# Ajoute Biome dans le dicionnaire Biomes
def Ajout_Biome(Biomes, Biome):
	Biomes[Biome.id] = Biome


################# CREATION_CONSTANTES_BIOMES ##################
def Creation_Constantes_Biomes():
	Biomes = {}
	Ajout_Biome(Biomes, Biome("DsCh",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],0,125))
	Ajout_Biome(Biomes, Biome("FHmd",["boreal"],500,1000))
	Ajout_Biome(Biomes, Biome("FHmd",["tempere_frais"],1000,2000))
	Ajout_Biome(Biomes, Biome("FHmd",["tempere_tiede","sous-tropical"],2000,4000))
	Ajout_Biome(Biomes, Biome("FHmd",["tropical"],4000,8000))
	Ajout_Biome(Biomes, Biome("FPlv",["boreal"],1000,2000))
	Ajout_Biome(Biomes, Biome("FPlv",["tempere_frais"],2000,4000))
	Ajout_Biome(Biomes, Biome("FTrp",["tempere_tiede","sous-tropical"],4000,8000))
	Ajout_Biome(Biomes, Biome("FTrp",["tropical"],8000,16000))
	Ajout_Biome(Biomes, Biome("FTpr",["boreal"],250,500))
	Ajout_Biome(Biomes, Biome("FTpr",["tempere_frais"],500,1000))
	Ajout_Biome(Biomes, Biome("FTpr",["tempere_tiede","sous-tropical"],1000,2000))
	Ajout_Biome(Biomes, Biome("FTpr",["tropical"],2000,4000))
	Ajout_Biome(Biomes, Biome("FSch",["tempere_tiede","sous-tropical"],500,1000))
	Ajout_Biome(Biomes, Biome("FSch",["tropical"],1000,2000))
	Ajout_Biome(Biomes, Biome("FTSc",["tropical"],500,1000))
	Ajout_Biome(Biomes, Biome("MaqD",["tempere_frais","tempere_tiede","sous-tropical","tropical"],125,250))
	Ajout_Biome(Biomes, Biome("Maqi",["tempere_tiede","sous-tropical","tropical"],250,500))
	Ajout_Biome(Biomes, Biome("MaqS",["boreal"],125,250))
	Ajout_Biome(Biomes, Biome("Stpe",["tempere_frais"],250,500))
	Ajout_Biome(Biomes, Biome("RoEG",["polaire"],0,125))
	Ajout_Biome(Biomes, Biome("Taig",["polaire"],125,500))
	Ajout_Biome(Biomes, Biome("TndS",["sous-polaire"],0,125))
	Ajout_Biome(Biomes, Biome("Toun",["sous-polaire"],125,1000))



###############################################################
#################### FONCTIONS DU PLATEAU  ####################
###############################################################

#################### CREER_PLATEAU_VIDE #######################
# Crée un plateau vide de x cases de largeur et y de longueur

def Creer_Plateau_Vide():
	nbx=eval(input("x = "))
	nby=eval(input("y = "))
	Plateau=[]
	for i in range (nby) :
		Plateau.append([])
		for j in range (nbx) :
			Plateau[i].append(Case(None,None,None))
	return Plateau

######################## PLACER_CASE ##########################
# Place en (x,y) la case correspondant aux caracteristiques
# Temperature et PlAn
def Placer_Case(Plateau, x, y, Temperature, PlAn):
	return Case(Choix_Biome(Temperature, PlAn), Temperature, PlAn)


###############################################################
################# FONCTIONS DECISIONNELLES ####################
###############################################################

#################### PLACER_1ERE_CASE #########################
# Crée aléatoirement la 1ere case puis la place en (0,0)

def Placer_1ere_Case(Plateau):
	# Conditionnement pour éviter la sureprésentation des biomes
	# polaires au spawn
	aleatTemp = random.randint(0,100)

	if Between(aleatTemp,0,15) :
		Temperature = "polaire"

	elif Between(aleatTemp,15,25) :
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
	Plateau[0][0]=Choix_Biome(Temperature, PlAn)
	return Plateau


######################### CHOIX_BIOME ########################
# Renvoit l'id du Biome avec les caracteristiques Temperature
# et PlAn correspondantes
def Choix_Biome(Temperature, PlAn):
	for Biome in Biomes.values():
		if Biome.in_range(Temperature, PlAn):
			return Case(Biome.id, Temperature, PlAn)
	return Case("NULL", Temperature, PlAn)





###############################################################
################## FONCTIONS D AFFICHAGE ######################
###############################################################

def Afficher_Plateau(Plateau):
	for i in range (len(Plateau)) :
		for j in range (len(Plateau[0])):
			print(Plateau[i][j].type, ' ',end='')
		print('')







###############################################################
##################### CORPS DU PROGRAMME ######################
###############################################################

Biomes = Creation_Constantes_Biomes()
Plateau = Creer_Plateau_Vide()
Plateau = Placer_1ere_Case(Plateau)
Afficher_Plateau(Plateau)
