# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Biome, qui sert à avoir les infos sur un biome
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# - getters
# - setters
# - __str__() -> str
# - in_range() -> bool
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
        # - trees : liste de Tree
        # - ground_color : instance de Color
        # - autres entées convertibles en leur type indiqué
        # =============================

        self._name = None
        self.set_name(name)

        self._temperature_min = None
        self.set_temperature_min(temperature_min)

        self._temperature_max = None
        self.set_temperature_max(temperature_max)

        self._pluviometry_min = None
        self.set_pluviometry_min(pluviometry_min)

        self._pluviometry_max = None
        self.set_pluviometry_max(pluviometry_max)

        self._ground_color = None
        self.set_ground_color(ground_color)

        self._trees = None
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
        try:
            self._name = str(name)
        except ValueError:
            raise Exception(
                "Error: impossible to set name for a Biome, when trying to convert " +
                str(name) +
                " to str."
            )

    def set_temperature_min(self, temperature_min: int) -> None:
        try:
            self._temperature_min = int(temperature_min)
        except ValueError:
            raise Exception(
                "Error: impossible to set minimal_temperature for a Biome, when trying to convert " +
                str(type(temperature_min)) +
                "to int."
            )

    def set_temperature_max(self, temperature_max: int) -> None:
        try:
            self._temperature_max = int(temperature_max)
        except ValueError:
            raise Exception(
                "Error: impossible to set maximal_temperature for a Biome, when trying to convert.",
                type(temperature_max),
                "to int."
            )

    def set_pluviometry_min(self, pluviometry_min: int) -> None:
        try:
            self._pluviometry_min = int(pluviometry_min)
        except ValueError:
            raise Exception(
                "Error: impossible to set minimal_pluviometry for a Biome, when trying to convert " +
                str(type(pluviometry_min)) +
                " to int."
            )

    def set_pluviometry_max(self, pluviometry_max: int) -> None:
        try:
            self._pluviometry_max = int(pluviometry_max)
        except ValueError:
            raise Exception(
                "Error: impossible to set maximal_pluviometry for a Biome, when trying to convert " +
                str(type(pluviometry_max)) +
                " to int."
            )

    def set_ground_color(self, ground_color: Color) -> None:
        if isinstance(ground_color, Color):
            self._ground_color = ground_color
        else:
            raise Exception(
                "Error: impossible to set a ground_color for a Biome: " +
                str(type(ground_color)) +
                " is not Color"
            )

    def set_trees(self, trees: list) -> None:

        iterator = iter(trees)
        tree = next(iterator, None)

        while tree is not None and isinstance(tree, Tree):
            tree = next(iterator, None)

        if tree is None:
            self._trees = trees
        else:
            raise Exception(
                "Error: impossible to set trees for a Biome: at least one item in trees is not a tree."
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

