# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoxBoard, un tableau de Box en 2D
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# - getters
# - setters
# - get_element()
# - set_element()
# - create_empty_board()
# ==========================================================

from __future__ import annotations
from typing import List, Optional

from packages.classes.Board import Board
from packages.classes.Box import Box
from packages.classes.Position import Position


class BoardBox(Board):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
    )

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: Optional[List[List[Box]]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet BoardBox, héritant de Board,
        # caractérisé par :
        # - ses éléments (une liste de liste de Box)
        # -----------------------------
        # PRÉCONDITION:
        # elements: liste de Box à au moins deux dimensions
        # =============================
        super().__init__(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> List[List[Box]]:
        return super(BoardBox, self).get_elements()

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: List[List[Optional[Box]]]) -> None:
        line = 0
        column = 0
        while line < len(elements) and isinstance(elements[line], list) and column == 0:
            while (
                    column < len(elements[line])
                    and (
                            isinstance(elements[line][column], Box)
                            or elements[line][column] is None
                    )
            ):
                column += 1
            if column == len(elements[line]):
                column = 0
                line += 1

        if line == len(elements):
            super(BoardBox, self).set_elements(elements)
        else:
            raise Exception(
                "Error: trying to set _elements for a " + type(self).__name__ +
                " but at least one element is not a Box."
            )

    ###############################################################
    ######################### GET_ELEMENT #########################
    ###############################################################
    def get_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> Optional[Box]:
        element = super(BoardBox, self).get_element()
        if element is None or isinstance(element, Box):
            return element
        else:
            raise Exception(
                "Error: an element of a " + type(self).__name__ + " is a " + type(element).__name__ +
                ", must be a Box or None"
            )

    ###############################################################
    ######################### SET_ELEMENTS ########################
    ###############################################################
    def set_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None,
            value: Optional[Box] = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Set l'élément en (y,x) ou en (position.y, position.x) à value
        # -----------------------------
        # PRÉCONDITIONS:
        # - value : instance de Box
        # - x et y ou position.x et position.y existent et respectent les dimensions de elements.
        # =============================
        if isinstance(value, Box):
            super(BoardBox, self).set_element(value, x, y, position)
        else:
            raise Exception(
                "Error: impossible to set an element in a " + type(self).__name__ + ".elements:" +
                "\nelement must be a Box, is a " + type(value).__name__ + "."
            )

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self) -> str:

        str_version = ""

        for line in self.get_elements():

            for element in line:
                str_version += element.get_biome().get_name()[0:4] + " "

        str_version += "\n"

        return str_version
