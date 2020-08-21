# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoxWithTree, une case qui remplace Box
# quand cette dernière se fait poser un arbre dessus
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + get_color(self)
# ==========================================================

from packages.classes.Biome import Biome
from packages.classes.Box import Box
from packages.classes.Color import Color
from packages.classes.Position import Position
from packages.classes.Tree import Tree


class BoxWithTree(Box):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_tree",
        "_position_in_tree"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _tree: Tree
    _position_in_tree: Position

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(self, biome: Biome, tree: Tree, position_in_tree: Position) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet BoxWithTree qui hérite de Box, caractérisée par :
        # - son biome
        # - l'arbre qui est dessus
        # - la position de son pixel d'arbre dans le modèle de l'arbre
        # =============================

        super().__init__(biome)
        self.set_tree(tree)
        self.set_position_in_tree(position_in_tree)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_tree(self) -> Tree:
        return self._tree

    def get_position_in_tree(self) -> Position:
        return self._position_in_tree

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_tree(self, tree: Tree) -> None:
        if isinstance(tree, Tree):
            self._tree = tree
        else:
            raise Exception(
                "Error: impossible to set _tree for a " + type(self).__name__ + ":" +
                "\n_tree must be a Tree, but a " + type(tree).__name__ + " is given."
            )

    def set_position_in_tree(self, position_in_tree: Position) -> None:
        if isinstance(position_in_tree, Position):
            self._position_in_tree = position_in_tree
        else:
            raise Exception(
                "Error: impossible to set _position_in_tree for a " + type(self).__name__ + ":" +
                "\n_position_in_tree must be a Position, but a " + type(position_in_tree).__name__ + " is given."
            )

    ###############################################################
    ########################## GET_COLOR ##########################
    ###############################################################
    def get_color(self) -> Color:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Revoie la couleur de la case,
        # donc celle de l'arbre à la position_in_tree puisqu'il y a un arbre
        # =============================
        return self.get_tree().get_body().get_element(position=self.get_position_in_tree())
