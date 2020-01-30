import os
from .p_classes import cl_image

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer une image à partir du vecteur v_plateau
# -----------------------------
# CONTENU :
# - f_lire_mots_depuis_fichier(fi_fichier)
# - f_mise_en_vecteur(v_nom_biome)
# - f_ajout_image(v_images_chargees,v_image)
# - f_image_creation(v_plateau, v_seed)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================



###############################################################
################# LIRE_MOTS_DEPUIS_FICHIER ####################
###############################################################
def f_lire_mots_depuis_fichier(fi_fichier):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Renvoie le(s) mot(s) d'une ligne d'un fichier sans le \n
	# sous la forme d'un string
	# -----------------------------
	# PRECONDITIONS :
	# - fi_fichier ouvert en lecture, fi_fichier- = <>, fi_ficher+ != <>
	# -----------------------------
	# DEPEND DE :
	# - os
	# -----------------------------
	# UTILISE PAR :
	# - f_mise_en_vecteur()
	# =============================

	v_string=""
	v_tampon=fi_fichier.read(1) #Lit le 1er caractère de la ligne

	while v_tampon!="\n" and v_tampon!="" :

		v_string+=v_tampon
		v_tampon=fi_fichier.read(1) #Lit le caractère après le dernier caractère lu

	return v_string



###############################################################
##################### MISE_EN_VECTEUR #########################
###############################################################
def f_mise_en_vecteur(v_nom_biome):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Prend le nom d'un biome, ouvre son fichier puis met son
	# body dans un string.
	# -----------------------------
	# PRECONDITIONS :
	# - v_nom_biome est un nom de biome valide
	# -----------------------------
	# DEPEND DE :
	# - os
	# - p_image_creation.f_lire_mots_depuis_fichier()
	# -----------------------------
	# UTILISE PAR :
	# - f_image_creation()
	# =============================

	fi_fichier = open("biomes_grounds/" + v_nom_biome + ".ppm","r")

	# Saut du header
	for i in range(4):
		f_lire_mots_depuis_fichier(fi_fichier)

	# Lecture du body du fichier
	v_string = f_lire_mots_depuis_fichier(fi_fichier)

	return v_string



###############################################################
####################### AJOUT_IMAGE ###########################
###############################################################
def f_ajout_image(v_images_chargees,v_image):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute v_image dans le dictionnaire v_images_chargees
	# -----------------------------
	# PRECONDITIONS :
	# - v_images_chargees : dictionnaire
	# - v_image : cl_image
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_image
	# -----------------------------
	# UTILISE PAR :
	# - f_image_creation()
	# =============================
	v_images_chargees[v_image.nom_biome] = v_image



###############################################################
###################### IMAGE_CREATION #########################
###############################################################
def f_image_creation(v_plateau, v_seed):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Crée une image à partir de v_plateau
	# -----------------------------
	# PRECONDITIONS :
	# - v_seed : not null
	# -----------------------------
	# DEPEND DE :
	# - os
	# - p_classes.cl_image
	# - p_image_creation.f_mise_en_vecteur()
	# -----------------------------
	# UTILISE PAR :
	# - f_image_creation()
	# =============================

	fi_fichier_dest = open("Generated_map.ppm", "w")

	# Creation du header
	fi_fichier_dest.write("P3\n")
	fi_fichier_dest.write("# Tx = " + str(v_seed["Tx"]) + "\n")
	fi_fichier_dest.write("# Ty = " + str(v_seed["Ty"]) + "\n")
	fi_fichier_dest.write("# Px = " + str(v_seed["Px"]) + "\n")
	fi_fichier_dest.write("# Py = " + str(v_seed["Py"]) + "\n")
	fi_fichier_dest.write(str(len(v_plateau[0])))
	fi_fichier_dest.write("\n")
	fi_fichier_dest.write(str(len(v_plateau)))
	fi_fichier_dest.write("\n")
	fi_fichier_dest.write("255\n")
	fi_fichier_dest.write("\n")

	v_images_chargees = {}

	# Creation du body
	for v_num_ligne in range(len(v_plateau)):
		for v_num_colonnes in range(len(v_plateau[0])):
			v_nom = v_plateau[v_num_ligne][v_num_colonnes].type

			v_image_presente = False
			for v_var_image in v_images_chargees.values():
				if v_nom == v_var_image.nom_biome:
					v_image_presente = True

			if not v_image_presente :
				v_tampon = cl_image(v_nom,f_mise_en_vecteur(v_nom))
				f_ajout_image(v_images_chargees,v_tampon)

			fi_fichier_dest.write(v_images_chargees[v_nom].body)
			fi_fichier_dest.write(" ")

			fi_fichier_dest.write("\n")

		print("Creating the map's image : ",round((v_num_ligne + 1)/len(v_plateau)*100,2),"%", end = "\r")

	print("")

	fi_fichier_dest.close()
