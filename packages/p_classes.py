# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir les classes utilisées dans le programme
# -----------------------------
# CONTENU :
# - Box
# - Encyclopedia
# - Biome
# - Tree
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - p_board_functions.py
# - p_decisional.py
# - p_dic_creation.py
# - p_image_creation.py
# - p_decisional.py
# ==========================================================


##############################################################
########################### TREE #############################
##############################################################
class Tree:

    def __init__(self, name: str, spawn_probability: int, body: list):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet définissant un arbre de biome,
        # caractérisé par :
        # - son nom
        # - la probabilité d'être placé sur une case possible
        # - le body de sa représentation ppm avec None pour les pixels vides
        # -----------------------------
        # UTILISÉ PAR :
        # - p_dic_functions.dic_biomes_creation()
        # - p_classes.Encyclopedia.max_height_of_trees()
        # - p_trees_generation.possible_to_place_tree()
        # - p_trees_generation.put_tree()
        # =============================
        self.name = name
        self.spawn_probability = spawn_probability
        self.body = body

    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la hauteur de l'arbre
        # -----------------------------
        # UTILISÉ PAR :
        # - p_classes.Encyclopedia.max_height_of_trees()
        # - A COMPLETER
        # =============================
        return len(self.body)

    def get_width(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la largeur de l'arbre
        # -----------------------------
        # UTILISÉ PAR :
        # - A COMPLETER
        # =============================
        return len(self.body[0])


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
        # - p_encyclopedia_functions.encyclopedia_creation()
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
        # - p_classes.Biome
        # - p_classes.Tree
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
        # - p_classes.Encyclopedia.get_trees()
        # - p_classes.Tree
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
        # PRECONDITIONS :
        # - None
        # -----------------------------
        # DEPEND DE :
        # - p_classes.Encyclopedia.get_trees()
        # - p_classes.Tree
        # =============================
        max_height = 0

        for tree in self.get_trees():

            if tree.get_height() > max_height:

                max_height = tree.get_height()

        return max_height


###############################################################
############################ BIOME ############################
###############################################################
class Biome:

    def __init__(
        self,
        name: str,
        temperature_min: int,
        temperature_max: int,
        pluviometry_min: int,
        pluviometry_max: int,
        ground_color: str,
        trees: list
    ):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Biome, caractérisé par :
        # - son nom
        # - sa température minimale
        # - sa température maximale
        # - sa pluviometrie minimale
        # - sa pluviometrie maximale
        # - la couleur de son sol
        # - une liste des arbres qui y poussent
        # -----------------------------
        # UTILISE PAR :
        # - p_dic_creation.f_dic_biomes_creation()
        # - p_decisional.f_choice_biome()
        # =============================
        self.name = name

        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.pluviometry_min = pluviometry_min
        self.pluviometry_max = pluviometry_max

        self.ground_color = ground_color

        self.trees = trees

    def in_range(self, temperature: float, pluviometry: float) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie si la température et la pluviométrie
        # correspondent à celles de ce Biome
        # -----------------------------
        # UTILISE PAR :
        # - p_decisional.f_choice_biome()
        # =============================
        return (self.temperature_min <= temperature <= self.temperature_max
                and self.pluviometry_min <= pluviometry < self.pluviometry_max)


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
        # - p_board_functions.f_display_board()
        # - p_decisional.f_choix_biome()
        # - p_image_creation.f_image_creation()
        # - p_trees_creation.f_possible_to_place_tree
        # - p_trees_creation.f_put_tree()
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
        # - A COMPLETER
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
