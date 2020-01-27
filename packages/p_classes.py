# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - class C_Case
# - class C_Biome
# - class C_Image
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - p_biomes_creation.py
# - p_board_creation.py
# - p_decisional.py
# - p_image_creation.py
# =============================



##############################################################
########################## C_CASE ############################
##############################################################
class C_Case:

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
		# - p_board_functions.Creer_Plateau_Vide()
		# - p_board_functions.Afficher_Plateau()
		# - p_decisional.Choix_Biome()
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
########################## C_BIOME ############################
###############################################################
class C_Biome:

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
		# - p_biomes_creation.Creation_Constantes_Biomes()
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
		# - p_decisional.Choix_Biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - p_classes.C_Biome.__init__()
		# =============================

		return self.TempMin <= Temp <= self.TempMax and self.PlAnMin <= PlAn < self.PlAnMax



##############################################################
######################### C_IMAGE ############################
##############################################################
class C_Image:

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
		# - p_image_creation.Ajout_Image()
		# - p_image_creation.Image_creation()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.NomBiome = NomBiome
		self.Str = Str
