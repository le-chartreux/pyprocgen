import os
from .p_creation_biomes_dic import f_creation_dic_couleurs_biomes

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
	# - p_classes.cl_sol_biome
	# - p_image_creation.f_mise_en_vecteur()
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	v_dic_biomes = f_creation_dic_couleurs_biomes()

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
			fi_fichier_dest.write(v_dic_biomes[v_nom].coul_sol)
			fi_fichier_dest.write(" ")

		fi_fichier_dest.write("\n")

		print("Creating the map's image : ",round((v_num_ligne + 1)/len(v_plateau)*100,2),"%", end = "\r")

	print("")

	fi_fichier_dest.close()
