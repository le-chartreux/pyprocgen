# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Board, un tableau en 2D
# -----------------------------
# CONTENU :
# - __init__()
# - getters
# - get_element()
# - get_element_with_position()
# - get_width() -> int
# - get_height() -> int
# - setters
# - create_empty_board()
# ==========================================================


from packages.classes.Position import Position


class Board:

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: list = []):
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
        if elements != None:
            self.set_elements(elements)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_elements(self) -> list:
        return self._elements

    def get_element(self, x: int, y: int):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie l'élément de self.elements en (y, x)
        # =============================
        return self.get_elements()[y][x]

    def get_element_with_position(self, position: Position):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie l'élément de self.elements en (position.y, position.x)
        # =============================
        return self.get_element(position.x, position.y)

    def get_width(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie la largeur du plateau
        # =============================
        return len(self.get_elements()[0])

    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie la hauteur du plateau
        # =============================
        return len(self.get_elements())

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_elements(self, elements: list):
        try:
            elements[0][0]
            self._elements = elements
        except:
            raise Exception(
                "Error: impossible to set elements for a Board: it must be at least two-dimensional."
            )

    def set_element(self, x: int, y: int, value):
        try:
            self.get_elements()[y][x] = value
        except:
            raise Exception(
                "Error: trying to set an element outside of the Board size limits : " +
                "\nHeight of the Board is " + self.get_height + ", requested " + x + ";"
                "\nWidth of the Board is " + self.get_width + ", requested " + y + "."
            )

    ###############################################################
    ##################### CREATE_EMPTY_BOARD ######################
    ###############################################################

    @staticmethod
    def create_empty_board(width: int, height: int, board=Board()):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un plateau vide de height x width
        # =============================

        for line in range(height):

            board.get_elements().append([])

            for _ in range(width):

                board.get_elements()[line].append(None)

        return board
