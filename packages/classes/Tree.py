# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Tree
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + get_height
# + get_width
# ==========================================================

from packages.classes.BoardColor import BoardColor

from packages.settings import DEV_MOD
from packages.utilities import check_attribute_type_set, check_number_between_to_set


class Tree:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_name",
        "_spawn_probability",
        "_body"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _body: BoardColor
    _name: str
    _spawn_probability: float

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, name: str, spawn_probability: float, body: BoardColor):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet définissant un arbre de biome,
        # caractérisé par :
        # - son nom
        # - la probabilité d'être placé sur une case possible
        # - le body de sa représentation ppm avec None pour les pixels vides
        # -----------------------------
        # PRÉCONDITION :
        # - 0 <= spawn_probability <= 1
        # =============================
        self.set_body(body)
        self.set_name(name)
        self.set_spawn_probability(spawn_probability)

    ###############################################################
    ############################ GETTERS ##########################
    ###############################################################
    def get_body(self) -> BoardColor:
        return self._body

    def get_name(self) -> str:
        return self._name

    def get_spawn_probability(self) -> float:
        return self._spawn_probability

    ###############################################################
    ############################ SETTERS ##########################
    ###############################################################
    def set_body(self, body: BoardColor) -> None:
        if DEV_MOD:
            check_attribute_type_set(
                attribute_to_check=body,
                type_to_check=BoardColor,
                name_of_attribute_to_check="_body",
                object_destination=self
            )
        self._body = body

    def set_name(self, name: str) -> None:
        if DEV_MOD:
            check_attribute_type_set(
                attribute_to_check=name,
                type_to_check=str,
                name_of_attribute_to_check="_name",
                object_destination=self
            )
        self._name = name

    def set_spawn_probability(self, spawn_probability: float) -> None:
        if DEV_MOD:
            check_attribute_type_set(
                attribute_to_check=spawn_probability,
                type_to_check=float,
                name_of_attribute_to_check="_spawn_probability",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=spawn_probability,
                min_value=0.0,
                max_value=1.0,
                name_of_attribute_to_check="_spawn_probability",
                object_to_set=self
            )
        self._spawn_probability = spawn_probability

    ###############################################################
    ########################## GET_HEIGHT #########################
    ###############################################################
    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la hauteur de l'arbre
        # =============================
        return self.get_body().get_height()

    ###############################################################
    ########################## GET_WIDTH ##########################
    ###############################################################
    def get_width(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la largeur de l'arbre
        # =============================
        return self.get_body().get_width()
