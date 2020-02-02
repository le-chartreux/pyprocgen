from .p_classes import cl_case, cl_arbre

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer le dictionnaire v_dic_conditions_biomes
# et le dicionnaire v_dic_couleurs_biomes
# -----------------------------
# CONTENU :
# - f_possible_to_place_tree(v_plateau, v_dic_arbres, v_x, v_y)
# - f_put_tree(v_plateau, v_dic_arbres, v_x, v_y)
# - f_generate_trees(v_plateau, v_dic_arbres, v_nbx, v_nby)
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
	# - p_classes.cl_case
	# - p_classes.cl_arbre
	# -----------------------------
	# UTILISE PAR :
	# - p_trees_creation.f_generate_trees()
	# =============================

	v_type_case_origine = v_plateau[v_y][v_x].type

	if v_type_case_origine == "Tree" or v_type_case_origine == "Water" or v_type_case_origine == "Rocks_and_ice" or v_type_case_origine == "Toundra_Dry" or v_type_case_origine == "Toundra_Moist" or v_type_case_origine == "Steppe":
		return False

	v_larg_arbre = len(v_dic_arbres[v_type_case_origine].body[0])
	v_haut_arbre = len(v_dic_arbres[v_type_case_origine].body)


	if v_y + v_haut_arbre > len(v_plateau):
		v_haut_arbre = len(v_plateau) - v_y

	if v_x + v_larg_arbre > len(v_plateau[0]):
		v_larg_arbre = len(v_plateau[0]) - v_x


	for v_num_ligne in range(v_haut_arbre):

		for v_num_colonne in range(v_larg_arbre):

			if v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].type != v_type_case_origine :
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
	# - p_classes.cl_case
	# - p_classes.cl_arbre
	# -----------------------------
	# UTILISE PAR :
	# - p_trees_creation.f_generate_trees()
	# =============================

	v_type_case_origine = v_plateau[v_y][v_x].type

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

				v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].type = "Tree"

				v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].coul = v_vect_arbre[v_num_ligne][v_num_colonne]




###############################################################
###################### F_GENERATE_TREE ########################
###############################################################
def f_generate_trees(v_plateau):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Place les arbres dans v_plateau
	# -----------------------------
	# PRECONDITIONS :
	# - None
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_case
	# - p_classes.cl_arbre
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	import random
	from packages.p_trees_dic_creation import f_creation_dic_arbres

	v_dic_arbres = f_creation_dic_arbres()

	v_nbx = len(v_plateau[0])
	v_nby = len(v_plateau)

	for v_num_ligne in range(v_nby):

		for v_num_colonne in range(v_nbx):

			if f_possible_to_place_tree(v_plateau, v_dic_arbres, v_num_colonne, v_num_ligne) and random.randint(1,30) == 1:

				f_put_tree(v_plateau, v_dic_arbres, v_num_colonne, v_num_ligne)



	return v_plateau
