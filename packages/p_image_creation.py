import os
from .p_classes import cl_image

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer une image à partir du vecteur Plateau
# -----------------------------
# CONTENU :
# - f_lire_mots_depuis_fichier(Fichier)
# - f_mise_en_vecteur(NomBiome)
# - f_ajout_image(ImagesChargees,Image)
# - f_image_creation(Plateau)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================



###############################################################
################# LIRE_MOTS_DEPUIS_FICHIER ####################
###############################################################
def f_lire_mots_depuis_fichier(Fichier):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Renvoie le(s) mot(s) d'une ligne d un fichier sans le \n
	# -----------------------------
	# PRECONDITIONS :
	# - Fichier ouvert en lecture, Fichier- = <>,Ficher+ != <>
	# -----------------------------
	# DEPEND DE :
	# - os
	# -----------------------------
	# UTILISE PAR :
	# - f_mise_en_vecteur()
	# =============================

	string=""
	courant=Fichier.read(1) #Lit le 1er caractère de la ligne

	while courant!="\n" and courant!="" :

		string+=courant
		courant=Fichier.read(1) #Lit le caractère après le dernier caractère lu

	return string



###############################################################
##################### MISE_EN_VECTEUR #########################
###############################################################
def f_mise_en_vecteur(NomBiome):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Prend le nom d'un biome, ouvre son fichier puis met son
	# contenu dans un string.
	# -----------------------------
	# PRECONDITIONS :
	# - NomBiome est un nom de biome valide
	# -----------------------------
	# DEPEND DE :
	# - os
	# - p_image_creation.f_lire_mots_depuis_fichier()
	# -----------------------------
	# UTILISE PAR :
	# - f_image_creation()
	# =============================

	Fichier = open("biomes_grounds/" + NomBiome + ".ppm","r")

	# Saut du header
	for i in range(4):
		f_lire_mots_depuis_fichier(Fichier)

	# Lecture du body du fichier
	str = f_lire_mots_depuis_fichier(Fichier)

	return str



###############################################################
####################### AJOUT_IMAGE ###########################
###############################################################
def f_ajout_image(ImagesChargees, Image):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute Image dans le dictionnaire ImagesChargees
	# -----------------------------
	# PRECONDITIONS :
	# - ImagesChargees : dictionnaire
	# - Image : cl_image
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_image
	# -----------------------------
	# UTILISE PAR :
	# - f_image_creation()
	# =============================
	ImagesChargees[Image.NomBiome] = Image



###############################################################
###################### IMAGE_CREATION #########################
###############################################################
def f_image_creation(Plateau, Seed):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Crée une image à partir de Plateau
	# -----------------------------
	# PRECONDITIONS :
	# - Seed : not null
	# -----------------------------
	# DEPEND DE :
	# - os
	# - p_classes.cl_image
	# - p_image_creation.f_mise_en_vecteur()
	# -----------------------------
	# UTILISE PAR :
	# - f_image_creation()
	# =============================

	FichierDest = open("Generated_map.ppm", "w")

	# Creation du header
	FichierDest.write("P3\n")
	FichierDest.write("# Tx = " + str(Seed["Tx"]) + "\n")
	FichierDest.write("# Ty = " + str(Seed["Ty"]) + "\n")
	FichierDest.write("# Px = " + str(Seed["Px"]) + "\n")
	FichierDest.write("# Py = " + str(Seed["Py"]) + "\n")
	FichierDest.write(str(len(Plateau[0])))
	FichierDest.write("\n")
	FichierDest.write(str(len(Plateau)))
	FichierDest.write("\n")
	FichierDest.write("255\n")
	FichierDest.write("\n")

	ImagesChargees = {}

	# Creation du body
	for num_ligne_tableau in range(len(Plateau)):
		for i in range(len(Plateau[0])):
			Nom = Plateau[num_ligne_tableau][i].type

			ImagePresente = False
			for VarImage in ImagesChargees.values():
				if Nom == VarImage.NomBiome:
					ImagePresente = True

			if not ImagePresente :
				tampon = cl_image(Nom,f_mise_en_vecteur(Nom))
				f_ajout_image(ImagesChargees,tampon)

			FichierDest.write(ImagesChargees[Nom].Str)
			FichierDest.write(" ")

			FichierDest.write("\n")

		print("Creating the map's image : ",round((num_ligne_tableau + 1)/len(Plateau)*100,2),"%", end = "\r")

	print("")

	FichierDest.close()
