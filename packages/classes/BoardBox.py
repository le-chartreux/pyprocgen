# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoardBox, un tableau de Box en 2D
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# - create_empty_board()
# ==========================================================

from __future__ import annotations
from typing import List, Optional

from packages.classes.Board import Board
from packages.classes.Box import Box


class BoardBox(Board):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    TYPE_OF_ELEMENTS: Optional = Optional[Box]

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
    ##################### CREATE_EMPTY_BOARD ######################
    ###############################################################
    @classmethod
    def create_empty_board(cls, width: int, height: int) -> BoardBox:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un BoardBox rempli de None, de dimension height x width
        # =============================
        bullshit_check = super(BoardBox, cls).create_empty_board(width, height)
        if isinstance(bullshit_check, BoardBox):
            return bullshit_check
        else:
            raise Exception(
                "Error: WTF how could this error happened ???"
            )


a = BoardBox.create_empty_board(0, 0)
print(a.TYPE_OF_ELEMENTS)
