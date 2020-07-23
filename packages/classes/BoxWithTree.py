# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe BoxWithTree, une case qui remplace Box
# quand cette dernière se fait poser un arbre dessus
# -----------------------------
# CONTENU :
# - __init__()
# - get_color(self) -> str
# ==========================================================

from packages.classes.Biome import Biome
from packages.classes.Box import Box
from packages.classes.Position import Position
from packages.classes.Tree import Tree


class BoxWithTree(Box):

    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Crée un objet BoxWithTree qui hérite de Box, caractérisée par :
    # - son biome
    # - l'arbre qui est dessus
    # - la position de son pixel d'arbre dans le modèle de l'arbre
    # =============================
    def __init__(self, biome: Biome, tree: Tree, position_in_tree: Position):
        super().__init__(biome)
        self.tree = tree
        self.position_in_tree = position_in_tree

    def get_color(self) -> str:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Revoie la couleur de la case,
        # donc celle de l'arbre à la postion_in_tree puisqu'il y a un arbre
        # =============================
        return self.tree.body.get_element_with_position(self.position_in_tree).get_rgb()
