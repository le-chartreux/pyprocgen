from .p_classes import cl_cond_biome, cl_sol_biome

# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer le dictionnaire v_dic_conditions_biomes
# et le dicionnaire v_dic_couleurs_biomes
# -----------------------------
# CONTENU :
# - f_ajout_biome(v_dic_biomes, v_le_biome)
# - f_creation_dic_conditions_biomes()
# - f_creation_dic_couleurs_biomes()
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# - p_image_creation.py
# =============================



###############################################################
######################### AJOUT_BIOME #########################
###############################################################
def f_ajout_biome(v_dic_biomes, v_le_biome):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute v_le_biome dans le dicionnaire v_dic_biomes avec
	# v_le_biome.nom_biome comme référence
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_biomes est un dictionnaire
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_cond_biome
	# - p_classes.cl_coul_biome
	# -----------------------------
	# UTILISE PAR :
	# - p_biomes_creation.f_creation_dic_conditions_biomes()
	# - p_biomes_creation.f_creation_dic_couleurs_biomes()
	# =============================

	v_dic_biomes[v_le_biome.nom_biome] = v_le_biome



###############################################################
############### CREATION_DIC_CONDITIONS_BIOMES ################
###############################################################
def f_creation_dic_conditions_biomes():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit v_dic_conditions_biomes de classes cl_cond_biome
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_biomes_creation.f_ajout_biome()
	# - p_classes.cl_cond_biome
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	v_dic_conditions_biomes = {}
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Desert_Cool", 0, 1, -4, -3))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Desert_Tropical", 2, 3, -4, -3))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Desert_Warm", 1, 2, -4, -3))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Desert_Scub_Cool", 0, 1, -3, -2))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Desert_Scub_Tropical", 2, 3, -3, -2))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Desert_Scub_Warm", 1, 2, -3, -2))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Dry_Forest_Tropical", 2, 3, 0, 1))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Dry_Forest_Warm", 1, 2, -1, 0))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Moist_Forest_Cool", 0, 1, -1, 0))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Moist_Forest_Tropical", 2, 3, 1, 2))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Moist_Forest_Warm", 1, 2, 0, 1))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Rain_Forest", 0, 1, 1, 2))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Rocks_and_ice", -3, -2, -4, -1))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Steppe", 0, 1, -2, -1))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Steppe_Woodland_Thorn", 1, 2, -2, -1))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Taiga_Desert", -1, 0, -4, -3))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Taiga_Dry", -1, 0, -3, -2))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Taiga_Moist", -1, 0, -2, -1))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Taiga_Rain", -1, 0, 0, 1))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Taiga_Wet", -1, 0, -1, 0))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Toundra_Dry", -2, -1, -4, -3))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Toundra_Moist", -2, -1, -3, -2))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Toundra_Rain", -2, -1, -1, 0))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Toundra_Wet", -2, -1, -2, -1))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Tropical_Forest_Tropical", 2, 3, 3, 4))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Tropical_Forest_Warm", 1, 2, 2, 3))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Very_Dry_Forest", 2, 3, -1, 0))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Wet_Forest_Cool", 0, 1, 0, 1))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Wet_Forest_Tropical", 2, 3, 2, 3))
	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Wet_Forest_Warm", 1, 2, 1, 2))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Woodland_Thorn", 2, 3, -2, -1))

	f_ajout_biome(v_dic_conditions_biomes, cl_cond_biome("Water", 0, 0, 0, 0))

	return v_dic_conditions_biomes



###############################################################
################ CREATION_DIC_COULEURS_BIOMES #################
###############################################################
def f_creation_dic_couleurs_biomes():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit v_dic_couleurs_biomes de classes cl_sol_biome
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_biomes_creation.f_ajout_biome()
	# - p_classes.cl_sol_biome
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	v_dic_couleurs_biomes = {}
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Desert_Cool", "193 165 133"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Desert_Tropical", "247 210 165"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Desert_Warm", "207 151 100"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Desert_Scub_Cool", "187 158 126"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Desert_Scub_Tropical", "251 224 181"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Desert_Scub_Warm", "193 161 122"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Dry_Forest_Tropical", "177 148 108"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Dry_Forest_Warm", "167 138 104"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Moist_Forest_Cool", "78 105 36"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Moist_Forest_Tropical", "93 84 51"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Moist_Forest_Warm", "86 104 56"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Rain_Forest", "89 93 66"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Rocks_and_ice", "190 220 255"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Steppe", "160 173 120"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Steppe_Woodland_Thorn", "160 173 120"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Taiga_Desert", "146 126 101"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Taiga_Dry", "167 175 120"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Taiga_Moist", "86 104 56"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Taiga_Rain", "57 102 21"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Taiga_Wet", "75 102 44"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Toundra_Dry", "167 175 120"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Toundra_Moist", "86 104 56"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Toundra_Rain", "57 102 21"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Toundra_Wet", "75 102 44"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Tropical_Forest_Tropical", "71 94 12"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Tropical_Forest_Warm", "94 124 16"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Very_Dry_Forest", "191 168 124"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Wet_Forest_Cool", "128 168 104"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Wet_Forest_Tropical", "128 168 104"))
	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Wet_Forest_Warm", "128 168 104"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Woodland_Thorn", "149 163 140"))

	f_ajout_biome(v_dic_couleurs_biomes, cl_sol_biome("Water", "0 0 255"))

	return v_dic_couleurs_biomes
