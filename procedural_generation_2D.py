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
from packages.p_board_functions 	import f_generate_seed, f_create_empty_board, f_print_progression, f_seed_to_string, f_string_to_seed, f_is_it_a_seed, f_is_it_an_integer
from packages.p_decisional 			import f_genererate_box
from packages.p_dic_functions 		import f_dic_biomes_creation, f_max_height_of_trees
from packages.p_image_creation 		import f_create_image_header, f_create_image_body
from packages.p_trees_generation 	import f_generate_trees


###############################################################
################## CHOIX DE L UTILISATEUR #####################
###############################################################
print("Hello, welcome to this 2D procedural map generator. \n")


# ... de la taille de la map :
print("- Enter the map's size :")
print("  Tip : enter integers between 100 and 5000")

# Pour la largeur :
v_nbx = None
while not f_is_it_an_integer(v_nbx):

	if v_nbx != None:
		print("  Enter an integer.")

	v_nbx = input("  Lenght : ")

v_nbx = int(v_nbx)

# Pour la hauteur :
v_nby = None
while not f_is_it_an_integer(v_nby):

	if v_nby != None:
		print("  Enter an integer.")

	v_nby = input("  Height : ")

v_nby = int(v_nby)

print("")


# ... du mode d'utilisation
print("- Which mode do you want to use ?")
print("  1 : Basic")
print("  2 : Advanced")
v_mode = None
while v_mode != "1" and v_mode != "2":

	if v_mode != None:
		print("  Enter 1 or 2.")

	v_mode = input("  My choice : ")

print("")


###############################################################
######################## MODE BASIQUE #########################
###############################################################
if v_mode == "1":

	v_seed = f_generate_seed()
	v_intensite_variation = 1
	v_placer_arbres = True
	v_afficher_progression = True


###############################################################
######################## MODE AVANCE ##########################
###############################################################
elif v_mode == "2":

	# ... du seed
	v_choix = None
	while v_choix != "y" and v_choix != "n":

		if v_choix != None:
			print("Enter y or n.")

		v_choix = input("- Do you want to enter a seed ? (y / n) : ")

	if v_choix == "y":
		print("  Tip : a seed looks like a:b:c:d where a,b,c,d are integers")

		v_seed_in_string = ""
		while not f_is_it_a_seed(v_seed_in_string):

			if v_seed_in_string != "":
				print("  This is not a seed.")

			v_seed_in_string = input("  Enter the seed : ")

		v_seed = f_string_to_seed(v_seed_in_string)

	elif v_choix == "n":
		v_seed = f_generate_seed()

	print("")


	# ... de l'intensité de la variation
	v_choix = None
	while v_choix != "y" and v_choix != "n":

		if v_choix != None:
			print("Enter y or n.")

		v_choix = input("- Do you want to change the intensity of the variation between two boxes ? (y / n) : ")

	if v_choix == "y":
		print("Tip : enter a number between 0.1 and 10, 1 is the basic choice.")
		v_intensite_variation = float(input("My choice : "))

	elif v_choix == "n":
		v_intensite_variation = 1

	print("")


	# ... de la présence d'arbres
	v_choix = None
	while v_choix != "y" and v_choix != "n":

		if v_choix != None:
			print("Enter y or n.")

		v_choix = input("- Do you want trees on the map ? (y / n) : ")

	v_placer_arbres = (v_choix == "y")

	print("")


	# ... du support d'utilisation
	v_choix = None
	while v_choix != "y" and v_choix != "n":

		if v_choix != None:
			print("Enter y or n.")

		v_choix = input("- Do you run this program with IDLE ? (y / n)")

	v_afficher_progression = (v_choix == "n")

	print("")


###############################################################
######################### CONSTANTES ##########################
###############################################################
v_time = time.time()
print("Seed of the map : " + f_seed_to_string(v_seed) + "\n")
v_dic_biomes = f_dic_biomes_creation()

###############################################################
############### CREATION DU HEADER DE L IMAGE #################
###############################################################
fi_fichier_dest = open("Generated_map.ppm", "w")
f_create_image_header(fi_fichier_dest, v_nby, v_nbx, f_seed_to_string(v_seed))


###############################################################
############### CREATION DE L'IMAGE AVEC ARBRES ###############
###############################################################
if v_placer_arbres:

	v_hauteur_chunk = f_max_height_of_trees(v_dic_biomes)

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

		f_generate_trees(v_chunk_fusion, v_dic_biomes)

		v_chunk_actuel = v_chunk_fusion[:v_hauteur_chunk]

		f_create_image_body(fi_fichier_dest, v_chunk_actuel, v_dic_biomes)

		v_chunk_actuel = v_chunk_fusion[v_hauteur_chunk:]

		if v_afficher_progression:
			f_print_progression("Creation of the map :        ", ((v_num_chunk + 1) * v_hauteur_chunk) / v_nby)

		v_num_chunk -= 1


	# Création du dernier chunk
	v_chunk_dernier = v_chunk_actuel[0:(v_nby % v_hauteur_chunk)]

	f_create_image_body(fi_fichier_dest, v_chunk_dernier, v_dic_biomes)

	if v_afficher_progression:
		f_print_progression("Creation of the map :        ", 1.0)



###############################################################
############### CREATION DE L'IMAGE SANS ARBRES ###############
###############################################################
else:

	for v_num_ligne in range(v_nby):

		v_chunk = f_create_empty_board(v_nbx, 1)

		for v_num_colonne in range (v_nbx) :

			v_chunk[0][v_num_colonne] = f_genererate_box(v_dic_biomes, v_num_colonne, v_num_ligne, v_seed, v_intensite_variation)


		f_create_image_body(fi_fichier_dest, v_chunk, v_dic_biomes)

		if v_afficher_progression:
			f_print_progression("Creation of the map :        ", (v_num_ligne + 1) / v_nby)




###############################################################
################ AFFICHAGE DES MESSAGES DE FIN ################
###############################################################
fi_fichier_dest.close()
print("")
print("Done")
print("Execution time : ",time.time() - v_time)
