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

from modules.classes.Color import Color
from modules.classes.Tree import Tree

from modules.settings import (
    DEBUG_MOD,
    BIOME_NAME_LEN_MIN,
    BIOME_NAME_LEN_MAX,
    BIOME_PLUVIOMETRY_MIN,
    BIOME_PLUVIOMETRY_MAX,
    BIOME_TEMPERATURE_MIN,
    BIOME_TEMPERATURE_MAX,
    BIOME_TREES_LEN_MIN,
    BIOME_TREES_LEN_MAX
)
from modules.utilities import check_attribute_type_set, check_number_between_to_set


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
    _pluviometry_min: float
    _pluviometry_max: float
    _temperature_min: float
    _temperature_max: float
    _ground_color: Color
    _trees: List[Tree]

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            name: str,
            pluviometry_min: float,
            pluviometry_max: float,
            temperature_min: float,
            temperature_max: float,
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

    def get_pluviometry_min(self) -> float:
        return self._pluviometry_min

    def get_pluviometry_max(self) -> float:
        return self._pluviometry_max

    def get_temperature_min(self) -> float:
        return self._temperature_min

    def get_temperature_max(self) -> float:
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
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=name,
                type_to_check=str,
                name_of_attribute_to_check="_name",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=len(name),
                min_value=BIOME_NAME_LEN_MIN,
                max_value=BIOME_NAME_LEN_MAX,
                name_of_attribute_to_check="len(_name)",
                object_to_set=self
            )
        self._name = name

    def set_pluviometry_min(self, pluviometry_min: float) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de pluviometry_min puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_PLUVIOMETRY_MIN <= pluviometry_min <= BIOME_PLUVIOMETRY_MAX
        # =============================
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=pluviometry_min,
                type_to_check=float,
                name_of_attribute_to_check="_pluviometry_min",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=pluviometry_min,
                min_value=BIOME_PLUVIOMETRY_MIN,
                max_value=BIOME_PLUVIOMETRY_MAX,
                name_of_attribute_to_check="_pluviometry_min",
                object_to_set=self
            )
        self._pluviometry_min = pluviometry_min

    def set_pluviometry_max(self, pluviometry_max: float) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de pluviometry_max puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_PLUVIOMETRY_MIN <= pluviometry_max <= BIOME_PLUVIOMETRY_MAX
        # =============================
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=pluviometry_max,
                type_to_check=float,
                name_of_attribute_to_check="_pluviometry_max",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=pluviometry_max,
                min_value=BIOME_PLUVIOMETRY_MIN,
                max_value=BIOME_PLUVIOMETRY_MAX,
                name_of_attribute_to_check="_pluviometry_max",
                object_to_set=self
            )
        self._pluviometry_max = pluviometry_max

    def set_temperature_min(self, temperature_min: float) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de temperature_min puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_TEMPERATURE_MIN <= temperature_min <= BIOME_TEMPERATURE_MAX
        # =============================
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=temperature_min,
                type_to_check=float,
                name_of_attribute_to_check="_temperature_min",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=temperature_min,
                min_value=BIOME_TEMPERATURE_MIN,
                max_value=BIOME_TEMPERATURE_MAX,
                name_of_attribute_to_check="_temperature_min",
                object_to_set=self
            )
        self._temperature_min = temperature_min

    def set_temperature_max(self, temperature_max: float) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de temperature_max puis la set
        # -----------------------------
        # PRÉCONDITIONS :
        # - BIOME_TEMPERATURE_MIN <= temperature_max <= BIOME_TEMPERATURE_MAX
        # =============================
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=temperature_max,
                type_to_check=float,
                name_of_attribute_to_check="_temperature_max",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=temperature_max,
                min_value=BIOME_TEMPERATURE_MIN,
                max_value=BIOME_TEMPERATURE_MAX,
                name_of_attribute_to_check="_temperature_max",
                object_to_set=self
            )
        self._temperature_max = temperature_max

    def set_ground_color(self, ground_color: Color) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie la cohérence de ground_color puis la set
        # =============================
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=ground_color,
                type_to_check=Color,
                name_of_attribute_to_check="_ground_color",
                object_destination=self
            )
        self._ground_color = ground_color

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
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=trees,
                type_to_check=list,
                name_of_attribute_to_check="_trees",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=len(trees),
                min_value=BIOME_TREES_LEN_MIN,
                max_value=BIOME_TREES_LEN_MAX,
                name_of_attribute_to_check="len(_trees)",
                object_to_set=self
            )
            # Vérification que tous les éléments sont instance de Tree :
            i = 0
            while i < len(trees) and isinstance(trees[i], Tree):
                i += 1

            if i != len(trees):
                raise Exception(
                    "Error: impossible to set _trees for a " + type(self).__name__ + ":" +
                    "\n_trees must be a List[Tree] but element number " + str(i) + " is a " +
                    type(trees[i]).__name__ + "."
                )
        self._trees = trees

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
                "name: " + self.get_name() +
                "\ntemperature_min: " + str(self.get_temperature_min()) +
                "\ntemperature_max: " + str(self.get_temperature_max()) +
                "\npluviometry_min: " + str(self.get_pluviometry_min()) +
                "\npluviometry_max: " + str(self.get_pluviometry_max()) +
                "\nground_color: " + str(self.get_ground_color()) +
                "\ntrees: " + str(self.get_trees())
        )
