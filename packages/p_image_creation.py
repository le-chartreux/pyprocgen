import os
from .p_classes import C_Image

###############################################################
################# LIRE_MOTS_DEPUIS_FICHIER ####################
###############################################################
# Renvoie le(s) mot(s) d'une ligne d un fichier sans le \n
def Lire_Mots_Depuis_Fichier(Fichier):
	string=""
	courant=Fichier.read(1) #Lit le 1er caractère de la ligne
	while courant!="\n" and courant!="" :
		string+=courant
		courant=Fichier.read(1) #Lit le caractère après le dernier caractère lu
	return string

###############################################################
##################### MISE_EN_VECTEUR #########################
###############################################################
# Prend le nom d'un biome, ouvre son fichier puis met son
# contenu dans un vecteur de string V, avec V[i] = ligne n°i du
# body de l'image
def Mise_En_Vecteur(NomBiome):
	Fichier = open("biomes_images/" + NomBiome + ".ppm","r")
	V = []
	# Saut du header
	for i in range(4):
		Lire_Mots_Depuis_Fichier(Fichier)
	# Lecture des 16 lignes du fichier
	for i in range(16):
		V.append(Lire_Mots_Depuis_Fichier(Fichier))
	return V

###############################################################
####################### AJOUT_IMAGE ###########################
###############################################################
# Ajoute Image dans le dictionnaire ImagesChargees
def Ajout_Image(ImagesChargees,Image):
	ImagesChargees[Image.NomBiome] = Image



def image_creation(Plateau):
	FichierDest = open("Generated_map.ppm","w")
	# Creation du header
	FichierDest.write("P3\n")
	FichierDest.write("# Generation_procedurale.ppm\n")
	FichierDest.write(str(16 * len(Plateau[0])))
	FichierDest.write("\n")
	FichierDest.write(str(16 * len(Plateau)))
	FichierDest.write("\n")
	FichierDest.write("255\n")
	FichierDest.write("\n")

	ImagesChargees = {}

	# Creation du body
	for num_ligne_tableau in range(len(Plateau)):
		for num_ligne in range(16):
			for i in range(len(Plateau[0])):
				Nom = Plateau[num_ligne_tableau][i].type

				ImagePresente = False
				for VarImage in ImagesChargees.values():
					if Nom == VarImage.NomBiome:
						ImagePresente = True

				if not ImagePresente :
					a = C_Image(Nom,Mise_En_Vecteur(Nom))
					Ajout_Image(ImagesChargees,a)

				FichierDest.write(ImagesChargees[Nom].Vect[num_ligne])
				FichierDest.write(" ")

			FichierDest.write("\n")
		print("Creating the map's image : ",round((num_ligne_tableau + 1)/len(Plateau)*100,2),"%", end = '\r')
	print("")

	FichierDest.close()
