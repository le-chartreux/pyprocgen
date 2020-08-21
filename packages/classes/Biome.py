# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Biome, qui sert à avoir les infos sur un biome
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + in_range()
# + __str__()
# ==========================================================

from typing import List

from packages.classes.Color import Color
from packages.classes.Tree import Tree
from packages.constants import (
    BIOME_NAME_LEN_MIN,
    BIOME_NAME_LEN_MAX,
    BIOME_PLUVIOMETRY_MIN,
    BIOME_PLUVIOMETRY_MAX,
    BIOME_TEMPERATURE_MIN,
    BIOME_TEMPERATURE_MAX,
    BIOME_TREES_LEN_MIN,
    BIOME_TREES_LEN_MAX
)


class Biome:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_name",
        "_pluviometry_min",
        "_pluviometry_max",
        "_temperature_min",
        "_temperature_max",
        "_ground_color",
        "_trees"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _name: str
    _pluviometry_min: int
    _pluviometry_max: int
    _temperature_min: int
    _temperature_max: int
    _ground_color: Color
    _trees: List[Tree]

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            name: str,
            pluviometry_min: int,
            pluviometry_max: int,
            temperature_min: int,
            temperature_max: int,
            ground_color: Color,
            trees: List[Tree]
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Biome, caractérisé par :
        # - son nom
        # - sa température minimale
        # - sa température maximale
        # - sa pluviometrie minimale
        # - sa pluviometrie maximale
        # - la couleur de son sol
        # - une liste des arbres qui y poussent
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_NAME_LEN_MIN <= len(name) <= BIOME_NAME_LEN_MAX
        # - Les temperatures & pluviometries concordent avec leurs minimums et maximums
        # =============================
        self.set_name(name)

        self.set_pluviometry_min(pluviometry_min)
        self.set_pluviometry_max(pluviometry_max)
        self.set_temperature_min(temperature_min)
        self.set_temperature_max(temperature_max)

        self.set_ground_color(ground_color)
        self.set_trees(trees)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_name(self) -> str:
        return self._name

    def get_pluviometry_min(self) -> int:
        return self._pluviometry_min

    def get_pluviometry_max(self) -> int:
        return self._pluviometry_max

    def get_temperature_min(self) -> int:
        return self._temperature_min

    def get_temperature_max(self) -> int:
        return self._temperature_max

    def get_ground_color(self) -> Color:
        return self._ground_color

    def get_trees(self) -> List[Tree]:
        return self._trees

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_name(self, name: str) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de name puis le set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_NAME_LEN_MIN <= len(name) <= BIOME_NAME_LEN_MAX
        # =============================
        if isinstance(name, str):
            if BIOME_NAME_LEN_MIN <= len(name) <= BIOME_NAME_LEN_MAX:
                self._name = name
            else:
                raise Exception(
                    "Error: impossible to set _name for a " + type(self).__name__ + ":" +
                    "\nlen(_name) must be between " + str(BIOME_NAME_LEN_MIN) + " and " +
                    str(BIOME_NAME_LEN_MAX) + " but input's len is " + str(len(name)) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _name for a " + type(self).__name__ + ":" +
                "\n_name must be a str, but a " + type(name).__name__ + " is given."
            )

    def set_pluviometry_min(self, pluviometry_min: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de pluviometry_min puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_PLUVIOMETRY_MIN <= pluviometry_min <= BIOME_PLUVIOMETRY_MAX
        # =============================
        if isinstance(pluviometry_min, int):
            if BIOME_PLUVIOMETRY_MIN <= pluviometry_min <= BIOME_PLUVIOMETRY_MAX:
                self._pluviometry_min = pluviometry_min
            else:
                raise Exception(
                    "Error: impossible to set _pluviometry_min for a " + type(self).__name__ + ":" +
                    "\n_pluviometry_min must be between " + str(BIOME_PLUVIOMETRY_MAX) + " and " +
                    str(BIOME_PLUVIOMETRY_MAX) + " but input's value is " + str(pluviometry_min) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _pluviometry_min for a " + type(self).__name__ + ":" +
                "\n_pluviometry_min must be an int, but a " + type(pluviometry_min).__name__ + " is given."
            )

    def set_pluviometry_max(self, pluviometry_max: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de pluviometry_max puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_PLUVIOMETRY_MIN <= pluviometry_max <= BIOME_PLUVIOMETRY_MAX
        # =============================
        if isinstance(pluviometry_max, int):
            if BIOME_PLUVIOMETRY_MIN <= pluviometry_max <= BIOME_PLUVIOMETRY_MAX:
                self._pluviometry_max = pluviometry_max
            else:
                raise Exception(
                    "Error: impossible to set _pluviometry_max for a " + type(self).__name__ + ":" +
                    "\n_pluviometry_max must be between " + str(BIOME_PLUVIOMETRY_MAX) + " and " +
                    str(BIOME_PLUVIOMETRY_MAX) + " but input's value is " + str(pluviometry_max) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _pluviometry_max for a " + type(self).__name__ + ":" +
                "\n_pluviometry_max must be an int, but a " + type(pluviometry_max).__name__ + " is given."
            )


    def set_temperature_min(self, temperature_min: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de temperature_min puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_TEMPERATURE_MIN <= temperature_min <= BIOME_TEMPERATURE_MAX
        # =============================
        if isinstance(temperature_min, int):
            if BIOME_TEMPERATURE_MIN <= temperature_min <= BIOME_TEMPERATURE_MAX:
                self._temperature_min = temperature_min
            else:
                raise Exception(
                    "Error: impossible to set _temperature_min for a " + type(self).__name__ + ":" +
                    "\n_temperature_min must be between " + str(BIOME_TEMPERATURE_MIN) + " and " +
                    str(BIOME_TEMPERATURE_MAX) + " but input's value is " + str(temperature_min) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _temperature_min for a " + type(self).__name__ + ":" +
                "\n_temperature_min must be an int, but a " + type(temperature_min).__name__ + " is given."
            )

    def set_temperature_max(self, temperature_max: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de temperature_max puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_TEMPERATURE_MIN <= temperature_max <= BIOME_TEMPERATURE_MAX
        # =============================
        if isinstance(temperature_max, int):
            if BIOME_TEMPERATURE_MIN <= temperature_max <= BIOME_TEMPERATURE_MAX:
                self._temperature_max = temperature_max
            else:
                raise Exception(
                    "Error: impossible to set _temperature_max for a " + type(self).__name__ + ":" +
                    "\n_temperature_max must be between " + str(BIOME_TEMPERATURE_MIN) + " and " +
                    str(BIOME_TEMPERATURE_MAX) + " but input's value is " + str(temperature_max) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _temperature_max for a " + type(self).__name__ + ":" +
                "\n_temperature_max must be an int, but a " + type(temperature_max).__name__ + " is given."
            )

    def set_ground_color(self, ground_color: Color) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de ground_color puis la set
        # =============================
        if isinstance(ground_color, Color):
            self._ground_color = ground_color
        else:
            raise Exception(
                "Error: impossible to set _ground_color for a " + type(self).__name__ + ":" +
                "\n_ground_color must be a Color, but a " + type(ground_color).__name__ + " is given."
            )

    def set_trees(self, trees: List[Tree]) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de pluviometry_max puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_PLUVIOMETRY_MIN <= pluviometry_max <= BIOME_PLUVIOMETRY_MAX
        # =============================
        if isinstance(trees, list):
            if BIOME_TREES_LEN_MIN <= len(trees) <= BIOME_TREES_LEN_MAX:
                i = 0

                while i < len(trees) and isinstance(trees[i], Tree):
                    i += 1

                if i == len(trees):
                    self._trees = trees
                else:
                    raise Exception(
                        "Error: impossible to set _trees for a " + type(self).__name__ + ":" +
                        "\n_trees must be a List[Tree] but element number " + str(i) + " is a " +
                        type(trees[i]).__name__ + "."
                    )
            else:
                raise Exception(
                    "Error: impossible to set _trees for a " + type(self).__name__ + ":" +
                    "\nlen(_trees) must be between " + str(BIOME_TREES_LEN_MIN) + " and " +
                    str(BIOME_TREES_LEN_MAX) + " but input's len is " + str(len(trees)) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _trees for a " + type(self).__name__ + ":" +
                "\n_trees must be a List[Tree] but a " + type(trees).__name__ + " is given."
            )

    ###############################################################
    ########################## IN_RANGE ###########################
    ###############################################################
    def in_range(self, temperature: float, pluviometry: float) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie si la température et la pluviométrie
        # correspondent à celles de ce biome
        # =============================
        return (
                self.get_temperature_min() <= float(temperature) <= self.get_temperature_max() and
                self.get_pluviometry_min() <= float(pluviometry) < self.get_pluviometry_max()
        )

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self) -> str:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Passe les données du Biome en str. Utilisé pour debug
        # =============================
        return (
                "name: " +
                self.get_name() +
                "\ntemperature_min: " +
                str(self.get_temperature_min()) +
                "\ntemperature_max:" +
                str(self.get_temperature_max()) +
                "\npluviometry_min: " +
                str(self.get_pluviometry_min()) +
                "\npluviometry_max: " +
                str(self.get_pluviometry_max())
        )
