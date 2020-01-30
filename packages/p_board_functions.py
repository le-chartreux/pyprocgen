from .p_classes import cl_case

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer un plateau vide et
# afficher un plateau dans la console
# -----------------------------
# CONTENU :
# - f_creer_plateau_vide(co_nbx,co_nby)
# - f_afficher_plateau(v_plateau)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py



###############################################################
#################### CREER_PLATEAU_VIDE #######################
###############################################################
def f_creer_plateau_vide(v_nbx, v_nby):
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
	# - p_classes.cl_case
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	v_plateau=[]
	for v_i in range(v_nby) :

		v_plateau.append([])
		for v_j in range(v_nbx) :

			v_plateau[v_i].append(cl_case(None, None, None))

		print("Creation of the empty board's vector : ",round((v_i + 1) / v_nby*100, 2), "%", end = "\r")

	print("")

	return v_plateau



###############################################################
#################### AFFICHER_PLATEAU #########################
###############################################################
def f_afficher_plateau(v_plateau):
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
	# - p_classes.cl_case
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	for v_i in range(len(v_plateau)) :

		for v_j in range(len(v_plateau[0])) :

				print(v_plateau[v_i][v_j].type, " ", end="")

		print("")
