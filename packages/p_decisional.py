import random
from .p_classes import cl_case
from .p_perlin_noise import SimplexNoise
cl_noise = SimplexNoise()

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Gèrer l'évolution du terrain et
# prendre la décisison du type de case à placer en (x,y)
# -----------------------------
# CONTENU :
# - f_generer_case(Biomes, x, y, Seed)
# - f_choix_biome(Biomes, Temp, PlAn)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

###############################################################
###################### GENERER_CASE ###########################
###############################################################
def f_generer_case(Biomes, x, y, Seed):
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
	# - f_choix_biome()
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	Temp = cl_noise.noise2(Seed["Tx"] + x/500, Seed["Ty"] + y/500) * 3
	PlAn = cl_noise.noise2(Seed["Px"] + x/500, Seed["Py"] + y/500) * 4
	return f_choix_biome(Biomes, Temp, PlAn)



###############################################################
######################### CHOIX_BIOME #########################
###############################################################

def f_choix_biome(Biomes, Temp, PlAn):
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
		# - p_classes.cl_case
		# -----------------------------
		# UTILISE PAR :
		# - f_generer_case.(Biomes, x, y, Seed)
		# =============================
	for Biome in Biomes.values():
		if Biome.in_range(Temp, PlAn):
			return cl_case(Biome.id, Temp, PlAn)

	return cl_case("Water", Temp, PlAn)
