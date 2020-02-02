# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer un plateau vide, créer un seed et
# afficher un plateau dans la console
# -----------------------------
# CONTENU :
# - f_creer_plateau_vide(co_nbx,co_nby)
# - f_afficher_plateau(v_plateau)
# - f_generer_seed()
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

		print("Creation of the empty board's vector : ",round((v_i + 1) / v_nby*100, 2), "%", end = "\r")

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
