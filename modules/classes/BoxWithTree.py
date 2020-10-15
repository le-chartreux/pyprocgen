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

from modules.classes.Biome import Biome
from modules.classes.Box import Box
from modules.classes.Color import Color
from modules.classes.Position import Position
from modules.classes.Tree import Tree

from modules.settings import DEBUG_MOD
from modules.utilities import check_attribute_type_set


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
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=tree,
                type_to_check=Tree,
                name_of_attribute_to_check="_tree",
                object_destination=self
            )
        self._tree = tree

    def set_position_in_tree(self, position_in_tree: Position) -> None:
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=position_in_tree,
                type_to_check=Position,
                name_of_attribute_to_check="_position_in_tree",
                object_destination=self
            )
        self._position_in_tree = position_in_tree

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
