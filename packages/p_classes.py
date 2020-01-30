# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - class cl_case
# - class cl_biome
# - class cl_image
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

	def __init__(self, v_type, v_temp, v_pluv):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définissant une case, caractérisée par :
		# - son type
		# - sa température moyenne
		# - sa pluviométrie annuelle
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



###############################################################
######################### CL_BIOME ############################
###############################################################
class cl_biome:

	def __init__(self, v_id, v_temp_min, v_temp_max, v_pluv_min, v_pluv_max):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant un biome, caractérisé par :
		# - son identifiant
		# - sa température moyenne minimale
		# - sa température moyenne maximale
		# - sa pluviometrie annuelle minimale
		# - sa pluviometrie annuelle maximale
		# -----------------------------
		# UTILISE PAR :
		# - p_biomes_creation.f_creation_constantes_biomes()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.id = v_id
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
		# - p_classes.cl_biome.__init__()
		# =============================

		return self.temp_min <= v_temp <= self.temp_max and self.pluv_min <= v_pluv < self.pluv_max



##############################################################
######################## CL_IMAGE ############################
##############################################################
class cl_image:

	# CONSTRUCTION DE LA CLASSE #
	def __init__(self, v_nom_biome, v_body):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant une image, caractérisée par :
		# - le nom du biome qu'elle represente
		# - le vecteur de son body
		# -----------------------------
		# UTILISE PAR :
		# - p_image_creation.f_ajout_image()
		# - p_image_creation.f_image_creation()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome
		self.body = v_body
