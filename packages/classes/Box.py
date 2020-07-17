from packages.classes.Encyclopedia import Encyclopedia

##############################################################
########################### BOX ##############################
##############################################################


class Box:

    def __init__(self, biome_name: str, tree_name: str = "", position_in_tree_x: int = -1, position_in_tree_y: int = -1):
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

        self.biome_name = biome_name
        self.tree_name = tree_name
        self.position_in_tree_x = position_in_tree_x
        self.position_in_tree_y = position_in_tree_y

    def get_color(self, encyclopedia: Encyclopedia) -> str:
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
        if self.tree_name == "":
            # ce n'est pas un arbre
            return encyclopedia.biomes[self.biome_name].ground_color
        else:
            # c'est un arbre
            return encyclopedia.get_tree_info(self.tree_name).body[self.position_in_tree_y][self.position_in_tree_x]
