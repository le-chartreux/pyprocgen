# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Board, un tableau en 2D d'un type unique (peut quand même contenir des None)
# qui peut utiliser un objet Position
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

from packages.classes.Position import Position
from packages.settings import DEBUG_MOD
from packages.utilities import check_attribute_type_set


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
    TYPE_OF_ELEMENTS: Optional = Optional[object]  # mit en Optional pour la cohérence des classes filles

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: Optional[List[List[TYPE_OF_ELEMENTS]]] = None) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Board, caractérisé par :
        # - _elements: List[List[TYPE_OF_ELEMENTS]]
        # =============================
        if elements is None:
            self.set_elements([[]])
        else:
            self.set_elements(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> List[List[TYPE_OF_ELEMENTS]]:
        return self._elements

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: List[List[TYPE_OF_ELEMENTS]]) -> None:
        # Vérification que éléments est bien un List[List[TYPE_OF_ELEMENTS]]
        # Vérification que éléments est bien un List
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=elements,
                type_to_check=list,
                name_of_attribute_to_check="_elements",
                object_destination=self
            )

            # Vérification que elements est bien un List de quelque chose
            if len(elements) == 0:
                raise Exception(
                    "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                    "\n_elements must be a List[List[" + str(self.TYPE_OF_ELEMENTS) + "]], but an empty list is given."
                )
            # Vérification que elements est bien un List[List]
            i = 0
            while i < len(elements) and isinstance(elements[i], list):
                i += 1
            if i == len(elements):
                # Vérification que elements est bien un List[List[self.TYPE_OF_ELEMENTS]
                line = 0
                column = 0
                while (
                        line < len(elements) and
                        isinstance(elements[line], list) and
                        column == 0
                ):
                    while (
                            column < len(elements[line])
                            and isinstance(elements[line][column], self.TYPE_OF_ELEMENTS.__args__)
                    ):
                        column += 1
                    if column == len(elements[line]):
                        column = 0
                        line += 1

                if line != len(elements):
                    raise Exception(
                        "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                        "\n_elements must be a List[List[" + str(self.TYPE_OF_ELEMENTS) + "]] " +
                        "but at least one List[List]'s element is a " + type(elements[line][column]).__name__ + "."
                    )
            else:
                raise Exception(
                    "Error: impossible to set _elements for a " + type(self).__name__ + ":" +
                    "\n_elements must be a List[List[" + str(self.TYPE_OF_ELEMENTS) + "]] " +
                    "but at least one List's element is not a List."
                )
        self._elements = elements

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
        if DEBUG_MOD:
            if not isinstance(element, self.TYPE_OF_ELEMENTS.__args__):
                raise Exception(
                    "Error: impossible to add an element in a " + type(self).__name__ + "._elements:" +
                    "\n_elements is a List[List[" + str(self.TYPE_OF_ELEMENTS) + "]], but a " +
                    type(element).__name__ + " is given."
                )
        self.get_line(line).append(element)

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
        if line is None:
            self.get_elements().append([])
        else:
            if DEBUG_MOD:
                # Vérification que line: List[TYPE_OF_ELEMENTS]
                # Vérification que line: List
                if isinstance(line, list):
                    # Vérification que line: List[TYPE_OF_ELEMENTS]
                    i = 0
                    while i < len(line) and isinstance(line[i], self.TYPE_OF_ELEMENTS.__args__):
                        i += 1
                    if i != len(line):  # line n'est pas un List[TYPE_OF_ELEMENTS]
                        raise Exception(
                            "Error: impossible to add a line in a " + type(self).__name__ + "_elements:" +
                            "\nlines must be List[" + type(self.TYPE_OF_ELEMENTS).__name__ +
                            "] but at least one element is a " + type(line[i]).__name__ + "."
                        )

                else:  # line n'est pas un List
                    raise Exception(
                        "Error: impossible to add a line in a " + type(self).__name__ + "_elements:" +
                        "\nline must be a List[" + str(self.TYPE_OF_ELEMENTS) + "], but a " +
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
        if x is not None and y is not None:  # La position est demandée avec x et y
            if DEBUG_MOD:
                if isinstance(x, int) and isinstance(y, int):  # Vérification que x et y sont des int
                    # Vérification que x et y sont des index valides
                    if not (0 <= x < self.get_width() and 0 <= y < self.get_height()):
                        # x et/ou y ne sont pas des index valide
                        raise Exception(
                            "Error: impossible to get an element of a " + type(self).__name__ + "._elements:" +
                            "\nIndex out of range:" +
                            "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                            ", requested " + str(x) + "." +
                            "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                            ", requested " + str(y) + "." +
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
            return self.get_elements()[y][x]
        elif position is not None:  # La position est demandée avec position
            if DEBUG_MOD:
                # Vérification que position est un index valide
                if not (0 <= position.get_x() < self.get_width() and 0 <= position.get_y() < self.get_height()):
                    raise Exception(
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
            raise Exception(
                "Error: trying to get an element from a " + type(self).__name__ + "._elements, " +
                "but no positional argument is given."
            )

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
        if DEBUG_MOD:
            if isinstance(line_number, int):
                if not (0 <= line_number < self.get_height()):
                    raise Exception(
                        "Error: trying to get a line from a " + type(self).__name__ +
                        "._elements but index is out of range:" +
                        "requested .elements[" + str(line_number) + "] but len(elements) = " + str(self.get_height()) +
                        "."
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
        if x is not None and y is not None:  # La position est demandée avec x et y
            if DEBUG_MOD:
                if isinstance(x, int) and isinstance(y, int):  # Vérification que x et y sont des int
                    # Vérification que x et y sont des index valides
                    if not (0 <= x < self.get_width() and 0 <= y < self.get_height()):
                        # x et/ou y ne sont pas des index valide
                        raise Exception(
                            "Error: impossible to set an element of a " + type(self).__name__ + "._elements:" +
                            "\nIndex out of range:" +
                            "\nWidth of the " + type(self).__name__ + " is " + str(self.get_width()) +
                            ", requested " + str(x) + "." +
                            "\nHeight of the " + type(self).__name__ + " is " + str(self.get_height()) +
                            ", requested " + str(y) + "." +
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
            self.get_elements()[y][x] = value
        elif position is not None:  # La position est demandée avec position
            if DEBUG_MOD:
                # Vérification que position est un index valide
                if not (0 <= position.get_x() < self.get_width() and 0 <= position.get_y() < self.get_height()):
                    raise Exception(
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
            raise Exception(
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
    def create_empty_board(cls, width: int, height: int) -> Board:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un Board (ou un objet d'une classe en héritant) rempli de None, de dimension height x width
        # =============================
        board = cls()
        board._elements = []

        for line in range(height):

            board.add_line()

            for _ in range(width):
                board.add_element(None, line)

        return board
