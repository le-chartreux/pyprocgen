import time
from packages.p_board_functions 	import f_generate_seed, f_create_empty_board, f_print_progression
from packages.p_decisional 			import f_genererate_box
from packages.p_dic_functions 		import f_dic_biomes_creation, f_hauteur_max_arbre, f_dic_trees_creation
from packages.p_image_creation 		import f_create_image_header, f_create_image_body
from packages.p_trees_generation 	import f_generate_trees

# =============================
# INFORMATIONS :
# -----------------------------
# UTILITE :
# Corps du programme de génération
# procédurale de carte en 2D
# -----------------------------
# PRECONDITIONS :
# - Le reste du programme fonctionne et existe
# -----------------------------
# DEPEND DE :
# - les packages appelés
# -----------------------------
# UTILISE PAR :
# - None
# =============================

v_nbx = eval(input("x = "))
v_nby = eval(input("y = "))
print("")

###############################################################
######################### CONSTANTES ##########################
###############################################################
v_dic_biomes = f_dic_biomes_creation()
v_dic_arbres = f_dic_trees_creation()
v_hauteur_max_arbre = f_hauteur_max_arbre(v_dic_arbres)
v_seed = f_generate_seed()
v_time=time.time()


###############################################################
#################### CREATION DE L'IMAGE ######################
###############################################################
fi_fichier_dest = open("Generated_map.ppm", "w")

f_create_image_header(fi_fichier_dest, v_nby, v_nbx, v_seed)


# Création du chunk initial
v_chunk_actuel = f_create_empty_board(v_nbx, v_hauteur_max_arbre)

for v_num_ligne in range(v_hauteur_max_arbre):

	for v_num_colonne in range (v_nbx) :

		v_chunk_actuel[v_num_ligne][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_ligne, v_seed)


# Création des chunks intermédiaires
for v_num_chunk in range (int(v_nby / v_hauteur_max_arbre)) :

	v_num_chunk += 1

	v_chunk_suivant = f_create_empty_board(v_nbx, v_hauteur_max_arbre)

	for v_num_ligne in range(v_hauteur_max_arbre):

		for v_num_colonne in range (v_nbx) :

			v_chunk_suivant[v_num_ligne][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_chunk * v_hauteur_max_arbre + v_num_ligne, v_seed)

	v_chunk_fusion = v_chunk_actuel + v_chunk_suivant

	f_generate_trees(v_chunk_fusion, v_dic_arbres)

	v_chunk_actuel = v_chunk_fusion[:v_hauteur_max_arbre]

	f_create_image_body(fi_fichier_dest, v_chunk_actuel)

	v_chunk_actuel = v_chunk_fusion[v_hauteur_max_arbre:]

	f_print_progression("Creation of the map :        ", ((v_num_chunk + 1) * v_hauteur_max_arbre) / v_nby)

	v_num_chunk -= 1


# Création du dernier chunk
v_chunk_dernier = v_chunk_actuel[0:(v_nby % v_hauteur_max_arbre)]

f_create_image_body(fi_fichier_dest, v_chunk_dernier)

f_print_progression("Creation of the map :        ", 1.0)

print("")

fi_fichier_dest.close()


###############################################################
################ AFFICHAGE DES MESSAGES DE FIN ################
###############################################################
print("Done")
print("Execution time : ",time.time() - v_time)
