import time
t=time.time()

from packages.p_creation_biomes_dic import f_creation_dic_conditions_biomes, f_creation_dic_couleurs_biomes
from packages.p_board_functions import *
from packages.p_decisional import f_generer_case
from packages.p_image_creation import f_image_creation
from packages.p_trees_generation import f_generate_trees
# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.
v_dic_conditions_biomes = f_creation_dic_conditions_biomes()

v_dic_couleurs_biomes = f_creation_dic_couleurs_biomes()

v_nbx=eval(input("x = "))
v_nby=eval(input("y = "))
print("")

v_seed = f_generer_seed()

v_plateau = f_creer_plateau_vide(v_nbx,v_nby)

for v_num_colonne in range (v_nby) :

	for v_num_ligne in range (v_nbx) :

		v_plateau[v_num_colonne][v_num_ligne] = f_generer_case(v_dic_conditions_biomes, v_dic_couleurs_biomes, v_num_colonne, v_num_ligne, v_seed)

	print("Vectorial creation of the map : ",round((v_num_colonne + 1)/len(v_plateau)*100,2),"%", end = "\r")

print("")

#f_afficher_plateau(v_plateau)

f_generate_trees(v_plateau)

f_image_creation(v_plateau, v_seed)

print("Done")

print(time.time()-t)
