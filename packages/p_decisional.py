import random
from .p_classes import C_Case
from .p_perlin_noise import SimplexNoise
noise = SimplexNoise()

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Gèrer l'évolution du terrain et
# prendre la décisison du type de case à placer en (x,y)
# -----------------------------
# CONTENU :
# - Placer_Case(Biomes, x, y, Seed)
# - Temp_xy(x, y)
# - PlAn_xy(x, y)
# - Choix_Biome(Biomes, Temp, PlAn)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - Procedural_generation_2D.py
# =============================

###############################################################
###################### GENERER_CASE ###########################
###############################################################
def Generer_Case(Biomes, x, y, Seed):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Génère une case en (x,y)
	# -----------------------------
	# PRECONDITIONS :
	# - x,y : integers not null
	# - Seed["Tx"], Seed["Ty"] : integers not null
	# - Seed["Px"], Seed["Py"] : integers not null
	# -----------------------------
	# DEPEND DE :
	# - p_perlin_noise.py
	# - Choix_Biome()
	# -----------------------------
	# UTILISE PAR :
	# - Procedural_generation_2D.py
	# =============================

	Temp = noise.noise2(Seed["Tx"] + x/500, Seed["Ty"] + y/500) * 3
	PlAn = noise.noise2(Seed["Px"] + x/500, Seed["Py"] + y/500) * 4
	return Choix_Biome(Biomes, Temp, PlAn)



###############################################################
######################### CHOIX_BIOME #########################
###############################################################

def Choix_Biome(Biomes, Temp, PlAn):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Renvoit l'id du Biome qui a les caracteristiques
		# Temperature et PlAn correspondantes.
		# -----------------------------
		# PRECONDITIONS :
		# - Biomes : dicionnaire not null
		# - Temp : integer not null
		# - PlAn : integer not null
		# -----------------------------
		# DEPEND DE :
		# - p_classes.C_Case
		# -----------------------------
		# UTILISE PAR :
		# - Procedural_generation_2D.py
		# =============================
	for Biome in Biomes.values():
		if Biome.in_range(Temp, PlAn):
			return C_Case(Biome.id, Temp, PlAn)

	return C_Case("Eau", Temp, PlAn)
