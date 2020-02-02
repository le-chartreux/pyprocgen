import time
from packages.p_board_functions import f_generate_seed, f_create_empty_board
from packages.p_decisional import f_genererate_box
from packages.p_dic_creation import f_dic_biomes_creation
from packages.p_image_creation import f_image_creation
from packages.p_trees_generation import f_generate_trees

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.
v_dic_biomes = f_dic_biomes_creation()


v_nbx=eval(input("x = "))
v_nby=eval(input("y = "))
t=time.time()
print("")

v_seed = f_generate_seed()

v_plateau = f_create_empty_board(v_nbx, v_nby)


for v_num_ligne in range (v_nby) :

	for v_num_colonne in range (v_nbx) :

		v_plateau[v_num_ligne][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_ligne, v_seed)

	print("Vectorial creation of the map : ",round((v_num_ligne + 1)/len(v_plateau)*100,2),"%", end = "\r")

print("")

#f_display_board(v_plateau)

f_generate_trees(v_plateau)

f_image_creation(v_plateau, v_seed)

print("Done")

print("Execution time : ",time.time()-t)
