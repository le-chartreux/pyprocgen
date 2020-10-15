# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoardBox, un tableau de Box en 2D
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + add_element()
# + add_line()
# + get_element()
# + get_line()
# + get_height()
# + get_width()
# + set_element()
# + __str__()
# + create_empty_board()
# ==========================================================

from __future__ import annotations
from typing import List, Optional

from modules.classes.Box import Box
from modules.classes.Position import Position

from modules.settings import DEBUG_MOD
from modules.utilities import check_attribute_type_set


class BoardBox:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_elements"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _elements: List[List[Optional[Box]]]

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: Optional[List[List[Optional[Box]]]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet BoardBox, caractérisé par :
        # - ses éléments (une liste de liste de Box)
        # =============================
        self.set_elements(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> List[List[Optional[Box]]]:
        return self._elements

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: List[List[Optional[Box]]]) -> None:
        if DEBUG_MOD:
            # Vérification que elements est bien un List[List[Optional[Box]]] :
            # Vérification que elements est bien un List
            check_attribute_type_set(
                attribute_to_check=elements,
                type_to_check=list,
                name_of_attribute_to_check="_elements",
                object_destination=self
            )

            # Vérification que elements est bien un List de quelque chose
            if len(elements) == 0:
                raise TypeError(
                    "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                    "\n_elements must be a List[List[Optional[Box]], but an empty list is given."
                )
            # Vérification que elements est bien un List[List]
            i = 0
            while i < len(elements) and isinstance(elements[i], list):
                i += 1
            if i == len(elements):
                # Vérification que elements est bien un List[List[Optional[Box]
                line = 0
                column = 0
                while (
                        line < len(elements) and
                        isinstance(elements[line], list) and
                        column == 0
                ):
                    while (
                            column < len(elements[line])
                            and (
                                    elements[line][column] is None or
                                    isinstance(elements[line][column], Box)
                            )
                    ):
                        column += 1
                    if column == len(elements[line]):
                        column = 0
                        line += 1

                if line != len(elements):
                    raise TypeError(
                        "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                        "\n_elements must be a List[List[Optional[Box]] " +
                        "but at least one List[List]'s element is a " + type(elements[line][column]).__name__ + "."
                    )
            else:
                raise TypeError(
                    "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                    "\n_elements must be a List[List[Optional[Box]]] " +
                    "but at least one List's element is not a List."
                )
        self._elements = elements

    ###############################################################
    ######################### ADD_ELEMENT #########################
    ###############################################################
    def add_element(
            self,
            element: Optional[Box],
            line: int
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Ajoute element à la fin de _elements[line]
        # -----------------------------
        # PRÉCONDITIONS (uniquement si DEBUG_MOD) :
        # - 0 < line < len(elements)
        # =============================
        if DEBUG_MOD and (element is not None or not isinstance(element, Box)):
            raise TypeError(
                "Error: impossible to add an element in a " + type(self).__name__ + "._elements:" +
                "\n_elements is a List[List[Optional[Box]]], but a " +
                type(element).__name__ + " is given."
            )
        self.get_line(line).append(element)

    ###############################################################
    ########################### ADD_LINE ##########################
    ###############################################################
    def add_line(self, line: Optional[List[Optional[Box]]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Ajoute line à la fin de _elements
        # (si line is None, ajoute [] à la fin de _elements)
        # =============================
        if line is None:
            self.get_elements().append([])
        else:
            if DEBUG_MOD:
                # Vérification que line: List[Optional[Box]]
                # Vérification que line: List
                if isinstance(line, list):
                    # Vérification que line: List[Optional[Box]]
                    i = 0
                    while i < len(line) and (line[i] is None or isinstance(line[i], Box)):
                        i += 1
                    if i != len(line):  # line n'est pas un List[Optional[Box]]
                        raise TypeError(
                            "Error: impossible to add a line in a " + type(self).__name__ + "_elements:" +
                            "\nlines must be List[Optional[Box]] but at least one element is a " +
                            type(line[i]).__name__ + "."
                        )

                else:  # line n'est pas un List
                    raise TypeError(
                        "Error: impossible to add a line in a " + type(self).__name__ + "_elements:" +
                        "\nline must be a List[Optional[Box]], but a " +
                        type(line).__name__ + " is given."
                    )
            else:
                self.get_elements().append(line)

    ###############################################################
    ######################### GET_ELEMENT #########################
    ###############################################################
    def get_element(
            self,
            x: Optional[int] = None,
            y: Optional[int] = None,
            position: Optional[Position] = None
    ) -> Optional[Box]:
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
        if x is not None and y is not None:  # La position est demandée avec x et y
            if DEBUG_MOD:
                if isinstance(x, int) and isinstance(y, int):  # Vérification que x et y sont des int
                    # Vérification que x et y sont des index valides
                    if not (0 <= x < self.get_width() and 0 <= y < self.get_height()):
                        # x et/ou y ne sont pas des index valide
                        raise IndexError(
                            "Error: impossible to get an element of a " + type(self).__name__ + "._elements:" +
                            "\nIndex out of range:" +
                            "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                            ", requested " + str(x) + "." +
                            "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                            ", requested " + str(y) + "." +
                            "\n(since lists start at zero in Python, max_index = len(list) - 1)"
                        )
                elif not isinstance(x, int):
                    raise TypeError(
                        "Error: trying to get an element but asked x is a " + type(x).__name__ + ", must be an int."
                    )
                elif not isinstance(y, int):
                    raise TypeError(
                        "Error: trying to get an element but asked y is a " + type(y).__name__ + ", must be an int."
                    )
            return self.get_elements()[y][x]
        elif position is not None:  # La position est demandée avec position
            if DEBUG_MOD:
                # Vérification que position est un index valide
                if not (0 <= position.get_x() < self.get_width() and 0 <= position.get_y() < self.get_height()):
                    raise IndexError(
                        "Error: impossible to get an element of a " + type(self).__name__ + "._elements:" +
                        "\nIndex out of range:" +
                        "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                        ", requested " + str(position.get_x()) + "." +
                        "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                        ", requested " + str(position.get_y()) + "." +
                        "\n(since lists start at zero in Python, max_index = len(list) - 1)"
                    )
            return self.get_elements()[position.get_y()][position.get_x()]
        else:  # La position n'est pas demandée
            raise AttributeError(
                "Error: trying to get an element from a " + type(self).__name__ + "._elements, " +
                "but no positional argument is given."
            )

    ###############################################################
    ########################## GET_LINE ###########################
    ###############################################################
    def get_line(self, line_number: int) -> List[Optional[Box]]:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie l'élément en self._elements[line_number]
        # -----------------------------
        # PRÉCONDITIONS :
        # - 0 <= line_number < len(self._elements)
        # =============================
        if DEBUG_MOD:
            if isinstance(line_number, int):
                if not (0 <= line_number < self.get_height()):
                    raise IndexError(
                        "Error: trying to get a line from a " + type(self).__name__ +
                        "._elements but index is out of range:" +
                        "requested .elements[" + str(line_number) + "] but len(elements) = " + str(self.get_height()) +
                        "."
                    )
            else:
                raise TypeError(
                    "Error: trying to get a line but asked line number is a " + type(line_number).__name__ +
                    ", must be an int."
                )
        return self.get_elements()[line_number]

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
    ######################### SET_ELEMENT #########################
    ###############################################################
    def set_element(
            self,
            value: Optional[Box],
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
        if x is not None and y is not None:  # La position est demandée avec x et y
            if DEBUG_MOD:
                if isinstance(x, int) and isinstance(y, int):  # Vérification que x et y sont des int
                    # Vérification que x et y sont des index valides
                    if not (0 <= x < self.get_width() and 0 <= y < self.get_height()):
                        # x et/ou y ne sont pas des index valide
                        raise IndexError(
                            "Error: impossible to set an element of a " + type(self).__name__ + "._elements:" +
                            "\nIndex out of range:" +
                            "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                            ", requested " + str(x) + "." +
                            "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                            ", requested " + str(y) + "." +
                            "\n(since lists start at zero in Python, max_index = len(list) - 1)"
                        )
                elif not isinstance(x, int):
                    raise TypeError(
                        "Error: trying to get an element but asked x is a " + type(x).__name__ + ", must be an int."
                    )
                elif not isinstance(y, int):
                    raise TypeError(
                        "Error: trying to get an element but asked y is a " + type(y).__name__ + ", must be an int."
                    )
            self.get_elements()[y][x] = value
        elif position is not None:  # La position est demandée avec position
            if DEBUG_MOD:
                # Vérification que position est un index valide
                if not (0 <= position.get_x() < self.get_width() and 0 <= position.get_y() < self.get_height()):
                    raise IndexError(
                        "Error: impossible to set an element of a " + type(self).__name__ + "._elements: " +
                        "\nIndex out of range:" +
                        "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                        ", requested " + str(position.get_x()) + "." +
                        "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                        ", requested " + str(position.get_y()) + "." +
                        "\n(since lists start at zero in Python, max_index = len(list) - 1)"
                    )
            self.get_elements()[position.get_y()][position.get_x()] = value
        else:  # La position n'est pas demandée
            raise AttributeError(
                "Error: impossible to get an element from a " + type(self).__name__ + "._elements: " +
                "No positional argument is given."
            )

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self) -> str:
        string = ""
        for line in self.get_elements():
            for element in line:
                string += str(element) + " "
            string += "\n"
        return string

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
        board = cls()
        board._elements = []

        for line in range(height):

            board.add_line()

            for _ in range(width):
                board.add_element(None, line)

        return board
