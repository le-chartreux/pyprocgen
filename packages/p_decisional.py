# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Gèrer l'évolution du terrain et
# prendre la décisison du tv_ype de case à placer en (v_x,v_y)
# -----------------------------
# CONTENU :
# - f_genererate_box(v_dic_biomes, v_x, v_y, v_seed)
# - f_choice_biome(v_dic_biomes, v_temp, v_pluv)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

###############################################################
###################### F_GENERATE_BOX #########################
###############################################################
def f_genererate_box(v_dic_biomes, v_x, v_y, v_seed):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Génère une case en pour la case en (v_y, v_x)
	# -----------------------------
	# PRECONDITIONS :
	# - v_x, v_y : integers not null
	# - v_seed["Tx"], v_seed["Ty"] : integers not null
	# - v_seed["Py"], v_seed["Py"] : integers not null
	# -----------------------------
	# DEPEND DE :
	# - p_perlin_noise.py
	# - f_choice_biome()
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================
	from .p_perlin_noise import SimplexNoise
	cl_noise = SimplexNoise()

	v_temp = (
			cl_noise.noise2(v_seed["T1x"] + v_x/1000, v_seed["T1y"] + v_y/1000) * 10
			+ cl_noise.noise2(v_seed["T2x"] + v_x/100, v_seed["T2y"] + v_y/100) * 3
			+ cl_noise.noise2(v_seed["T3x"] + v_x/10, v_seed["T3y"] + v_y/10)
	 	) * 3 / 14

	v_pluv = (
			cl_noise.noise2(v_seed["P1x"] + v_x/1000, v_seed["P1y"] + v_y/1000) * 10
			+ cl_noise.noise2(v_seed["P2x"] + v_x/100, v_seed["P2y"] + v_y/100) * 3
			+ cl_noise.noise2(v_seed["P3x"] + v_x/10, v_seed["P3y"] + v_y/10)
		) * 4 / 14

	return f_choice_biome(v_dic_biomes, v_temp, v_pluv)



###############################################################
######################## F_CHOICE_BIOME #######################
###############################################################

def f_choice_biome(v_dic_biomes, v_temp, v_pluv):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Renvoit l'id du biome qui a les caracteristiques
	# v_temp et v_pluv correspondantes.
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_biomes : dicionnaire not null
	# - v_temp : integer not null
	# - v_pluv : integer not null
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_box
	# -----------------------------
	# UTILISE PAR :
	# - p_decisional.f_genererate_box(v_dic_biomes, v_x, v_y, v_seed)
	# =============================
	from .p_classes import cl_box

	for v_biome in v_dic_biomes.values():

		if v_biome.m_in_range(v_temp, v_pluv):

			return cl_box(v_biome.nom_biome, v_temp, v_pluv, v_biome.coul)

	return cl_box("Water", v_temp, v_pluv, v_dic_biomes["Water"].coul)
