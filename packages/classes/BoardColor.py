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

