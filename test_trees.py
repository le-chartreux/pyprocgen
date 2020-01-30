from packages.p_creation_biomes_dic import f_creation_dic_conditions_biomes
from packages.p_board_functions import *
from packages.p_image_creation import f_image_creation
from packages.p_classes import cl_case
from packages.p_trees_generation import generate_trees
from packages.p_trees_dic_creation import f_creation_dic_arbres


# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.
v_dic_conditions_biomes = f_creation_dic_conditions_biomes()

v_nbx=30
v_nby=30

v_dic_arbres = f_creation_dic_arbres()

v_plateau = f_creer_plateau_vide(v_nbx,v_nby)

for v_num_colonne in range (v_nby) :

	for v_num_ligne in range (v_nbx) :

		v_plateau[v_num_colonne][v_num_ligne] = cl_case("Desert_Cool", 0, 0, "193 165 133")

generate_trees(v_plateau, v_dic_arbres, v_nbx, v_nby)

f_afficher_plateau(v_plateau)
