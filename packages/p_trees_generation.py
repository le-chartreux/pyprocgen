from .p_classes import cl_case, cl_arbre

def possible_to_place_tree(v_plateau, v_dic_arbres, v_x, v_y):
	v_type_biome_case = v_plateau[v_x][v_y].type
	v_possible = True

	v_diam_x = len(v_dic_arbres[v_type_biome_case].body[0])
	v_diam_y = len(v_dic_arbres[v_type_biome_case].body)

	if v_x + v_diam_x > len(v_plateau[0]) - 1  :
		v_diam_x = (len(v_plateau[0]) - 1) - v_x

	elif v_y + v_diam_y > len(v_plateau) - 1 :
		v_diam_x = (len(v_plateau) - 1) - v_y

	for v_num_colonne in range (v_diam_y) :

		for v_num_ligne in range (v_diam_x) :

			if v_type_biome_case != v_plateau[v_num_ligne][v_num_colonne].type :
				return False

	return True

def placer_arbre(v_plateau, v_dic_arbres, v_x, v_y):
	v_type_biome_case = v_plateau[v_x][v_y].type

	v_diam_x = len(v_dic_arbres[v_type_biome_case].body[0])
	v_diam_y = len(v_dic_arbres[v_type_biome_case].body)


	if v_x + v_diam_x > len(v_plateau[0]) - 1  :
		v_diam_x = (len(v_plateau[0]) - 1) - v_x



	elif v_y + v_diam_y > len(v_plateau) - 1 :
		v_diam_x = (len(v_plateau) - 1) - v_y


	for v_num_ligne in range (v_diam_x) :

		for v_num_colonne in range (v_diam_y) :

			#print(v_num_ligne)
			#print(v_num_colonne)


			if v_dic_arbres[v_type_biome_case].body[v_num_ligne][v_num_colonne] != "0 0 0" :
				print("placé")
				v_plateau[v_x + v_num_ligne][v_y + v_num_colonne] = cl_case("Arbre", 0, 0, v_dic_arbres[v_type_biome_case].body[v_num_ligne][v_num_colonne])




def generate_trees(v_plateau, v_dic_arbres, v_nbx, v_nby):
	v_num_ligne = 0
	v_num_colonne = 0

	for v_num_ligne in range (v_nbx) :

		for v_num_colonne in range (v_nby) :


			try:
				if possible_to_place_tree(v_plateau, v_dic_arbres, v_num_ligne, v_num_colonne):

					placer_arbre(v_plateau, v_dic_arbres, v_num_ligne, v_num_colonne)

			except:
				print("Error")



	return v_plateau
