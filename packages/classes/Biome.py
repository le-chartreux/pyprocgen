# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Biome, qui sert à avoir les infos sur un biome
# -----------------------------
# CONTENU :
# - __slots__
# - HINTS
# - __init__()
# - GETTERS
# - SETTERS
# - in_range()
# - __str__()
# ==========================================================

from typing import List

from packages.classes.Color import Color
from packages.classes.Tree import Tree


class Biome:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_name",
        "_temperature_min",
        "_temperature_max",
        "_pluviometry_min",
        "_pluviometry_max",
        "_ground_color",
        "_trees"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _name: str
    _temperature_min: int
    _temperature_max: int
    _pluviometry_min: int
    _pluviometry_max: int
    _ground_color: Color
    _trees: List[Tree]

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            name: str,
            temperature_min: int,
            temperature_max: int,
            pluviometry_min: int,
            pluviometry_max: int,
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
        # - Les entrées sont de leur type
        # =============================
        self.set_name(name)

        self.set_temperature_min(temperature_min)
        self.set_temperature_max(temperature_max)
        self.set_pluviometry_min(pluviometry_min)
        self.set_pluviometry_max(pluviometry_max)

        self.set_ground_color(ground_color)
        self.set_trees(trees)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_name(self) -> str:
        return self._name

    def get_temperature_min(self) -> int:
        return self._temperature_min

    def get_temperature_max(self) -> int:
        return self._temperature_max

    def get_pluviometry_min(self) -> int:
        return self._pluviometry_min

    def get_pluviometry_max(self) -> int:
        return self._pluviometry_max

    def get_ground_color(self) -> Color:
        return self._ground_color

    def get_trees(self) -> List[Tree]:
        return self._trees

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_name(self, name: str) -> None:
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception(
                "Error: impossible to set _name for a " + type(self).__name__ + ":" +
                "\n_name must be a str, but a " + type(name).__name__ + " is given."
            )

    def set_temperature_min(self, temperature_min: int) -> None:
        if isinstance(temperature_min, int):
            self._temperature_min = temperature_min
        else:
            raise Exception(
                "Error: impossible to set _temperature_min for a " + type(self).__name__ + ": " +
                "\n_temperature_min must be an int, but a " + type(temperature_min).__name__ + " is given."
            )

    def set_temperature_max(self, temperature_max: int) -> None:
        if isinstance(temperature_max, int):
            self._temperature_min = temperature_max
        else:
            raise Exception(
                "Error: impossible to set _temperature_max for a " + type(self).__name__ + ":" +
                "\n_temperature_max must be an int, but a " + type(temperature_max).__name__ + " is given."
            )

    def set_pluviometry_min(self, pluviometry_min: int) -> None:
        if isinstance(pluviometry_min, int):
            self._pluviometry_min = pluviometry_min
        else:
            raise Exception(
                "Error: impossible to set _pluviometry_min for a " + type(self).__name__ + ":" +
                "\n_pluviometry_min must be an int, but a " + type(pluviometry_min).__name__ + " is given."
            )

    def set_pluviometry_max(self, pluviometry_max: int) -> None:
        if isinstance(pluviometry_max, int):
            self._pluviometry_max = pluviometry_max
        else:
            raise Exception(
                "Error: impossible to set _pluviometry_max for a " + type(self).__name__ + ":" +
                "\n_pluviometry_max must be an int, but a " + type(pluviometry_max).__name__ + " is given."
            )

    def set_ground_color(self, ground_color: Color) -> None:
        if isinstance(ground_color, Color):
            self._ground_color = ground_color
        else:
            raise Exception(
                "Error: impossible to set _ground_color for a " + type(self).__name__ + ":" +
                "\n_ground_color must be a Color, but a " + type(ground_color).__name__ + " is given."
            )

    def set_trees(self, trees: List[Tree]) -> None:

        i = 0

        while i < len(trees) and isinstance(trees[i], Tree):
            i += 1

        if i == len(trees):
            self._trees = trees
        else:
            raise Exception(
                "Error: impossible to set _trees for a " + type(self).__name__ + ":" +
                "\n_trees must be a List[Tree] but element number " + str(i) + " is a " + type(trees[i]).__name__ +
                "."
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
