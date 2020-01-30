from .p_classes import cl_arbre

###############################################################
######################### AJOUT_BIOME #########################
###############################################################
def f_ajout_arbre(v_dic_arbres, v_l_arbre):
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Ajoute v_l_arbre dans le dicionnaire v_dic_arbres avec
	# v_l_arbre.nom_biome comme référence
	# -----------------------------
	# PRECONDITIONS :
	# - v_dic_arbres est un dictionnaire
	# -----------------------------
	# DEPEND DE :
	# - p_classes.cl_arbre
	# -----------------------------
	# UTILISE PAR :
	# - p_trees_dic_creation.f_creation_dic_arbres
	# =============================

	v_dic_arbres[v_l_arbre.nom_biome] = v_l_arbre

###############################################################
################### F_CREATION_DIC_ARBRES #####################
###############################################################

def f_creation_dic_arbres():
	# =============================
	# INFORMATIONS :
	# -----------------------------
	# UTILITE :
	# Remplit v_dic_arbres de classes cl_arbre
	# -----------------------------
	# PRECONDITIONS :
	# - NONE
	# -----------------------------
	# DEPEND DE :
	# - p_trees_dic_create.f_ajout_arbre(v_dic_arbres, v_l_arbre)
	# - p_classes.cl_arbre
	# -----------------------------
	# UTILISE PAR :
	# - procedural_generation_2D.py
	# =============================

	v_dic_arbres = {}
	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Cool", [
			["0 0 0", "106 82 18", "0 0 0", "0 0 0", "106 82 18"],
			["106 82 18", "142 93 60", "0 0 0", "127 85 63", "0 0 0"],
			["0 0 0", "0 0 0", "142 93 60", "142 93 60", "106 82 18"],
			["0 0 0", "106 82 18", "142 93 60", "0 0 0", "0 0 0"],
			["0 0 0", "0 0 0", "142 93 60", "0 0 0", "0 0 0"]
		]))

	"""
	f_ajout_biome(v_dic_arbres, cl_arbre("Desert_Tropical", "247 210 165"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Desert_Warm", "207 151 100"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Desert_Scub_Cool", "187 158 126"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Desert_Scub_Tropical", "251 224 181"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Desert_Scub_Warm", "193 161 122"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Dry_Forest_Tropical", "177 148 108"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Dry_Forest_Warm", "167 138 104"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Moist_Forest_Cool", "78 105 36"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Moist_Forest_Tropical", "93 84 51"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Moist_Forest_Warm", "86 104 56"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Rain_Forest", "89 93 66"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Rocks_and_ice", "190 220 255"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Steppe", "160 173 120"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Steppe_Woodland_Thorn", "160 173 120"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Taiga_Desert", "146 126 101"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Taiga_Dry", "167 175 120"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Taiga_Moist", "86 104 56"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Taiga_Rain", "57 102 21"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Taiga_Wet", "75 102 44"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Toundra_Dry", "167 175 120"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Toundra_Moist", "86 104 56"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Toundra_Rain", "57 102 21"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Toundra_Wet", "75 102 44"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Tropical_Forest_Tropical", "71 94 12"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Tropical_Forest_Warm", "94 124 16"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Very_Dry_Forest", "191 168 124"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Wet_Forest_Cool", "128 168 104"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Wet_Forest_Tropical", "128 168 104"))
	f_ajout_biome(v_dic_arbres, cl_arbre("Wet_Forest_Warm", "128 168 104"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Woodland_Thorn", "149 163 140"))

	f_ajout_biome(v_dic_arbres, cl_arbre("Water", "0 0 255"))
	"""

	return v_dic_arbres
