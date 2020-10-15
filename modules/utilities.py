# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Vrac d'utilitaires qui ne sont pas propres à ce projet
# -----------------------------
# CONTENU :
# + check_attribute_type_set()
# + check_number_between_to_set()
# + is_integer()
# + print_progression()
# ==========================================================

from typing import Union, Optional


###############################################################
################ CHECK_ATTRIBUTE_TYPE_SET #####################
###############################################################
def check_attribute_type_set(
        attribute_to_check: object,
        type_to_check: type,
        name_of_attribute_to_check: str,
        object_destination: object
) -> None:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Regarde si object_to_check est instance de type_to_check, et lève une exception si non
    # =============================
    if not isinstance(attribute_to_check, type_to_check):
        raise Exception(
            "Error: impossible to set " + name_of_attribute_to_check + " for a " +
            type(object_destination).__name__ + ":" +
            "\n" + name_of_attribute_to_check + " must be a " + type_to_check.__name__ + " but a " +
            type(attribute_to_check).__name__ + " is given."
        )


###############################################################
############### CHECK_NUMBER_BETWEEN_TO_SET ###################
###############################################################
def check_number_between_to_set(
        number_to_check: Union[int, float],
        min_value: Union[int, float],
        max_value: Union[int, float],
        name_of_attribute_to_check: str,
        object_to_set: object,
        strict_between: Optional[bool] = False
) -> None:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Regarde si min_value <= number_to_check <= max_value, et lève une exception si non
    # =============================
    if not (
            (strict_between and min_value < number_to_check < max_value) or
            (not strict_between and min_value <= number_to_check <= max_value)
    ):
        raise Exception(
            "Error: impossible to set " + name_of_attribute_to_check + " for a " + type(object_to_set).__name__ + ":" +
            "\n " + name_of_attribute_to_check + " must be between " + str(min_value) + " and " +
            str(max_value) + " but " + str(number_to_check) + " is given." +
            "\nChange the relative constant in modules/settings.py to allow."
        )


###############################################################
######################### IS_INTEGER ##########################
###############################################################
def is_integer(value: str) -> bool:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Regarde si value est convertible en un entier
    # =============================
    try:
        int(value)
        return True
    except TypeError:
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
