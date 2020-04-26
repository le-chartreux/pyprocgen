# =============================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITE DE SON CONTENU :
# Créer un plateau vide, créer un seed et
# afficher un plateau dans la console
# -----------------------------
# CONTENU :
# - f_create_empty_board(co_nbx,co_nby)
# - f_display_board(v_plateau)
# - f_print_progression(v_texte, v_progression)
#
# - f_generate_seed()
# - f_seed_to_string(v_seed)
# - f_string_to_seed(v_seed_compressed)
#
# - f_is_it_a_seed(v_seed_compressed)
# - f_is_it_an_integer(valeur)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py


###############################################################
#################### F_CREATE_EMPTY_BOARD #####################
###############################################################
def f_create_empty_board(v_nbx, v_nby):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Crée un plateau vide de x cases de largeur et y de longueur
    # -----------------------------
    # PRECONDITIONS :
    # - v_nbx, v_nby : integers
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_box
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    from .p_classes import cl_box

    v_plateau=[]

    for v_hauteur in range(v_nby) :

        v_plateau.append([])

        for v_largeur in range(v_nbx) :

            v_plateau[v_hauteur].append(None)

    return v_plateau


###############################################################
##################### F_DISPLAY_BOARD #########################
###############################################################
def f_display_board(v_plateau):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Affiche un plateau de taille len(v_plateau[0]) * len(v_plateau)
    # dans la console
    # -----------------------------
    # PRECONDITIONS :
    # - NONE
    # -----------------------------
    # DEPEND DE :
    # - p_classes.cl_box
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py (pour debug)
    # =============================
    from .p_classes import cl_box

    for v_i in range(len(v_plateau)) :

        for v_j in range(len(v_plateau[0])) :

                print(v_plateau[v_i][v_j].nom_biome[0:4], " ", end="")

        print("")


def f_print_progression(v_texte, v_progression):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Affiche la progression (de 0 à 1)
    # dans la console, avec un # par tranche de 0.1
    # Forme : v_texte + "[####      ]" + (v_progression, en pourcent) + "%"
    # -----------------------------
    # PRECONDITIONS :
    # - v_progression : réel compris entre 0 et 1
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================

    v_progression10 = int(v_progression * 10)
    v_barre_progression = ""

    # Remplissage de la barre de progression des '#' :
    for i in range(v_progression10):
        v_barre_progression += "#"

    # Remplissage de la barre de progression de ' ' sur la partie restante :
    for i in range(10 - v_progression10):
        v_barre_progression += " "

    # Ajout de zeros après la virgule pour les floats trop cours
    # (sinon le \r ne réécrit pas tout) :
    if round(v_progression, 3) == v_progression:
        v_progression_str = str(round(v_progression * 100, 2)) + "0"

    else:
        v_progression_str = str(round(v_progression * 100, 2))

    # Affichage de la progression :
    print(v_texte + "[" + v_barre_progression + "] " + v_progression_str + " %", end="\r")


###############################################################
##################### F_GENERERATE_SEED #######################
###############################################################
def f_generate_seed():
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Génère un dictionnaire de seed avec :
    # - "Tx" : seed de l'axe x de la température
    # - "Ty" : seed de l'axe y de la température
    # - "Px" : seed de l'axe x de la  pluviométrie
    # - "Py" : seed de l'axe y de la  pluviométrie
    # -----------------------------
    # PRECONDITIONS :
    # - NONE
    # -----------------------------
    # DEPEND DE :
    # - random
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    import random

    v_seed = {}

    v_seed["Tx"] = random.randint(-10000,10000)
    v_seed["Ty"] = random.randint(-10000,10000)
    v_seed["Px"] = random.randint(-10000,10000)
    v_seed["Py"] = random.randint(-10000,10000)

    return v_seed


###############################################################
###################### F_SEED_TO_STRING #######################
###############################################################
def f_seed_to_string(v_seed):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Transforme le seed en string pour l'écrire dans le header
    # de l'image générée,
    # de la forme Tx + ":" + Ty + ":" + Px + ":" + Py
    # -----------------------------
    # PRECONDITIONS :
    # - v_seed["Tx"], v_seed["Ty"] : integers not null
    # - v_seed["Px"], v_seed["Py"] : integers not null
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================

    v_seed_in_string = (
          str(v_seed["Tx"]) + ":"
        + str(v_seed["Ty"]) + ":"
        + str(v_seed["Px"]) + ":"
        + str(v_seed["Py"])
    )

    return v_seed_in_string



###############################################################
###################### F_STRING_TO_SEED ########################
###############################################################
def f_string_to_seed(v_seed_in_string):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Crée un dictionnaire de seed à partir de v_seed_compressed avec :
    # - "Tx" : seed de l'axe x de la température
    # - "Ty" : seed de l'axe y de la température
    # - "Px" : seed de l'axe x de la  pluviométrie
    # - "Py" : seed de l'axe y de la  pluviométrie
    # -----------------------------
    # PRECONDITIONS :
    # - v_seed_compressed : string
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    v_seed = {}
    v_noms = ("Tx", "Ty", "Px", "Py")
    v_compteur = 0

    for i in range(4):

        v_tampon = ""

        while v_compteur < len(v_seed_in_string) and v_seed_in_string[v_compteur] != ":":

            v_tampon += v_seed_in_string[v_compteur]
            v_compteur += 1

        v_seed[v_noms[i]] = int(v_tampon)
        v_compteur += 1

    return v_seed


###############################################################
####################### F_IS_IT_A_SEED ########################
###############################################################
def f_is_it_a_seed(v_seed_compressed):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Vérifie que v_seed_compressed est bien
    # de la forme a + ":" + b + ":" + c + ":" + d
    # avec a,b,c,d str(integers)
    # -----------------------------
    # PRECONDITIONS :
    # - v_seed_compressed : string
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    v_compteur_deux_points = 0
    v_compteur_position = 0
    v_nb_deux_points_suite = 1    # Initialisé à 1 pour contrer le cas où v_seed_compressed[0] = ":"
    v_caracteres_possibles = ("0123456789-:")

    while (
        v_compteur_position < len(v_seed_compressed)
        and v_seed_compressed[v_compteur_position] in v_caracteres_possibles
        and v_nb_deux_points_suite != 2
        # Pour eviter un - au milieu d'un entier :
        and not (v_compteur_position != 0 and v_seed_compressed[v_compteur_position] == "-" and v_seed_compressed[v_compteur_position - 1] != ":")
    ):

        if v_seed_compressed[v_compteur_position] == ":":
            v_compteur_deux_points += 1
            v_nb_deux_points_suite += 1

        else:
            v_nb_deux_points_suite = 0

        v_compteur_position += 1

    return (
        v_compteur_position == len(v_seed_compressed)
        and v_compteur_deux_points == 3
        and v_nb_deux_points_suite == 0
    )


###############################################################
################### F_IS_IT_AN_INTEGER ########################
###############################################################
def f_is_it_an_integer(valeur):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITE :
    # Regarde si valeur est un entier
    # -----------------------------
    # PRECONDITIONS :
    # - NONE
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    try:
        return int(valeur) == float(valeur)
    except:
        return False
