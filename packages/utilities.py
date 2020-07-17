# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Vrac d'utilitaires qui ne sont pas propres à ce projet
# -----------------------------
# CONTENU :
# - is_integer(value)
# - is_float(value)
# - print_progression(text, progression)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# ==========================================================

###############################################################
######################### IS_INTEGER ##########################
###############################################################
def is_integer(value) -> bool:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Regarde si value est un entier
    # -----------------------------
    # UTILISÉ PAR :
    # - procedural_generation_2D.py
    # =============================
    try:
        return int(value) == float(value)
    except:
        return False


###############################################################
######################### IS_FLOAT ############################
###############################################################
def is_float(value) -> bool:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Regarde si value est un float
    # -----------------------------
    # UTILISÉ PAR :
    # - procedural_generation_2D.py
    # =============================
    try:
        float(value)
        return True
    except:
        return False


###############################################################
##################### PRINT_PROGRESSION #######################
###############################################################
def print_progress(text: str, progression: float):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Affiche la progression dans la console, avec un # par tranche de 0.1
    # Forme : text + "[####------]" + (progression, en pourcent) + "%"
    # -----------------------------
    # PRECONDITIONS :
    # - progression compris entre 0 et 1
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================

    progress10 = int(progression * 30)
    progress_bar = ""

    # Remplissage de la barre de progression des "%" :
    for _ in range(progress10):
        progress_bar += "#"

    # Remplissage de la barre de progression de "." sur la partie restante :
    for _ in range(30 - progress10):
        progress_bar += "."

    # Ajout de zeros après la virgule pour les floats trop cours
    # (sinon le \r ne réécrit pas tout) :
    if round(progression, 3) == progression:
        progression_str = str(round(progression * 100, 2)) + "0"

    else:
        progression_str = str(round(progression * 100, 2))

    # Affichage de la progression :
    print(
        text +
        "[" +
        progress_bar +
        "] " +
        progression_str +
        " %",
        end="\r"
    )
