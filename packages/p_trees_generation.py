# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Génère les arbres dans le plateau
# -----------------------------
# CONTENU :
# - f_generate_trees(v_plateau)
# - f_possible_to_place_tree(v_plateau, v_encyclopedie, v_x, v_y)
# - f_put_tree(v_plateau, v_encyclopedie, v_x, v_y)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# =============================

from .p_classes import cl_box, cl_tree
from .p_board_functions import f_print_progression

###############################################################
###################### F_GENERATE_TREE ########################
###############################################################
def f_generate_trees(v_plateau, v_encyclopedie):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Place les arbres dans v_plateau
    # -----------------------------
    # PRECONDITIONS :
    # - v_encyclopedie : cl_encyclopedia dont le dictionnaire de
    #   biomes comprend une liste d'au moins un arbre par biome
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_box
    # - p_classes.cl_tree
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    import random


    v_nbx = len(v_plateau[0])
    v_nby = int(len(v_plateau) / 2)

    for v_num_ligne in range(v_nby):

        for v_num_colonne in range(v_nbx):

            if v_plateau[v_num_ligne][v_num_colonne].nom_biome != "Tree":

                # Creation d'une liste à ordre aleatoire des arbres possibles
                v_liste_arbres = list(v_encyclopedie.biomes[v_plateau[v_num_ligne][v_num_colonne].nom_biome].vect_arbres)

                random.shuffle(v_liste_arbres)

                v_i = 0

                v_pose = False

                while v_i < len(v_liste_arbres) and not v_pose:

                    if f_possible_to_place_tree(v_plateau, v_liste_arbres[v_i], v_num_colonne, v_num_ligne) and random.random() < v_liste_arbres[v_i].prob_arbre :

                        f_put_tree(v_plateau, v_encyclopedie, v_liste_arbres[v_i], v_num_colonne, v_num_ligne)

                        v_pose = True

                    v_i += 1


    return v_plateau


###############################################################
################# F_POSSIBLE_TO_PLACE_TREE ####################
###############################################################
def f_possible_to_place_tree(v_plateau, v_arbre, v_x, v_y):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Renvoie si il est possible de placer l'arbre
    # -----------------------------
    # PRECONDITIONS :
    # - v_arbre : cl_tree
    # - v_x : integer, <= len(v_plateau[0])
    # - v_y : integer, <= len(v_plateau)
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_box
    # - p_classes.cl_tree
    # - random
    # -----------------------------
    # UTILISE PAR :
    # - p_trees_creation.f_generate_trees()
    # =============================
    import random

    v_type_case_origine = v_plateau[v_y][v_x].nom_biome

    possible = True


    v_larg_arbre = v_arbre.m_get_width()
    v_haut_arbre = v_arbre.m_get_height()


    if v_y + v_haut_arbre > len(v_plateau):
        v_haut_arbre = len(v_plateau) - v_y

    if v_x + v_larg_arbre > len(v_plateau[0]):
        v_larg_arbre = len(v_plateau[0]) - v_x


    for v_num_ligne in range(v_haut_arbre):

        for v_num_colonne in range(v_larg_arbre):

            if v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].nom_biome != v_type_case_origine or v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].nom_arbre != "":
                possible = False


    return possible


###############################################################
######################### F_PUT_TREE ##########################
###############################################################
def f_put_tree(v_plateau, v_encyclopedie, v_arbre, v_x, v_y):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Place un arbre depuis le point v_plateau[v_y][v_x]
    # -----------------------------
    # PRECONDITIONS :
    # - v_arbre est un objet de cl_tree
    # - v_x : integer, <= len(v_plateau[0])
    # - v_y : integer, <= len(v_plateau)
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_box
    # - p_classes.cl_tree
    # -----------------------------
    # UTILISE PAR :
    # - p_trees_creation.f_generate_trees()
    # =============================

    v_haut_arbre = v_arbre.m_get_height()
    v_larg_arbre = v_arbre.m_get_width()

    # Traitement des cas où l'arbre est en bordure d'image :
    # on coupe le modèle à la bordure (pour ne pas placer de case en dehors du tableau)
    if v_y + v_haut_arbre > len(v_plateau):
        v_haut_arbre = len(v_plateau) - v_y

    if v_x + v_larg_arbre > len(v_plateau[0]):
        v_larg_arbre = len(v_plateau[0]) - v_x

    # Placement de l'arbre
    for v_num_ligne in range(v_haut_arbre):

        for v_num_colonne in range(v_larg_arbre):

            if v_arbre.body[v_num_ligne][v_num_colonne] != None :

                v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].nom_arbre = v_arbre.nom_arbre
                v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].position_arbre_x = v_num_colonne
                v_plateau[v_y + v_num_ligne][v_x + v_num_colonne].position_arbre_y = v_num_ligne
