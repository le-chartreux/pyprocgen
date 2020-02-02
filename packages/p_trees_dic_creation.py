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
	# - packages.p_trees_generation()
	# =============================

	v_dic_arbres = {}

	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Cool", [
			[None, "106 82 18",  None,  None, "106 82 18"],
			["106 82 18", "142 93 60",  None, "127 85 63",  None],
			[ None,  None, "142 93 60", "142 93 60", "106 82 18"],
			[ None, "106 82 18", "142 93 60",  None,  None],
			[ None,  None, "142 93 60",  None,  None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Tropical", [
			[None, "106 82 18",  None,  None, "106 82 18"],
			["106 82 18", "142 93 60",  None, "127 85 63",  None],
			[ None,  None, "142 93 60", "142 93 60", "106 82 18"],
			[ None, "106 82 18", "142 93 60",  None,  None],
			[ None,  None, "142 93 60",  None,  None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Warm", [
			[None, "106 82 18",  None,  None, "106 82 18"],
			["106 82 18", "142 93 60",  None, "127 85 63",  None],
			[ None,  None, "142 93 60", "142 93 60", "106 82 18"],
			[ None, "106 82 18", "142 93 60",  None,  None],
			[ None,  None, "142 93 60",  None,  None]
		]))


	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Scub_Cool", [
			["156 152 107", "156 152 107", None],
			["156 152 107", "118 115 98", "156 152 107"],
			[None, "118 115 98", None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Scub_Tropical", [
			["156 152 107", "156 152 107", None],
			["156 152 107", "118 115 98", "156 152 107"],
			[None, "118 115 98", None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Desert_Scub_Warm", [
			["156 152 107", "156 152 107", None],
			["156 152 107", "118 115 98", "156 152 107"],
			[None, "118 115 98", None]
		]))


	f_ajout_arbre(v_dic_arbres, cl_arbre("Dry_Forest_Tropical", [
			[None, None, "121 105 56", None, None, None, None],
			[None, None, None, "133 103 69", None, "133 103 69", "121 105 56"],
			["121 105 56", "133 103 69", "133 103 69", "133 103 69", "133 103 69", None, None],
			[None, "121 105 56", None, "133 103 69", None, None, None],
			[None, None, None, "133 103 69", None, None, None],
			[None, None, None, "133 103 69", None, None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Dry_Forest_Warm", [
			[None, None, "121 105 56", None, None, None, None],
			[None, None, None, "133 103 69", None, "133 103 69", "121 105 56"],
			["121 105 56", "133 103 69", "133 103 69", "133 103 69", "133 103 69", None, None],
			[None, "121 105 56", None, "133 103 69", None, None, None],
			[None, None, None, "133 103 69", None, None, None],
			[None, None, None, "133 103 69", None, None, None]
		]))


	f_ajout_arbre(v_dic_arbres, cl_arbre("Moist_Forest_Cool", [
			[None, "54 62 15", "34 46 10", "34 46 10", None],
			["65 71 23", "34 46 10", "34 46 10", "34 46 10", None],
			["34 46 10", "34 46 10", "58 45 26", "34 46 10", "34 46 10"],
			[None, None, "58 45 26", None, None],
			[None, None, "58 45 26", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Moist_Forest_Tropical", [
			[None, "54 62 15", "34 46 10", "34 46 10", None],
			["65 71 23", "34 46 10", "34 46 10", "34 46 10", None],
			["34 46 10", "34 46 10", "58 45 26", "34 46 10", "34 46 10"],
			[None, None, "58 45 26", None, None],
			[None, None, "58 45 26", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Moist_Forest_Warm", [
			[None, "54 62 15", "34 46 10", "34 46 10", None],
			["65 71 23", "34 46 10", "34 46 10", "34 46 10", None],
			["34 46 10", "34 46 10", "58 45 26", "34 46 10", "34 46 10"],
			[None, None, "58 45 26", None, None],
			[None, None, "58 45 26", None, None]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Rain_Forest", [
			[None, "68 88 39", "68 88 39", "68 88 39", None],
			["68 88 39", "68 88 39", "68 88 39", "68 88 39", "68 88 39"],
			[None, "68 88 39", "88 107 55", "68 88 39", "68 88 39"],
			[None, None, "111 129 74", "68 88 39", None],
			[None, None, "116 133 78", None, None],
			[None, None, "116 133 78", None, None],
			[None, None, "116 133 78", None, None],
			[None, None, "116 133 78", None, None],
			[None, None, "114 131 77", None, None]
		]))


	f_ajout_arbre(v_dic_arbres, cl_arbre("Steppe_Woodland_Thorn", [
			[None, "34 58 26", None],
			["34 58 26", "34 58 26", "34 58 26"],
			["34 58 26", "34 58 26", "34 58 26"],
			[None, "88 73 50", None]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Taiga_Desert", [
			[None, None, "34 58 26", None, None],
			[None, None, "34 58 26", None, None],
			[None, "34 58 26", "34 58 26", "34 58 26", None],
			["34 58 26", "34 58 26", "88 73 50", "34 58 26", "34 58 26"],
			[None, None, "88 73 50", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Taiga_Dry", [
			[None, None, "34 58 26", None, None],
			[None, None, "34 58 26", None, None],
			[None, "34 58 26", "34 58 26", "34 58 26", None],
			["34 58 26", "34 58 26", "88 73 50", "34 58 26", "34 58 26"],
			[None, None, "88 73 50", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Taiga_Moist", [
			[None, None, "34 58 26", None, None],
			[None, None, "34 58 26", None, None],
			[None, "34 58 26", "34 58 26", "34 58 26", None],
			["34 58 26", "34 58 26", "88 73 50", "34 58 26", "34 58 26"],
			[None, None, "88 73 50", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Taiga_Rain", [
			[None, None, "34 58 26", None, None],
			[None, None, "34 58 26", None, None],
			[None, "34 58 26", "34 58 26", "34 58 26", None],
			["34 58 26", "34 58 26", "88 73 50", "34 58 26", "34 58 26"],
			[None, None, "88 73 50", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Taiga_Wet", [
			[None, None, "34 58 26", None, None],
			[None, None, "34 58 26", None, None],
			[None, "34 58 26", "34 58 26", "34 58 26", None],
			["34 58 26", "34 58 26", "88 73 50", "34 58 26", "34 58 26"],
			[None, None, "88 73 50", None, None]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Toundra_Rain", [
			["34 58 26", "34 58 26"]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Toundra_Wet", [
			["34 58 26", "34 58 26"]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Tropical_Forest_Tropical", [
			[None, "0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41", None],
			["0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41"],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", "88 73 50", None, None],
			[None, None, None, None, "88 73 50", None, None],
			[None, None, None, None, "88 73 50", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Tropical_Forest_Warm", [
			[None, "0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41", None],
			["0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41", "0 69 41"],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", None, None, None],
			[None, None, None, "88 73 50", "88 73 50", None, None],
			[None, None, None, None, "88 73 50", None, None],
			[None, None, None, None, "88 73 50", None, None]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Very_Dry_Forest", [
			[None, None, "121 105 56", None, None, None, None],
			[None, None, None, "133 103 69", None, "133 103 69", "121 105 56"],
			["121 105 56", "133 103 69", "133 103 69", "133 103 69", "133 103 69", None, None],
			[None, "121 105 56", None, "133 103 69", None, None, None],
			[None, None, None, "133 103 69", None, None, None],
			[None, None, None, "133 103 69", None, None, None]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Wet_Forest_Cool", [
			[None, "38 127 0", "38 127 0", "38 127 0", None],
			["38 127 0", "38 127 0", "38 127 0", "38 127 0", "38 127 0"],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Wet_Forest_Tropical", [
			[None, "38 127 0", "38 127 0", "38 127 0", None],
			["38 127 0", "38 127 0", "38 127 0", "38 127 0", "38 127 0"],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None]
		]))
	f_ajout_arbre(v_dic_arbres, cl_arbre("Wet_Forest_Warm", [
			[None, "38 127 0", "38 127 0", "38 127 0", None],
			["38 127 0", "38 127 0", "38 127 0", "38 127 0", "38 127 0"],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None],
			[None, None, "95 80 51", None, None]
		]))

	f_ajout_arbre(v_dic_arbres, cl_arbre("Woodland_Thorn", [
			[None, "39 67 0", "39 67 0", "39 67 0", "39 67 0", "39 67 0", None],
			["39 67 0", "39 67 0", "39 67 0", "39 67 0", "39 67 0", "39 67 0", "39 67 0"],
			[None, "138 127 99", None, "118 98 65", None, "138 127 99", None],
			[None, None, None, "118 98 65", None, "138 127 99", None],
			[None, None, None, None, "118 98 65", None, None],
			[None, None, None, None, "118 98 65", None, None]
		]))



	return v_dic_arbres
