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

import time
from packages.p_board_functions 	import f_generate_seed, f_create_empty_board, f_print_progression
from packages.p_decisional 			import f_genererate_box
from packages.p_dic_functions 		import f_dic_biomes_creation, f_hauteur_max_arbre, f_dic_trees_creation
from packages.p_image_creation 		import f_create_image_header, f_create_image_body
from packages.p_trees_generation 	import f_generate_trees


print("Hello, welcome to this 2D procedural map generator.")


# Taille de la map
print("Enter the map's size :")
print("Tip : enter numbers between 100 and 5000")
v_nbx = eval(input("Lenght : "))
v_nby = eval(input("Height : "))
print("")


# Mode d'utilisation
v_mode = None
while v_mode != "1" and v_mode != "2":
	print("Which mode do you want to use ?")
	print("1 : Basic")
	print("2 : Advanced")
	v_mode = input("My choice : ")
	print("")


# Mode Basique
if v_mode == "1":
	v_seed = f_generate_seed()
	v_intensite_variation = 1
	v_placer_arbres = True


# Mode avancé
elif v_mode == "2":

	# Choix seed
	v_choix = None
	while v_choix != "y" and v_choix != "n":
		v_choix = input("Do you want to enter a seed ? (y / n) : ")

	if v_choix == "y":
		print("Not yet possible.")
		v_seed = f_generate_seed()

	elif v_choix == "n":
		v_seed = f_generate_seed()
	print("")


	# Choix intensité variation
	v_choix = None
	while v_choix != "y" and v_choix != "n":
		v_choix = input("Do you want to change the intensity of the variation between two boxes ? (y / n) : ")

	if v_choix == "y":
		print("Tip : enter a number between 0.1 and 10, 1 is the basic choice.")
		v_intensite_variation = float(input("My choice : "))

	elif v_choix == "n":
		v_intensite_variation = 1
	print("")


	# Choix création des arbres
	v_choix = None
	while v_choix != "y" and v_choix != "n":
		v_choix = input("Do you want trees on the map ? (y / n) : ")

	v_placer_arbres = (v_choix == "y")


###############################################################
######################### CONSTANTES ##########################
###############################################################
v_dic_biomes = f_dic_biomes_creation()
v_dic_arbres = f_dic_trees_creation()
v_time = time.time()


###############################################################
############### CREATION DU HEADER DE L IMAGE #################
###############################################################
fi_fichier_dest = open("Generated_map.ppm", "w")
f_create_image_header(fi_fichier_dest, v_nby, v_nbx, v_seed)


###############################################################
############### CREATION DE L'IMAGE AVEC ARBRES ###############
###############################################################
if v_placer_arbres:

	v_hauteur_chunk = f_hauteur_max_arbre(v_dic_arbres)

	# Création du chunk initial
	v_chunk_actuel = f_create_empty_board(v_nbx, v_hauteur_chunk)

	for v_num_ligne in range(v_hauteur_chunk):

		for v_num_colonne in range (v_nbx) :

			v_chunk_actuel[v_num_ligne][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_ligne, v_seed, v_intensite_variation)


	# Création des chunks intermédiaires
	for v_num_chunk in range (int(v_nby / v_hauteur_chunk)) :

		v_num_chunk += 1

		v_chunk_suivant = f_create_empty_board(v_nbx, v_hauteur_chunk)

		for v_num_ligne in range(v_hauteur_chunk):

			for v_num_colonne in range (v_nbx) :

				v_chunk_suivant[v_num_ligne][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_chunk * v_hauteur_chunk + v_num_ligne, v_seed, v_intensite_variation)

		v_chunk_fusion = v_chunk_actuel + v_chunk_suivant

		f_generate_trees(v_chunk_fusion, v_dic_arbres)

		v_chunk_actuel = v_chunk_fusion[:v_hauteur_chunk]

		f_create_image_body(fi_fichier_dest, v_chunk_actuel)

		v_chunk_actuel = v_chunk_fusion[v_hauteur_chunk:]

		f_print_progression("Creation of the map :        ", ((v_num_chunk + 1) * v_hauteur_chunk) / v_nby)

		v_num_chunk -= 1


	# Création du dernier chunk
	v_chunk_dernier = v_chunk_actuel[0:(v_nby % v_hauteur_chunk)]

	f_create_image_body(fi_fichier_dest, v_chunk_dernier)

	f_print_progression("Creation of the map :        ", 1.0)

	print("")

	fi_fichier_dest.close()


###############################################################
############### CREATION DE L'IMAGE SANS ARBRES ###############
###############################################################
else:

	for v_num_ligne in range(v_nby):

		v_chunk = f_create_empty_board(v_nbx, 1)

		for v_num_colonne in range (v_nbx) :

			v_chunk[0][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_ligne, v_seed, v_intensite_variation)


		f_create_image_body(fi_fichier_dest, v_chunk)

		f_print_progression("Creation of the map :        ", (v_num_ligne + 1) / v_nby)




###############################################################
################ AFFICHAGE DES MESSAGES DE FIN ################
###############################################################
print("Done")
print("Execution time : ",time.time() - v_time)
