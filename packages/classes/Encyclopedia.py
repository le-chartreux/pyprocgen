from packages.classes.Tree import Tree

##############################################################
####################### ENCYCLOPEDIA #########################
##############################################################


class Encyclopedia:

    def __init__(self, name: str, biomes: dict = {}):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Encyclopedia, caractérisé par :
        # - son nom
        # - les Biomes qu'il répertorie
        # -----------------------------
        # UTILISÉ PAR :
        # - procedural_generation_2D.py
        # - encyclopedia_functions.encyclopedia_creation()
        # =============================
        self.name = name
        self.biomes = biomes

    def get_trees(self) -> list:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie une liste de tous les arbres présents dans l'encyclopédie
        # -----------------------------
        # UTILISÉ PAR :
        # - .get_tree_info()
        # - .max_height_of_trees()
        # -----------------------------
        # DÉPEND DE :
        # - classes.Biome
        # - classes.Tree
        # =============================
        trees = []

        for biome in self.biomes.values():

            for tree in biome.trees:

                trees.append(tree)

        return trees

    def get_tree_info(self, tree_name: str) -> Tree:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie l'objet de l'arbre à partir de son nom
        # -----------------------------
        # UTILISÉ PAR :
        # - A COMPLETER
        # -----------------------------
        # DÉPEND DE :
        # - classes.Encyclopedia.get_trees()
        # - classes.Tree
        # =============================
        trees = self.get_trees()
        increment = 0

        while increment < len(trees) and trees[increment].name != tree_name:
            increment += 1

        if increment < len(trees):
            return trees[increment]

        else:
            return None

    def max_height_of_trees(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie la hauteur de l'arbre le plus haut de l'encyclopédie
        # -----------------------------
        # UTILISE PAR :
        # - procedural_generation_2D.py
        # -----------------------------
        # DEPEND DE :
        # - classes.Encyclopedia.get_trees()
        # - classes.Tree
        # =============================
        max_height = 0

        for tree in self.get_trees():

            if tree.get_height() > max_height:

                max_height = tree.get_height()

        return max_height
