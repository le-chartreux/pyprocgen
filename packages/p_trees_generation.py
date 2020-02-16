from .p_classes import cl_box, cl_tree
from .p_board_functions import f_print_progression

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Génère les arbres dans le plateau
# -----------------------------
# CONTENU :
# - f_possible_to_place_tree(v_plateau, v_dic_arbres, v_x, v_y)
# - f_put_tree(v_plateau, v_dic_arbres, v_x, v_y)
# - f_generate_trees(v_plateau)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

###############################################################
################# F_POSSIBLE_TO_PLACE_TREE ####################
###############################################################
def f_possible_to_place_tree(v_plateau, v_dic_arbres, v_x, v_y):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Renvoie si il est possible de placer un arbre poussant dans ce
	# biome à partir du point v_plateau[v_y][v_x]
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_arbres est un dictionnaire contenant au moins un type
	# 	d'arbre poussant dans le biome de v_plateau[v_y][v_x], sauf si
	#	v_plateau[v_y][v_x] est une case Arbre
	# - v_x : integer, <= len(v_plateau[0])
	# - v_y : integer, <= len(v_plateau)
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_box
	# - p_classes.cl_tree
	# -----------------------------
	# UTILISE PAR :
	# - p_trees_creation.f_generate_trees()
	# =============================

	v_type_case_origine = v_plateau[v_y][v_x].nom_biome


	if v_type_case_origine in ["Tree", "Water", "Rocks_and_ice", "Toundra_Dry", "Toundra_Moist", "Steppe", "Cyan_Water1", "Cyan_Water2",  "Cyan_Water3", "Cyan_Water4", "Cyan_Water5", "Cyan_Water6", "Cyan_Water7", "Cyan_Water8", "Cyan_Water9", "Cyan_Water10"] :
		return False

	v_vect_arbre = v_dic_arbres[v_type_case_origine]

	v_larg_arbre = v_vect_arbre.f_get_width()
	v_haut_arbre = v_vect_arbre.f_get_height()


	if v_y + v_haut_arbre > len(v_plateau):
		v_haut_arbre = len(v_plateau) - v_y

	if v_x + v_larg_arbre > len(v_plateau[0]):
		v_larg_arbre = len(v_plateau[0]) - v_x


	for v_num_ligne in range(v_haut_arbre):

		for v_num_colonne in range(v_larg_arbre):

			if v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].nom_biome[0:5] != v_type_case_origine[0:5] and v_vect_arbre.body[v_num_ligne][v_num_colonne] :
				return False


	return True


###############################################################
######################### F_PUT_TREE ##########################
###############################################################
def f_put_tree(v_plateau, v_dic_arbres, v_x, v_y):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Place un arbre depuis le point v_plateau[v_y][v_x]
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_arbres est un dictionnaire contenant au moins un type
	# 	d'arbre poussant dans le biome de v_plateau[v_y][v_x], sauf si
	#	v_plateau[v_y][v_x] est une case Arbre
	# - v_x : integer, <= len(v_plateau[0])
	# - v_y : integer, <= len(v_plateau)
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_box
	# - p_classes.cl_tree
	# -----------------------------
	# UTILISE PAR :
	# - p_trees_creation.f_generate_trees()
	# =============================

	v_type_case_origine = v_plateau[v_y][v_x].nom_biome

	v_vect_arbre = v_dic_arbres[v_type_case_origine].body

	v_larg_arbre = len(v_vect_arbre[0])
	v_haut_arbre = len(v_vect_arbre)


	if v_y + v_haut_arbre > len(v_plateau):
		v_haut_arbre = len(v_plateau) - v_y

	if v_x + v_larg_arbre > len(v_plateau[0]):
		v_larg_arbre = len(v_plateau[0]) - v_x


	for v_num_ligne in range(v_haut_arbre):

		for v_num_colonne in range(v_larg_arbre):

			if v_vect_arbre[v_num_ligne][v_num_colonne] != None :

				v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].nom_biome = "Tree"

				v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].coul = v_vect_arbre[v_num_ligne][v_num_colonne]




###############################################################
###################### F_GENERATE_TREE ########################
###############################################################
def f_generate_trees(v_plateau, v_dic_arbres):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Place les arbres dans v_plateau
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_arbres : dictionnaire d'arbres comprenant
	# un arbre pour tous les biomes qui ne sont pas dans [
	# 	"Tree", "Water", "Rocks_and_ice",
	# 	"Toundra_Dry", "Toundra_Moist", "Steppe",
	# 	"Cyan_Water1", "Cyan_Water2",  "Cyan_Water3",
	# 	"Cyan_Water4", "Cyan_Water5", "Cyan_Water6",
	# 	"Cyan_Water7", "Cyan_Water8", "Cyan_Water9",
	# 	"Cyan_Water10"
	# ]
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_box
	# - p_classes.cl_tree
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	import random


	v_nbx = len(v_plateau[0])
	v_nby = int(len(v_plateau) / 2)

	for v_num_ligne in range(v_nby):

		for v_num_colonne in range(v_nbx):

			if f_possible_to_place_tree(v_plateau, v_dic_arbres, v_num_colonne, v_num_ligne) and random.random() < v_dic_arbres[v_plateau[v_num_ligne][v_num_colonne].nom_biome].prob_arbre :

				f_put_tree(v_plateau, v_dic_arbres, v_num_colonne, v_num_ligne)


	return v_plateau
