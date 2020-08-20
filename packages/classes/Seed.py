# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Seed
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# ==========================================================
from __future__ import annotations
from typing import Optional
import random


class Seed:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "temperature_x",
        "temperature_y",
        "pluviometry_x",
        "pluviometry_y"
    )

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            pluviometry_x: Optional[int] = None,
            pluviometry_y: Optional[int] = None,
            temperature_x: Optional[int] = None,
            temperature_y: Optional[int] = None,
            string: Optional[str] = None
    ):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Seed, caractérisé par :
        # - sa temperature_x
        # - sa temperature_y
        # - sa pluviometry_x
        # - sa pluviometry_y
        # -----------------------------
        # PRÉCONDITION:
        # - Soit toutes les entrées sont des int, soit elles sont toutes None
        # =============================
        if isinstance(string, str) and Seed.is_seed(string):
            splitted_string = string.split(":")
            self.pluviometry_x = int(splitted_string[0])
            self.pluviometry_y = int(splitted_string[1])
            self.temperature_x = int(splitted_string[2])
            self.temperature_y = int(splitted_string[3])

        elif (
                isinstance(pluviometry_x, int) and
                isinstance(pluviometry_y, int) and
                isinstance(temperature_x, int) and
                isinstance(temperature_y, int)
        ):
            self.pluviometry_x = pluviometry_x
            self.pluviometry_y = pluviometry_y
            self.temperature_x = temperature_x
            self.temperature_y = temperature_y

        elif (
                pluviometry_x is None and
                pluviometry_y is None and
                temperature_x is None and
                temperature_y is None
        ):
            self.pluviometry_x = random.randint(-10000, 10000)
            self.pluviometry_y = random.randint(-10000, 10000)
            self.temperature_x = random.randint(-10000, 10000)
            self.temperature_y = random.randint(-10000, 10000)

        else:
            raise Exception(
                "Error: impossible to set an element in a " + type(self).__name__ + ":" +
                "\ninputs must all be int or all None"
            )

    ###############################################################
    ########################### IS_SEED ###########################
    ###############################################################
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Vérifie que seed_in_string est bien
    # de la forme a + ":" + b + ":" + c + ":" + d
    # avec a,b,c,d str(integers)
    # =============================
    @staticmethod
    def is_seed(string: str) -> bool:
        colon_counter = 0
        position_counter = 0
        # number_of_following_colon est initialisé à 1 pour contrer le cas où seed_in_string[0] == ":"
        number_of_following_colon = 1

        while (
                position_counter < len(string)
                and string[position_counter] in "0123456789-:"
                and number_of_following_colon != 2
                and not (  # Pour éviter un - au milieu d'un entier
                        position_counter != 0
                        and string[position_counter] == "-"
                        and string[position_counter - 1] != ":"
                )
        ):

            if string[position_counter] == ":":
                colon_counter += 1
                number_of_following_colon += 1

            else:
                number_of_following_colon = 0

            position_counter += 1

        return (
                position_counter == len(string)
                and colon_counter == 3
                and number_of_following_colon == 0
        )

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self) -> str:
        return (
                str(self.pluviometry_x) + ":" +
                str(self.pluviometry_y) + ":" +
                str(self.temperature_x) + ":" +
                str(self.temperature_y)
        )
