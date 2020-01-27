from .p_classes import C_Case

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer un plateau vide et
# afficher un plateau dans la console
# -----------------------------
# CONTENU :
# - Creer_Plateau_Vide(nbx,nby)
# - Afficher_Plateau(Plateau)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - Procedural_generation_2D.py



###############################################################
#################### CREER_PLATEAU_VIDE #######################
###############################################################
def Creer_Plateau_Vide(nbx, nby):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Crée un plateau vide de x cases de largeur et y de longueur
	# -----------------------------
	# PRECONDITIONS :
	# - nbx,nby : integer
	# -----------------------------
	# DEPEND DE :
	# - p_classes.C_Case
	# -----------------------------
	# UTILISE PAR :
	# - Procedural_generation_2D.py
	# =============================

	Plateau=[]
	for i in range(nby) :

		Plateau.append([])
		for j in range(nbx) :

			Plateau[i].append(C_Case(None, None, None))

		print("Creation of the empty board's vector : ",round((i + 1) / nby*100, 2), "%", end = "\r")

	print("")

	return Plateau



###############################################################
#################### AFFICHER_PLATEAU #########################
###############################################################
def Afficher_Plateau(Plateau):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Affiche un plateau de taille len(Plateau[0]) x len(Plateau)
	# dans la console
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_classes.C_Case
	# -----------------------------
	# UTILISE PAR :
	# - Procedural_generation_2D.py
	# =============================

	for i in range(len(Plateau)) :

		for j in range(len(Plateau[0])) :

				print(Plateau[i][j].type, " ", end="")

		print("")
