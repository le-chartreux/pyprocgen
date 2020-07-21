from packages.classes.Encyclopedia import Encyclopedia
from packages.classes.Biome import Biome
from packages.classes.Tree import Tree
from packages.classes.Position import Position
from packages.classes.Board import Board

##############################################################
########################### BOX ##############################
##############################################################


class Box:

    def __init__(
        self,
        biome: Biome,
        tree: Tree = None,
        position_in_tree: Position = Position(-1, -1)
    ):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Box (case), caractérisée par :
        # - le nom de son biome
        # - le nom de l'arbre qui est dessus ("" si il n'y a pas d'arbre)
        # - la position de son pixel d'arbre dans le modèle de l'arbre en x
        # - la position de son pixel d'arbre dans le modèle de l'arbre en y
        # -----------------------------
        # UTILISÉ PAR :
        # - board_functions.display_board()
        # - decisional.genererate_box()
        # - image_creation.write_image_body()
        # - trees_generation.possible_to_place_tree()
        # - trees_generation.put_tree()
        # =============================

        self.biome = biome
        self.tree = tree
        self.position_in_tree = position_in_tree

    def get_color(self) -> str:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Revoie la couleur de la case
        # -----------------------------
        # UTILISÉ PAR :
        # - image_creation.write_image_body()
        # -----------------------------
        # DÉPEND DE :
        # - Encyclopedia
        # - Tree
        # =============================
        if self.tree == None:
            # ce n'est pas un arbre
            return self.biome.ground_color.get_rgb()
        else:
            # c'est un arbre
            print("Yaunarbre")
            return self.tree.body.get_element_with_position(self.position_in_tree).get_rgb()
