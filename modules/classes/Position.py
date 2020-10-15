# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Position,
# dont les objets définissent une position en 2D
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + __str__()
# ==========================================================

from modules.settings import DEBUG_MOD
from modules.utilities import check_attribute_type_set


class Position:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_x",
        "_y"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _x: int
    _y: int

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, x: int, y: int):
        self.set_x(x)
        self.set_y(y)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_x(self, x: int) -> None:
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=x,
                type_to_check=int,
                name_of_attribute_to_check="_x",
                object_destination=self
            )
        self._x = x

    def set_y(self, y: int) -> None:
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=y,
                type_to_check=int,
                name_of_attribute_to_check="_y",
                object_destination=self
            )
        self._y = y

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self) -> str:
        return "x = " + str(self.get_x()) + "; y = " + str(self.get_y())
