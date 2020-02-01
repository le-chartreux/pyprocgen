from .p_classes import cl_case, cl_arbre
from packages.p_board_functions import *

def possible_to_place_tree(v_plateau, v_dic_arbres, v_x, v_y):
	# A modifier
	v_larg_arbre = 5
	v_haut_arbre = 5

	v_type_case_0_0 = "Desert_Cool"

	if v_x + v_haut_arbre > len(v_plateau):
		v_haut_arbre = len(v_plateau) - v_x

	if v_y + v_larg_arbre > len(v_plateau[0]):
		v_larg_arbre = len(v_plateau[0]) - v_y


	for v_num_ligne in range(v_haut_arbre):

		for v_num_colonne in range(v_larg_arbre):

			#print("x = ",v_x + v_num_ligne)
			print("y = ",v_y + v_num_colonne)

			if v_plateau[v_x + v_num_ligne][v_y + v_num_colonne].type != v_type_case_0_0:
				return False

	return True



#def placer_arbre(v_plateau, v_dic_arbres, v_x, v_y):





def generate_trees(v_plateau, v_dic_arbres, v_nbx, v_nby):

	for v_num_ligne in range(v_nby):
		for v_num_colonne in range(v_nbx):
			print(v_num_ligne, "x",v_num_colonne)
			print(possible_to_place_tree(v_plateau, v_dic_arbres, v_num_colonne, v_num_ligne))
			print("")

	return v_plateau
