# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer un plateau vide, créer un seed et
# afficher un plateau dans la console
# -----------------------------
# CONTENU :
# - f_create_empty_board(co_nbx,co_nby)
# - f_display_board(v_plateau)
# - f_generate_seed()
# - f_print_progression(v_texte, v_progression)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py


###############################################################
#################### F_CREATE_EMPTY_BOARD #####################
###############################################################
def f_create_empty_board(v_nbx, v_nby):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Crée un plateau vide de x cases de largeur et y de longueur
	# -----------------------------
	# PRECONDITIONS :
	# - v_nbx, v_nby : integers
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_box
	# - p_board_functions.f_print_progression()
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	from .p_classes import cl_box

	v_plateau=[]

	for v_i in range(v_nby) :

		v_plateau.append([])

		for v_j in range(v_nbx) :

			v_plateau[v_i].append(None)

		f_print_progression("Creation of the empty board's vector : ", (v_i + 1) / v_nby)

	print("")

	return v_plateau


###############################################################
##################### F_GENERERATE_SEED #######################
###############################################################
def f_generate_seed():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Génère un dictionnaire de seed avec :
	# - Tx : seed de température axe x
	# - Ty : seed de température axe y
	# - Px : seed de pluviométrie axe x
	# - Py : seed de pluviométrie axe y
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - random
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	import random

	v_seed = {}
	v_seed["Tx"] = random.randint(-100000,100000)
	v_seed["Ty"] = random.randint(-100000,100000)
	v_seed["Px"] = random.randint(-100000,100000)
	v_seed["Py"] = random.randint(-100000,100000)

	print("Seed coordinates :")
	print("Temperature : x =",v_seed["Tx"],", y =",v_seed["Ty"])
	print("Pluviometry : x =",v_seed["Px"],", y =",v_seed["Py"])
	print("")

	return v_seed



###############################################################
##################### F_DISPLAY_BOARD #########################
###############################################################
def f_display_board(v_plateau):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Affiche un plateau de taille len(v_plateau[0]) * len(v_plateau)
	# dans la console
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_box
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py (pour debug)
	# =============================
	from .p_classes import cl_box

	for v_i in range(len(v_plateau)) :

		for v_j in range(len(v_plateau[0])) :

				print(v_plateau[v_i][v_j].nom_biome[0:4], " ", end="")

		print("")


def f_print_progression(v_texte, v_progression):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Affiche la progression (de 0 à 1)
	# dans la console, avec un # par tranche de 0.1
	# Forme : v_texte + "[####      ]" + (v_progression, en pourcent) + "%"
	# -----------------------------
	# PRECONDITIONS :
	# - v_progression : réel compris entre 0 et 1
	# -----------------------------
	# DEPEND DE :
	# - None
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# - p_board_functions.f_create_empty_board()
	# - p_image_creation.f_image_creation()
	# =============================

	v_progression10 = int(v_progression * 10)
	v_str_progression = ""

	for i in range(v_progression10):
		v_str_progression += "#"

	for i in range(10 - v_progression10):
		v_str_progression += " "

	print(v_texte +
		"[" + v_str_progression + "]",
		round(v_progression * 100, 2),"%",
		end="\r")
