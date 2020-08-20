# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Tree
# -----------------------------
# CONTENU :
# + __slots__
# + __init__()
# + GETTERS
# + SETTERS
# + get_height
# + get_width
# ==========================================================


from packages.classes.BoardColor import BoardColor


class Tree:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_name",
        "_spawn_probability",
        "_body"
    )

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, name: str, spawn_probability: int, body: BoardColor):
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
        # - dic_functions.dic_biomes_creation()
        # - classes.Encyclopedia.max_height_of_trees()
        # - trees_generation.possible_to_place_tree()
        # - trees_generation.put_tree()
        # =============================
        self._body = body
        self._name = name
        self._spawn_probability = spawn_probability

    ###############################################################
    ############################ GETTERS ##########################
    ###############################################################
    def get_body(self) -> BoardColor:
        return self._body

    def get_name(self) -> str:
        return self._name

    def get_spawn_probability(self) -> int:
        return self._spawn_probability

    ###############################################################
    ############################ SETTERS ##########################
    ###############################################################
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A COMPLETER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    ###############################################################
    ########################## GET_HEIGHT #########################
    ###############################################################
    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la hauteur de l'arbre
        # -----------------------------
        # UTILISÉ PAR :
        # - classes.Encyclopedia.max_height_of_trees()
        # - A COMPLETER
        # =============================
        return self.body.get_height()

    ###############################################################
    ########################## GET_WIDTH ##########################
    ###############################################################
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
        return self.body.get_width()
