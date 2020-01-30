# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - class cl_case
# - class cl_cond_biome
# - class cl_sol_biome
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - p_biomes_creation.py
# - p_board_creation.py
# - p_decisional.py
# - p_image_creation.py
# =============================



##############################################################
######################### CL_CASE ############################
##############################################################
class cl_case:

	def __init__(self, v_type, v_temp, v_pluv, v_coul):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définissant une case, caractérisée par :
		# - son type
		# - sa température moyenne
		# - sa pluviométrie annuelle
		# - sa couleur de forme "r g b"
		# -----------------------------
		# UTILISE PAR :
		# - p_board_functions.f_creer_plateau_vide()
		# - p_board_functions.f_afficher_plateau()
		# - p_decisional.f_choix_biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.type = v_type
		self.temp = v_temp
		self.pluv = v_pluv
		self.coul = v_coul


###############################################################
###################### CL_COND_BIOME ##########################
###############################################################
class cl_cond_biome:

	def __init__(self, v_nom, v_temp_min, v_temp_max, v_pluv_min, v_pluv_max):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant un biome, caractérisé par :
		# - son nom
		# - sa température moyenne minimale
		# - sa température moyenne maximale
		# - sa pluviometrie annuelle minimale
		# - sa pluviometrie annuelle maximale
		# -----------------------------
		# UTILISE PAR :
		# - p_biomes_creation.f_creation_dic_conditions_biomes()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom
		self.temp_min = v_temp_min
		self.temp_max = v_temp_max
		self.pluv_min = v_pluv_min
		self.pluv_max = v_pluv_max


	def in_range(self, v_temp, v_pluv):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Renvoit True si la temperature et la pluviométrie
		# correspondent à celles de ce biome
		# -----------------------------
		# UTILISE PAR :
		# - p_decisional.f_choix_biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - p_classes.cl_cond_biome.__init__()
		# =============================

		return self.temp_min <= v_temp <= self.temp_max and self.pluv_min <= v_pluv < self.pluv_max



##############################################################
###################### CL_SOL_BIOME ##########################
##############################################################
class cl_sol_biome:

	# CONSTRUCTION DE LA CLASSE #
	def __init__(self, v_nom_biome, v_coul_sol):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant le sol d'un biome,
		# caractérisée par :
		# - le nom du biome representé
		# - le string de sa couleur rgb de forme r g b
		# -----------------------------
		# UTILISE PAR :
		# - p_biomes_creation.f_creation_dic_couleurs_biomes()
		# - p_image_creation.f_image_creation(v_plateau, v_seed)
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome
		self.coul_sol = v_coul_sol



##############################################################
######################## CL_ARBRE ############################
##############################################################
class cl_arbre:
	def __init__(self, v_nom_biome, v_body):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant les arbres
		# caractérisés par :
		# - le nom du biome où ils poussent
		# - le body de sa représentation ppm
		# -----------------------------
		# UTILISE PAR :
		# - p_trees_generation.
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome
		self.body = v_body
