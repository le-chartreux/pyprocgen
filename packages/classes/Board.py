# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Board, un tableau en 2D
# qui peut utiliser un objet Position
# -----------------------------
# CONTENU :
# - __slots__
# - __init__()
# - getters
# - setters
# - get_element()
# - get_width()
# - get_height()
# - set_element()
# - create_empty_board()
# ==========================================================

from __future__ import annotations
from typing import List, Optional

from packages.classes.Position import Position


class Board:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_elements"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _elements: List[List[object]]

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: List[List[object]]) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Board, caractérisé par :
        # - ses éléments (une liste en deux dimension)
        # -----------------------------
        # PRÉCONDITION:
        # elements: liste à au moins deux dimensions
        # =============================
        self.set_elements(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> List[List[object]]:
        return self._elements

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: List[List[object]]) -> None:
        if isinstance(elements, list):
            if len(elements) == 0:
                raise Exception(
                    "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                    "\n it must be a List[List[object]], but an empty list is given."
                )
            elif isinstance(elements[0], list):
                self._elements = elements
            else:
                raise Exception(
                    "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                    "\n_elements must be a List[List[object]], but a List[" + type(elements[0]).__name__ +
                    "] is given."
                )
        else:
            raise Exception(
                "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                "\nit must be a List[List[object]], but a " + type(elements).__name__ + " is given."
            )

    ###############################################################
    ######################### GET_ELEMENT #########################
    ###############################################################
    def get_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> object:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie l'élément de self.elements en (y, x) ou en (position.y, position.x)
        # =============================
        if x is not None and y is not None:
            if isinstance(x, int) and isinstance(y, int):
                if x < self.get_width():
                    if y < self.get_height():
                        return self.get_elements()[y][x]
                    else:
                        raise Exception(
                            "Error: trying to get an element outside of the " + type(self).__name__ +
                            "._elements size size limits : " +
                            "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                            ", requested " + str(y) + "." +
                            "\n(since lists start at zero in Python, max_index = len(list) - 1)"
                        )
                else:
                    raise Exception(
                        "Error: trying to get an element outside of the " + type(self).__name__ +
                        "._elements size limits: " +
                        "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                        ", requested " + str(x) + "." +
                        "\n(since lists start at zero in Python, max_index = len(list) - 1)"
                    )

            elif not isinstance(x, int):
                raise Exception(
                    "Error: trying to get an element but asked x is a " + type(x).__name__ + ", must be an int."
                )
            elif not isinstance(y, int):
                raise Exception(
                    "Error: trying to get an element but asked y is a " + type(y).__name__ + ", must be an int."
                )
        elif position is not None:
            return self.get_elements()[position.y][position.x]
        else:
            raise Exception(
                "Error: trying to get an element from a " + type(self).__name__ + "._elements, " +
                "but no positional argument is given."
            )

    ###############################################################
    ########################## GET_WIDTH ##########################
    ###############################################################
    def get_width(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie la largeur du plateau
        # =============================
        return len(self.get_elements()[0])

    ###############################################################
    ######################### GET_HEIGHT ##########################
    ###############################################################
    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie la hauteur du plateau
        # =============================
        return len(self.get_elements())

    ###############################################################
    ######################### SET_ELEMENT #########################
    ###############################################################
    def set_element(
            self,
            value: object,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> None:
        if x >= self.get_width():
            raise Exception(
                "Error: trying to set an element outside of the " + type(self).__name__ + " size limits : " +
                "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                ", requested " + str(x) + "." +
                "\n(since lists start at zero in Python, max_index = len(list) - 1)"
            )
        elif y >= self.get_height():
            raise Exception(
                "Error: trying to set an element outside of the " + type(self).__name__ + " size limits : " +
                "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                ", requested " + str(y) + "." +
                "\n(since lists start at zero in Python, max_index = len(list) - 1)"
            )
        else:
            if x is not None and y is not None:
                self.get_elements()[y][x] = value
            elif position is not None:
                self.get_elements()[y][x] = value
            else:
                raise Exception(
                    "Error: trying to set an element on a " + type(self).__name__ + ".elements, " +
                    "but no positional argument is given"
                )

    ###############################################################
    ##################### CREATE_EMPTY_BOARD ######################
    ###############################################################
    @classmethod
    def create_empty_board(cls, width: int, height: int) -> Board:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un plateau rempli de None, de dimension height x width
        # =============================
        board = cls()
        board._elements = []

        for line in range(height):

            board.get_elements().append([])

            for _ in range(width):
                board.get_elements()[line].append(None)

        return board
