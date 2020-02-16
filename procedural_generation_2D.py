import time
from packages.p_board_functions import f_generate_seed, f_create_empty_board, f_print_progression, f_display_board
from packages.p_decisional import f_genererate_box
from packages.p_dic_functions import f_dic_biomes_creation, f_hauteur_max_arbre, f_dic_trees_creation
from packages.p_image_creation import f_image_creation, f_image_header_creation
from packages.p_trees_generation import f_generate_trees

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.
v_dic_biomes = f_dic_biomes_creation()

v_dic_arbres = f_dic_trees_creation()
v_hauteur_max_arbre = f_hauteur_max_arbre(v_dic_arbres)

print(v_hauteur_max_arbre)

v_nbx=eval(input("x = "))
v_nby=eval(input("y = "))
t=time.time()
print("")

v_seed = f_generate_seed()

f_image_header_creation(v_nby,v_nbx, v_seed)

for v_num_chunk in range (int(v_nby / v_hauteur_max_arbre)) :

	v_chunk_suivant = f_create_empty_board(v_nbx, v_hauteur_max_arbre)

	for v_num_ligne in range(v_hauteur_max_arbre):

		for v_num_colonne in range (v_nbx) :

			v_chunk_suivant[v_num_ligne][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne , v_num_chunk * v_hauteur_max_arbre + v_num_ligne, v_seed)

	if v_num_chunk == 0:
		v_chunk_actuel = v_chunk_suivant

	v_chunk_fusion = v_chunk_actuel + v_chunk_suivant

	f_generate_trees(v_chunk_fusion)

	v_chunk_actuel = v_chunk_fusion[(v_hauteur_max_arbre):]

	f_image_creation(v_chunk_actuel)

	v_chunk_actuel = v_chunk_fusion[:(v_hauteur_max_arbre)]


	f_print_progression("Vectorial creation of the map :        ", ((v_num_chunk + 1) * v_hauteur_max_arbre) / v_nby)


print("")

print("Done")

print("Execution time : ",time.time()-t)

#f_display_board(v_plateau)
