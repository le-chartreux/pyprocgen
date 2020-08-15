# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoardColor, un tableau de Color en 2D
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# - getters
# - setters
# - add_element()
# - add_line()
# - get_element()
# - get_line()
# - set_element()
# ==========================================================

from __future__ import annotations
from typing import List, Optional

from packages.classes.Board import Board
from packages.classes.Color import Color
from packages.classes.Position import Position


class BoardColor(Board):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
    )

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: Optional[List[List[Color]]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet BoardColor, héritant de Board,
        # caractérisé par :
        # - ses éléments (une liste de liste de Color)
        # -----------------------------
        # PRÉCONDITION:
        # elements: liste de Color à au moins deux dimensions ou None
        # =============================
        super().__init__(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> List[List[Color]]:
        return super(BoardColor, self).get_elements()

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: List[List[Color]]) -> None:
        line = 0
        column = 0
        while line < len(elements) and isinstance(elements[line], list) and column == 0:
            while (
                    column < len(elements[line])
                    and (
                            isinstance(elements[line][column], Color)
                            or elements[line][column] is None
                    )
            ):
                column += 1
            if column == len(elements[line]):
                column = 0
                line += 1

        if line == len(elements):
            super(BoardColor, self).set_elements(elements)
        else:
            raise Exception(
                "Error: trying to set _elements for a " + type(self).__name__ +
                " but at least one element is not a Color."
            )

    ###############################################################
    ######################### ADD_ELEMENT #########################
    ###############################################################
    def add_element(
            self,
            value: object,
            line: int
    ) -> None:
        if isinstance(value, Color):
            super(BoardColor, self).add_element(value, line)
        else:
            raise Exception(
                "Error: trying to add an element in a " + type(self).__name__ + "._elements :" +
                "\nvalue must be a Color, but a " + type(value).__name__ + " is given."
            )

    ###############################################################
    ########################### ADD_LINE ##########################
    ###############################################################
    def add_line(self, line: Optional[List[Color]] = None) -> None:
        if line is None:
            super(BoardColor, self).add_line()
        elif isinstance(line, list):
            i = 0
            while i < len(line) and isinstance(line[i], Color):
                i += 1
            if i == len(line):
                super(BoardColor, self).add_line(line)
            else:
                raise Exception(
                    "Error: impossible to add a line in a " + type(self).__name__ + "._elements :" +
                    "\nlines must be List[Color], but a List[" + type(line[i]).__name__ + "] is given."
                )
        else:
            raise Exception(
                "Error: impossible to add a line in a " + type(self).__name__ + "._elements :" +
                "\nlines must be List[Color], but a " + type(line).__name__ + " is given."
            )

    ###############################################################
    ######################### GET_ELEMENT #########################
    ###############################################################
    def get_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> Optional[Color]:
        element = super(BoardColor, self).get_element()
        if element is None or isinstance(element, Color):
            return element
        else:
            raise Exception(
                "Error: an element of a " + type(self).__name__ + " is a " + type(element).__name__ +
                ", must be a Color or None"
            )

    ###############################################################
    ########################## GET_LINE ###########################
    ###############################################################
    def get_line(self, line_number: int) -> List[Optional[Box]]:
        line = super(BoardColor, self).get_line(line_number)
        i = 0
        while i < len(line) and (isinstance(line[i], Color) or line[i] is None):
            i += 1
        if i == len(line):
            return line
        else:
            raise Exception(
                "Error: trying to get a line from a " + type(self).__name__ +
                "._elements but at least one element is a " + type(line[i]).__name__ + ", must be a Color."
            )

    ###############################################################
    ######################### SET_ELEMENTS ########################
    ###############################################################
    def set_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None,
            value: Optional[Color] = None
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
        if isinstance(value, Color) or value is None:
            super(BoardColor, self).set_element(value, x, y, position)
        else:
            raise Exception(
                "Error: impossible to set an element in a " + type(self).__name__ + ".elements:" +
                "\nelement must be a Color or None, is a " + type(value).__name__ + "."
            )
