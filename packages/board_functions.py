# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Créer un plateau vide,  afficher un plateau dans la console
# et gérer les seed
# -----------------------------
# CONTENU :
# - create_empty_board(width, height)
# - display_board(board)
#
# - generate_seed()
# - seed_to_string(seed)
# - string_to_seed(seed_in_string)
# - is_seed(seed_in_string)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# ==========================================================

import random


###############################################################
###################### GENERERATE_SEED ########################
###############################################################
def generate_seed() -> str:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Génère un dictionnaire de seed avec :
    # - "Tx" : seed de l'axe x de la température
    # - "Ty" : seed de l'axe y de la température
    # - "Px" : seed de l'axe x de la  pluviométrie
    # - "Py" : seed de l'axe y de la  pluviométrie
    # -----------------------------
    # PRÉCONDITIONS :
    # - None
    # -----------------------------
    # DÉPEND DE :
    # - random
    # -----------------------------
    # UTILISÉ PAR :
    # - procedural_generation_2D.py
    # =============================

    seed = {}

    seed["Tx"] = random.randint(-10000, 10000)
    seed["Ty"] = random.randint(-10000, 10000)
    seed["Px"] = random.randint(-10000, 10000)
    seed["Py"] = random.randint(-10000, 10000)

    return seed


###############################################################
######################## SEED_TO_STRING #######################
###############################################################
def seed_to_string(seed: dict) -> str:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Transforme le seed en string pour l'écrire dans le header
    # de l'image générée, de la forme
    # str(seed["Tx"]) + ":" + str(seed["Ty"]) + ":" + str(seed["Px"]) + ":" + str(seed["Py"])
    # -----------------------------
    # PRÉCONDITIONS :
    # - seed["Tx"], seed["Ty"] : integers not null
    # - seed["Px"], seed["Py"] : integers not null
    # -----------------------------
    # DÉPEND DE :
    # - None
    # -----------------------------
    # UTILISÉ PAR :
    # - procedural_generation_2D.py
    # =============================

    seed_in_string = (
        str(seed["Tx"])
        + ":" + str(seed["Ty"])
        + ":" + str(seed["Px"])
        + ":" + str(seed["Py"])
    )

    return seed_in_string


###############################################################
####################### STRING_TO_SEED ########################
###############################################################
def string_to_seed(seed_in_string: str) -> dict:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Crée un dictionnaire de seed à partir de seed_in_string avec :
    # - "Tx" : seed de l'axe x de la température
    # - "Ty" : seed de l'axe y de la température
    # - "Px" : seed de l'axe x de la  pluviométrie
    # - "Py" : seed de l'axe y de la  pluviométrie
    # -----------------------------
    # PRECONDITIONS :
    # - None
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    seed = {}
    counter = 0

    for key in ("Tx", "Ty", "Px", "Py"):

        buffer = ""

        while counter < len(seed_in_string) and seed_in_string[counter] != ":":

            buffer += seed_in_string[counter]
            counter += 1

        seed[key] = int(buffer)
        counter += 1

    return seed


###############################################################
########################### IS_SEED ###########################
###############################################################
def is_seed(seed_in_string: str) -> bool:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Vérifie que seed_in_string est bien
    # de la forme a + ":" + b + ":" + c + ":" + d
    # avec a,b,c,d str(integers)
    # -----------------------------
    # PRECONDITIONS :
    # - None
    # -----------------------------
    # DEPEND DE :
    # - None
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================
    colon_counter = 0
    position_counter = 0
    # number_of_following_colon est initialisé à 1 pour contrer le cas où seed_in_string[0] == ":"
    number_of_following_colon = 1

    while (
        position_counter < len(seed_in_string)
        and seed_in_string[position_counter] in ("0123456789-:")
        and number_of_following_colon != 2
        and not (  # Pour éviter un - au milieu d'un entier
            position_counter != 0
            and seed_in_string[position_counter] == "-"
            and seed_in_string[position_counter - 1] != ":"
        )
    ):

        if seed_in_string[position_counter] == ":":
            colon_counter += 1
            number_of_following_colon += 1

        else:
            number_of_following_colon = 0

        position_counter += 1

    return (
        position_counter == len(seed_in_string)
        and colon_counter == 3
        and number_of_following_colon == 0
    )
