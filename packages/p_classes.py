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

	def __init__(self, type, Temp, PlAn):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définissant une case, caractérisée par :
		# - son type
		# - sa Température
		# - sa Pluviometrie Annuelle
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

		self.type = type
		self.Temp = Temp
		self.PlAn = PlAn



###############################################################
######################### CL_BIOME ############################
###############################################################
class cl_biome:

	def __init__(self, id, TempMin,TempMax, PlAnMin, PlAnMax):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant un biome, caractérisé par :
		# - son identifiant
		# - sa Température Minimale
		# - sa Température Maximale
		# - sa Pluviometrie Annuelle Minimale
		# - sa Pluviometrie Annuelle Maximale
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

		self.id = id
		self.TempMin = TempMin
		self.TempMax = TempMax
		self.PlAnMin = PlAnMin
		self.PlAnMax = PlAnMax


	def in_range(self, Temp, PlAn):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Renvoit True si la Temperature et les PlAn correspondent
		# à celles de ce biome
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

		return self.TempMin <= Temp <= self.TempMax and self.PlAnMin <= PlAn < self.PlAnMax



##############################################################
######################## CL_IMAGE ############################
##############################################################
class cl_image:

	# CONSTRUCTION DE LA CLASSE #
	def __init__(self, NomBiome, Str):
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

		self.NomBiome = NomBiome
		self.Str = Str
