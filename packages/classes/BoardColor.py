# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoardColor, un tableau de Color en 2D
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + create_empty_board()
# ==========================================================

from __future__ import annotations
from typing import List, Optional, cast

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
    ############################ HINTS ############################
    ###############################################################
    TYPE_OF_ELEMENTS: Optional = Optional[Color]

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
        # =============================
        super().__init__(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> List[List[TYPE_OF_ELEMENTS]]:
        return cast(List[List[BoardColor.TYPE_OF_ELEMENTS]], super(BoardColor, self).get_elements())

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: List[List[TYPE_OF_ELEMENTS]]) -> None:
        super(BoardColor, self).set_elements(elements)

    ###############################################################
    ######################### ADD_ELEMENT #########################
    ###############################################################
    def add_element(
            self,
            element: TYPE_OF_ELEMENTS,
            line: int
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Ajoute element à la fin de _elements[line]
        # -----------------------------
        # PRÉCONDITIONS :
        # - 0 < line < len(elements)
        # =============================
        super(BoardColor, self).add_element(element, line)

    ###############################################################
    ########################### ADD_LINE ##########################
    ###############################################################
    def add_line(self, line: Optional[List[TYPE_OF_ELEMENTS]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Ajoute line à la fin de _elements
        # (si line is None, ajoute [] à la fin de _elements)
        # =============================
        super(BoardColor, self).add_line(line)

    ###############################################################
    ######################### GET_ELEMENT #########################
    ###############################################################
    def get_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> TYPE_OF_ELEMENTS:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie l'élément de self._elements en (y, x) ou en (position.y, position.x)
        # -----------------------------
        # PRÉCONDITIONS :
        # - x et y non None et sont des index valides
        # OU
        # - position non None et est un index valide
        # =============================
        return cast(BoardColor.TYPE_OF_ELEMENTS, super(BoardColor, self).get_element(x=x, y=y, position=position))

    ###############################################################
    ########################## GET_LINE ###########################
    ###############################################################
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Renvoie l'élément en self._elements[line_number]
    # -----------------------------
    # PRÉCONDITIONS :
    # - 0 <= line_number < len(self._elements)
    # =============================
    def get_line(self, line_number: int) -> List[TYPE_OF_ELEMENTS]:
        return cast(List[BoardColor.TYPE_OF_ELEMENTS], super(BoardColor, self).get_line(line_number))

    ###############################################################
    ######################### SET_ELEMENT #########################
    ###############################################################
    def set_element(
            self,
            value: TYPE_OF_ELEMENTS,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Set l'élément de self._elements en (y, x) ou (position.y, position.x) à value
        # -----------------------------
        # PRÉCONDITIONS :
        # - x et y non None et sont des index valides
        # OU
        # - position non None et est un index valide
        # =============================
        super(BoardColor, self).set_element(value=value, x=x, y=y, position=position)

    ###############################################################
    ##################### CREATE_EMPTY_BOARD ######################
    ###############################################################
    @classmethod
    def create_empty_board(cls, width: int, height: int) -> BoardColor:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un BoardColor rempli de None, de dimension height x width
        # =============================
        return cast(BoardColor, super(BoardColor, cls).create_empty_board(width, height))
