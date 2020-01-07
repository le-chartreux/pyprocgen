import random
import math
###############################################################
##################### CONSTANTES DES CASES ####################
###############################################################
# Forme : [NomCase,[Temperatures possibles],Borne inf PlAn,Borne sup PlAn]
T_Type_Case = []
T_Type_Case.append(["DsCh",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],0,125])
T_Type_Case.append(["FHmd",["boreal"],500,1000])
T_Type_Case.append(["FHmd",["tempere_frais"],1000,2000])
T_Type_Case.append(["FHmd",["tempere_tiede","sous-tropical"],2000,4000])
T_Type_Case.append(["FHmd",["tropical"],4000,8000])
T_Type_Case.append(["FPlv",["boreal"],1000,2000])
T_Type_Case.append(["FPlv",["tempere_frais"],2000,4000])
T_Type_Case.append(["FTrp",["tempere_tiede","sous-tropical"],4000,8000])
T_Type_Case.append(["FTrp",["tropical"],8000,16000])
T_Type_Case.append(["FTpr",["boreal"],250,500])
T_Type_Case.append(["FTpr",["tempere_frais"],500,1000])
T_Type_Case.append(["FTpr",["tempere_tiede","sous-tropical"],1000,2000])
T_Type_Case.append(["FTpr",["tropical"],2000,4000])
T_Type_Case.append(["FSch",["tempere_tiede","sous-tropical"],500,1000])
T_Type_Case.append(["FSch",["tropical"],1000,2000])
T_Type_Case.append(["FTSc",["tropical"],500,1000])
T_Type_Case.append(["MaqD",["tempere_frais","tempere_tiede","sous-tropical","tropical"],125,250])
T_Type_Case.append(["Maqi",["tempere_tiede","sous-tropical","tropical"],250,500])
T_Type_Case.append(["MaqS",["boreal"],125,250])
T_Type_Case.append(["Stpe",["tempere_frais"],250,500])
T_Type_Case.append(["RoEG",["polaire"],0,125])
T_Type_Case.append(["Taig",["polaire"],125,500])
T_Type_Case.append(["TndS",["sous-polaire"],0,125])
T_Type_Case.append(["Toun",["sous-polaire"],125,1000])

T_Type_Case.append(["NULL",[""],0,0])
###############################################################
########################## FONCTIONS ##########################
###############################################################

########################## BETWEEN ############################
# Regarde si val est compris entre min et max
def Between(val,min,max):
	if val >= min and val <=max :
		return True
	else :
		return False

###############################################################
#################### FONCTIONS DE CREATION ####################
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

#################### PLACER_1ERE_CASE #########################
# Crée aléatoirement la 1ere case puis la place en (0,0)
def Placer_1ere_Case(Plateau):

	#Conditionnement pour éviter la sureprésentation des biomes polaires
	aleatTemp = random.randint(0,100)

	if Between(aleatTemp,0,15) :
		Temperature = "polaire"

	elif Between(aleatTemp,15,25) :
		Temperature = "sous-polaire"

	else :
		Temperature = random.choice(["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"])


	#Génération de la Pluviometrie Annuelle de manière coordonnée avec la temperature pour éviter les situations impossibles
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

	#Placement de la 1ere case
	Plateau[0][0]=Case(Type_Case(Temperature, PlAn),Temperature,PlAn)
	return Plateau

########################## TYPE_CASE ##########################
def Type_Case(Temperature, PlAn):
	i = 0
	while i < len(T_Type_Case) - 1 and not (Temperature in T_Type_Case[i][1] and Between(PlAn,T_Type_Case[i][2],T_Type_Case[i][3])) :
		i += 1
	return T_Type_Case[i][0]


###############################################################
################## FONCTIONS D AFFICHAGE ######################
###############################################################

def Afficher_Plateau(Plateau):
	for i in range (len(Plateau)) :
		for j in range (len(Plateau[0])):
			print(Plateau[i][j].type, ' ',end='')
		print('')
###############################################################
########################## CLASSE #############################
###############################################################
class Case:
	""" Classe définissant une case caractérisée par :
	- son type
	- sa Température
	- sa Pluviometrie Annuelle
	"""

	def __init__(self, type, Temperature, PlAn):
		# CONSTRUCTION DE LA CLASSE #
		self.type = type
		self.Temperature = Temperature
		self.PlAn = PlAn



###############################################################
##################### CORPS DU PROGRAMME ######################
###############################################################

Plateau=Creer_Plateau_Vide()
#Afficher_Plateau(Plateau)
print(len(Plateau))
Plateau = Placer_1ere_Case(Plateau)
Afficher_Plateau(Plateau)
