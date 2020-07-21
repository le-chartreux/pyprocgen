from packages.classes.Board import Board


class Tree:

    def __init__(self, name: str, spawn_probability: int, body: Board):
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
        # - classes.Encyclopedia.max_height_of_trees()
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
