# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer une image à partir du vecteur v_plateau
# -----------------------------
# CONTENU :
# - f_create_image_header(v_haut, v_larg, v_seed)
# - f_create_image_body(v_plateau)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

import os
from .p_classes import cl_box
from .p_board_functions import f_print_progression


###############################################################
################### F_CREATE_IMAGE_HEADER #####################
###############################################################
def f_create_image_header(fi_fichier_dest, v_haut, v_larg, v_seed):
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
	# - v_seed : string
	# -----------------------------
	# DEPEND DE :
	# - os
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	fi_fichier_dest.write("P3\n")
	fi_fichier_dest.write("# Seed : " + v_seed + "\n")
	fi_fichier_dest.write(str(v_larg))
	fi_fichier_dest.write("\n")
	fi_fichier_dest.write(str(v_haut))
	fi_fichier_dest.write("\n")
	fi_fichier_dest.write("255\n")
	fi_fichier_dest.write("\n")


###############################################################
##################### F_CREATE_IMAGE_BODY #####################
###############################################################

def f_create_image_body(fi_fichier_dest, v_plateau, v_dic_biomes):
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

			fi_fichier_dest.write(v_plateau[v_num_ligne][v_num_colonnes].m_get_couleur(v_dic_biomes))
			fi_fichier_dest.write(" ")

		fi_fichier_dest.write("\n")
