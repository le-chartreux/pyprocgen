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
# - f_create_image_body(v_plateau)
# - f_create_image_header(v_haut, v_larg, v_seed)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================


###############################################################
##################### F_CREATE_IMAGE_BODY #####################
###############################################################

def f_create_image_body(fi_fichier_dest, v_plateau):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Place à la suite de Generated_map.ppm la couleur
	# de chaque case de v_plateau
	# -----------------------------
	# PRECONDITIONS :
	# - v_seed : not null
	# -----------------------------
	# DEPEND DE :
	# - os
	# - p_classes.cl_box
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	for v_num_ligne in range(len(v_plateau)):

		for v_num_colonnes in range(len(v_plateau[0])):

			fi_fichier_dest.write(v_plateau[v_num_ligne][v_num_colonnes].coul)
			fi_fichier_dest.write(" ")

		fi_fichier_dest.write("\n")




###############################################################
################### F_CREATE_IMAGE_HEADER #####################
###############################################################
def f_create_image_header(v_haut, v_larg, v_seed):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Crée le header de Generated_map.ppm
	# selon le modèle d'un header de fichier ppm.
	# Si Generated_map.ppm existe déjà, il est
	# supprimé, sinon il est créé.
	# -----------------------------
	# PRECONDITIONS :
	# - v_seed : dictionnaire comportant un élément
	# pour les indices "Tx", "Ty", "Px" et "Py".
	# -----------------------------
	# DEPEND DE :
	# - os
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	fi_fichier_dest = open("Generated_map.ppm", "w")

	fi_fichier_dest.write("P3\n")

	fi_fichier_dest.write("# Tx = " + str(v_seed["Tx"]) + "\n")
	fi_fichier_dest.write("# Ty = " + str(v_seed["Ty"]) + "\n")
	fi_fichier_dest.write("# Px = " + str(v_seed["Px"]) + "\n")
	fi_fichier_dest.write("# Py = " + str(v_seed["Py"]) + "\n")

	fi_fichier_dest.write(str(v_larg))
	fi_fichier_dest.write("\n")
	fi_fichier_dest.write(str(v_haut))
	fi_fichier_dest.write("\n")
	fi_fichier_dest.write("255\n")
	fi_fichier_dest.write("\n")

	fi_fichier_dest.close()
