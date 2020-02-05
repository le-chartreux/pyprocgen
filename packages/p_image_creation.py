import os
from .p_classes import cl_box
from .p_board_functions import f_print_progression

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer une image à partir du vecteur v_plateau
# -----------------------------
# CONTENU :
# - f_image_creation(v_plateau, v_seed)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================


###############################################################
##################### F_IMAGE_CREATION ########################
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
	# - p_classes.cl_box
	# - p_board_functions.f_print_progression
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
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

			fi_fichier_dest.write(v_plateau[v_num_ligne][v_num_colonnes].coul)
			fi_fichier_dest.write(" ")

		fi_fichier_dest.write("\n")

		f_print_progression("Creating the map's image :             ", (v_num_ligne + 1)/len(v_plateau))

	print("")

	fi_fichier_dest.close()
