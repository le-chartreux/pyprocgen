# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoxBoard, un tableau de Box en 2D
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

from packages.classes.Board import Board
from packages.classes.Box import Box
from packages.classes.Position import Position


class BoardBox(Board):

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, elements: list = []):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet BoardBox, héritant de Board,
        # caractérisé par :
        # - ses éléments (une liste en deux dimension)
        # -----------------------------
        # PRÉCONDITION:
        # elements: liste à au moins deux dimensions
        # =============================
        super.__init__(elements)

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################

    def set_element(self, x: int, y: int, value: Box):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Set l'élément en (y,x) à value
        # -----------------------------
        # PRÉCONDITIONS:
        # - value : instance de Box
        # - x et y respectent les dimensions de elements.
        # =============================
        if isinstance(value, Box):
            super.set_element(x, y, value)
        else:
            raise Exception(
                "Error: impossible to set an element for a BoardBox : an element type is " +
                str(type(value)) +
                ", must be Box."
            )

    ###############################################################
    ##################### CREATE_EMPTY_BOARD ######################
    ###############################################################
    @staticmethod
    def create_empty_board(width: int, height: int):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un BoardBox vide de height x width
        # =============================
        return super.create_empty_board(width, height, BoardBox())

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self) -> str:

        str_version = ""

        for line in self.get_elements():

            for element in line:

                str_version += element.biome.name[0:4], " "

        str_version += "\n"

        return str_version
