# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Box, une case
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + getters
# + setters
# + get_color()
# ==========================================================

from modules.classes.Biome import Biome
from modules.classes.Color import Color

from modules.settings import DEBUG_MOD
from modules.utilities import check_attribute_type_set


class Box:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_biome"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _biome: Biome

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            biome: Biome
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Box (case), caractérisé par :
        # - son biome
        # =============================
        self.set_biome(biome)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_biome(self) -> Biome:
        return self._biome

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_biome(self, biome: Biome) -> None:
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=biome,
                type_to_check=Biome,
                name_of_attribute_to_check="_biome",
                object_destination=self
            )
        self._biome = biome

    ###############################################################
    ########################## GET_COLOR ##########################
    ###############################################################
    def get_color(self) -> Color:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Revoie la couleur de la case,
        # donc celle du sol puisque il n'y a pas d'arbre
        # =============================
        return self.get_biome().get_ground_color()
