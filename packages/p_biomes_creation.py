from .p_classes import C_Biome

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer le dictionnaire Biomes
# -----------------------------
# CONTENU :
# - Ajout_Biome(Biomes, Biome)
# - Creation_Constantes_Biomes()
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - Procedural_generation_2D.py
# =============================



###############################################################
######################### AJOUT_BIOME #########################
###############################################################
def Ajout_Biome(Biomes, Biome):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute Biome dans le dicionnaire Biomes avec Biome.id comme
	# référence
	# -----------------------------
	# PRECONDITIONS :
	# - Biomes est un dictionnaire
	# -----------------------------
	# DEPEND DE :
	# - p_classes.C_Biome
	# -----------------------------
	# UTILISE PAR :
	# - p_biomes_creation.Creation_Constantes_Biomes()
	# =============================

	Biomes[Biome.id] = Biome



###############################################################
################# CREATION_CONSTANTES_BIOMES ##################
###############################################################
def Creation_Constantes_Biomes():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit Biomes de classes Biome
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_biomes_creation.Ajout_Biome()
	# - p_classes.C_Biome
	# -----------------------------
	# UTILISE PAR :
	# - Procedural_generation_2D.py
	# =============================

	Biomes = {}
	Ajout_Biome(Biomes, C_Biome("Desert_Cool", 0, 1, -4, -3))
	Ajout_Biome(Biomes, C_Biome("Desert_Tropical", 2, 3, -4, -3))
	Ajout_Biome(Biomes, C_Biome("Desert_Warm", 1, 2, -4, -3))

	Ajout_Biome(Biomes, C_Biome("Desert_Scub_Cool", 0, 1, -3, -2))
	Ajout_Biome(Biomes, C_Biome("Desert_Scub_Tropical", 2, 3, -3, -2))
	Ajout_Biome(Biomes, C_Biome("Desert_Scub_Warm", 1, 2, -3, -2))

	Ajout_Biome(Biomes, C_Biome("Dry_Forest_Tropical", 2, 3, 0, 1))
	Ajout_Biome(Biomes, C_Biome("Dry_Forest_Warm", 1, 2, -1, 0))

	Ajout_Biome(Biomes, C_Biome("Moist_Forest_Cool", 0, 1, -1, 0))
	Ajout_Biome(Biomes, C_Biome("Moist_Forest_Tropical", 2, 3, 1, 2))
	Ajout_Biome(Biomes, C_Biome("Moist_Forest_Warm", 1, 2, 0, 1))

	Ajout_Biome(Biomes, C_Biome("Rain_Forest", 0, 1, 1, 2))

	Ajout_Biome(Biomes, C_Biome("Rocks_and_ice", -3, -2, -4, -1))

	Ajout_Biome(Biomes, C_Biome("Steppe", 0, 1, -2, -1))

	Ajout_Biome(Biomes, C_Biome("Steppe_Woodland_Thorn", 1, 2, -2, -1))

	Ajout_Biome(Biomes, C_Biome("Taiga_Desert", -1, 0, -4, -3))
	Ajout_Biome(Biomes, C_Biome("Taiga_Dry", -1, 0, -3, -2))
	Ajout_Biome(Biomes, C_Biome("Taiga_Moist", -1, 0, -2, -1))
	Ajout_Biome(Biomes, C_Biome("Taiga_Rain", -1, 0, 0, 1))
	Ajout_Biome(Biomes, C_Biome("Taiga_Wet", -1, 0, -1, 0))

	Ajout_Biome(Biomes, C_Biome("Toundra_Dry", -2, -1, -4, -3))
	Ajout_Biome(Biomes, C_Biome("Toundra_Moist", -2, -1, -3, -2))
	Ajout_Biome(Biomes, C_Biome("Toundra_Rain", -2, -1, -1, 0))
	Ajout_Biome(Biomes, C_Biome("Toundra_Wet", -2, -1, -2, -1))

	Ajout_Biome(Biomes, C_Biome("Tropical_Forest_Tropical", 2, 3, 3, 4))
	Ajout_Biome(Biomes, C_Biome("Tropical_Forest_Warm", 1, 2, 2, 3))

	Ajout_Biome(Biomes, C_Biome("Very_Dry_Forest", 2, 3, -1, 0))

	Ajout_Biome(Biomes, C_Biome("Wet_Forest_Cool", 0, 1, 0, 1))
	Ajout_Biome(Biomes, C_Biome("Wet_Forest_Tropical", 2, 3, 2, 3))
	Ajout_Biome(Biomes, C_Biome("Wet_Forest_Warm", 1, 2, 1, 2))

	Ajout_Biome(Biomes, C_Biome("Woodland_Thorn", 2, 3, -2, -1))


	return Biomes
