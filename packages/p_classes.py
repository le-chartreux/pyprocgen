# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - cl_box
# - cl_encyclopedia
# - cl_biome
# - cl_tree
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

    def __init__(self, v_nom_biome, v_nom_arbre = "", v_position_arbre_x = -1, v_position_arbre_y = -1):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITE :
        # Crée la classe définissant une case, caractérisée par :
        # - son type
        # - le nom de l'arbre qui est dessus ("" si il n'y a pas d'arbre)
        # - la position de son pixel d'arbre dans le modèle de l'arbre
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
        self.nom_arbre = v_nom_arbre
        self.position_arbre_x = v_position_arbre_x
        self.position_arbre_y = v_position_arbre_y

    def m_get_couleur(self, v_encyclopedie):
        if self.nom_arbre == "":
            # ce n'est pas un arbre
            return v_encyclopedie.biomes[self.nom_biome].coul
        else:
            # c'est un arbre
            return v_encyclopedie.m_get_tree_info(self.nom_arbre).body[self.position_arbre_y][self.position_arbre_x]


##############################################################
##################### CL_ENCYCLOPEDIA ########################
##############################################################
class cl_encyclopedia:

    def __init__(self, v_nom, v_biomes = []):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITE :
        # Crée la classe définissant une encyclopédie, caractérisée par :
        # - son nom
        # - les cl_biome qu'elle répertorie (dictionnaire)
        # -----------------------------
        # UTILISE PAR :
        # - procedural_generation_2D.py
        # -----------------------------
        # PRECONDITIONS :
        # - NONE
        # -----------------------------
        # DEPEND DE :
        # - NONE
        # =============================
        self.nom_encyclopedie = v_nom
        self.biomes = v_biomes

    def m_get_arbres(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITE :
        # Renvoie une liste de tous les arbres présents dans l'encyclopédie
        # -----------------------------
        # UTILISE PAR :
        # - m_get_tree_info()
        # -----------------------------
        # PRECONDITIONS :
        # - NONE
        # -----------------------------
        # DEPEND DE :
        # - p_classes.cl_biome
        # - p_classes.cl_tree
        # =============================
        v_arbres = []

        for v_biome in self.biomes.values():

            for v_arbre in v_biome.vect_arbres:

                v_arbres.append(v_arbre)

        return v_arbres


    def m_get_tree_info(self, v_nom_arbre):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITE :
        # Renvoie la classe de l'arbre à partir de son nom
        # -----------------------------
        # UTILISE PAR :
        # -----------------------------
        # PRECONDITIONS :
        # - NONE
        # -----------------------------
        # DEPEND DE :
        # - self.m_get_arbres()
        # - p_classes.cl_tree
        # =============================
        v_i = 0
        v_arbres = self.m_get_arbres()

        while v_i < len(v_arbres) and v_arbres[v_i].nom_arbre != v_nom_arbre:
            v_i += 1

        if v_i < len(v_arbres):
            return v_arbres[v_i]

        else:
            return None


    def m_max_height_of_trees(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITE :
        # Renvoie la hauteur de l'arbre le plus haut
        # -----------------------------
        # UTILISE PAR :
        # - procedural_generation_2D.py
        # -----------------------------
        # PRECONDITIONS :
        # - NONE
        # -----------------------------
        # DEPEND DE :
        # - self.m_get_arbres()
        # - p_classes.cl_tree
        # =============================
        v_arbres = self.m_get_arbres()
        v_hauteur_max = 0

        for v_arbre in v_arbres:

            if v_arbre.m_get_height() > v_hauteur_max:

                v_hauteur_max = v_arbre.m_get_height()

        return v_hauteur_max



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
        # - la couleur de son sol
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
        # Renvoie True si la temperature et la pluviométrie
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
    def __init__(self, v_nom_arbre, v_prob_arbre, v_body):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITE :
        # Crée la classe définisant un arbre de biome,
        # caractérisé par :
        # - son nom
        # - la probabilité d'être placé sur une case possible
        # - le body de sa représentation ppm avec None pour les pixels vides
        # -----------------------------
        # UTILISE PAR :
        # - p_dic_functions.f_dic_biomes_creation()
        # - p_classes.cl_encyclopedia.m_max_height_of_trees()
        # - p_trees_generation.f_possible_to_place_tree()
        # - p_trees_generation.f_put_tree()
        # -----------------------------
        # PRECONDITIONS :
        # - NONE
        # -----------------------------
        # DEPEND DE :
        # - NONE
        # =============================
        self.nom_arbre = v_nom_arbre
        self.prob_arbre = v_prob_arbre
        self.body = v_body

    def m_get_height(self):
        return len(self.body)

    def m_get_width(self):
        return len(self.body[0])
