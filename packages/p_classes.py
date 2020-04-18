# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - class cl_box
# - class cl_biome
# - class cl_trees_of_the_biome
# - class cl_tree
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - p_board_functions.py
# - p_decisional.py
# - p_dic_creation.py
# - p_image_creation.py
# - p_decisional.py
# =============================



##############################################################
######################### CL_BOX #############################
##############################################################
class cl_box:

	def __init__(self, v_nom_biome, v_num_arbre = -1, v_position_arbre_x = 0, v_position_arbre_y = 0):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définissant une case, caractérisée par :
		# - son type
		# - son numéro d'arbre dans le vecteur d'arbres de son biome (-1 si ce n'est pas un arbre)
		# -----------------------------
		# UTILISE PAR :
		# - p_board_functions.f_display_board()
		# - p_decisional.f_choix_biome()
		# - p_image_creation.f_image_creation()
		# - p_trees_creation.f_possible_to_place_tree
		# - p_trees_creation.f_put_tree()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome
		self.num_arbre = v_num_arbre
		self.position_arbre_x = v_position_arbre_x
		self.position_arbre_y = v_position_arbre_y

	def m_get_couleur(self, v_dic_biomes):
		if self.num_arbre == -1 :
			# ce n'est pas un arbre
			return v_dic_biomes[self.nom_biome].coul
		else :
			# c'est un arbre
			return v_dic_biomes[self.nom_biome].vect_arbres[self.num_arbre].body[self.position_arbre_y][self.position_arbre_x]


###############################################################
######################### CL_BIOME ############################
###############################################################
class cl_biome:

	def __init__(self, v_nom_biome, v_temp_min, v_temp_max, v_pluv_min, v_pluv_max, v_coul, v_vect_arbres):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant un biome, caractérisé par :
		# - son nom
		# - sa température moyenne minimale
		# - sa température moyenne maximale
		# - sa pluviometrie annuelle minimale
		# - sa pluviometrie annuelle maximale
		# - sa couleur
		# - un vecteur de cl_tree
		# -----------------------------
		# UTILISE PAR :
		# - p_dic_creation.f_dic_biomes_creation()
		# - p_decisional.f_choice_biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.nom_biome = v_nom_biome

		self.temp_min = v_temp_min
		self.temp_max = v_temp_max
		self.pluv_min = v_pluv_min
		self.pluv_max = v_pluv_max

		self.coul = v_coul

		self.vect_arbres = v_vect_arbres


	def m_in_range(self, v_temp, v_pluv):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Renvoit True si la temperature et la pluviométrie
		# correspondent à celles de ce biome
		# -----------------------------
		# UTILISE PAR :
		# - p_decisional.f_choice_biome()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - p_classes.cl_cond_biome.__init__()
		# =============================

		return self.temp_min <= v_temp <= self.temp_max and self.pluv_min <= v_pluv < self.pluv_max



##############################################################
######################### CL_TREE ############################
##############################################################
class cl_tree:
	def __init__(self, v_prob_arbre, v_body):
		# =============================
		# INFORMATIONS :
		# -----------------------------
		# UTILITE :
		# Crée la classe définisant un arbre de biome,
		# caractérisé par :
		# - la probabilité d'être placé sur une case possible
		# - le body de sa représentation ppm avec None pour les pixels vides
		# -----------------------------
		# UTILISE PAR :
		# - p_dic_functions.f_dic_biomes_creation()
		# - p_dic_functions.f_max_height_of_trees()
		# - p_trees_generation.f_possible_to_place_tree()
		# - p_trees_generation.f_put_tree()
		# -----------------------------
		# PRECONDITIONS :
		# - NONE
		# -----------------------------
		# DEPEND DE :
		# - NONE
		# =============================

		self.prob_arbre = v_prob_arbre
		self.body = v_body

	def m_get_height(self):
		return len(self.body)

	def m_get_width(self):
		return len(self.body[0])
