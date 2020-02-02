import random
from .p_classes import cl_case
from .p_perlin_noise import SimplexNoise
cl_noise = SimplexNoise()

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Gèrer l'évolution du terrain et
# prendre la décisison du tv_ype de case à placer en (v_x,v_y)
# -----------------------------
# CONTENU :
# - f_generer_case(v_dic_conditions_biomes, v_x, v_y, v_seed)
# - f_choiv_x_biome(v_dic_conditions_biomes, v_temp, v_pluv)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

###############################################################
###################### GENERER_CASE ###########################
###############################################################
def f_generer_case(v_dic_conditions_biomes, v_dic_couleurs_biomes, v_x, v_y, v_seed):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Génère une case en (v_x,v_y)
	# -----------------------------
	# PRECONDITIONS :
	# - v_x,v_y : integers not null
	# - v_seed["Tx"], v_seed["Ty"] : integers not null
	# - v_seed["Py"], v_seed["Py"] : integers not null
	# -----------------------------
	# DEPEND DE :
	# - p_perlin_noise.pv_y
	# - f_choix_biome()
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.pv_y
	# =============================

	v_temp = cl_noise.noise2(v_seed["Tx"] + v_x/500, v_seed["Ty"] + v_y/500) * 3
	v_pluv = cl_noise.noise2(v_seed["Px"] + v_x/300, v_seed["Py"] + v_y/300) * 4
	return f_choix_biome(v_dic_conditions_biomes, v_dic_couleurs_biomes, v_temp, v_pluv)



###############################################################
######################### CHOIX_BIOME #########################
###############################################################

def f_choix_biome(v_dic_conditions_biomes, v_dic_couleurs_biomes, v_temp, v_pluv):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Renvoit l'id du Biome qui a les caracteristiques
		# v_temperature et v_pluv correspondantes.
		# -----------------------------
		# PRECONDITIONS :
		# - v_dic_conditions_biomes : dicionnaire not null
		# - v_temp : integer not null
		# - v_pluv : integer not null
		# -----------------------------
		# DEPEND DE :
		# - p_classes.cl_case
		# -----------------------------
		# UTILISE PAR :
		# - f_generer_case.(v_dic_conditions_biomes, v_x, v_y, v_seed)
		# =============================
	for v_biome in v_dic_conditions_biomes.values():
		if v_biome.in_range(v_temp, v_pluv):
			v_couleur = v_dic_couleurs_biomes[v_biome.nom_biome].coul
			return cl_case(v_biome.nom_biome, v_temp, v_pluv, v_couleur)

	return cl_case("Water", v_temp, v_pluv, v_dic_couleurs_biomes["Water"].coul)
