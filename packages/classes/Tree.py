# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Tree
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
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
    ############################ HINTS ############################
    ###############################################################
    _body: BoardColor
    _name: str
    _spawn_probability: float

    ###############################################################
    ########################### __INIT__ ##########################
    ###############################################################
    def __init__(self, name: str, spawn_probability: float, body: BoardColor):
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
        # PRÉCONDITION :
        # - 0 <= spawn_probability <= 1
        # =============================
        self.set_body(body)
        self.set_name(name)
        self.set_spawn_probability(spawn_probability)

    ###############################################################
    ############################ GETTERS ##########################
    ###############################################################
    def get_body(self) -> BoardColor:
        return self._body

    def get_name(self) -> str:
        return self._name

    def get_spawn_probability(self) -> float:
        return self._spawn_probability

    ###############################################################
    ############################ SETTERS ##########################
    ###############################################################
    def set_body(self, body: BoardColor) -> None:
        if isinstance(body, BoardColor):
            self._body = body
        else:
            raise Exception(
                "Error: impossible to set _body for a " + type(self).__name__ + ":" +
                "\n_body must be a BoardColor, but a " + type(body).__name__ + " is given."
            )

    def set_name(self, name: str) -> None:
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception(
                "Error: impossible to set _name for a " + type(self).__name__ + ":" +
                "\n_name must be a str, but a " + type(name).__name__ + " is given."
            )

    def set_spawn_probability(self, spawn_probability: float) -> None:
        if isinstance(spawn_probability, float):
            if 0.0 <= spawn_probability <= 1.0:
                self._spawn_probability = spawn_probability
            else:
                raise Exception(
                    "Error: impossible to set _spawn_probability for a " + type(self).__name__ + ":" +
                    "\n_spawn_probability must be an int between 0 and 1, but input's value equals "
                    + str(spawn_probability) + "."
                )
        else:
            raise Exception(
                "Error: impossible to set _spawn_probability for a " + type(self).__name__ + ":" +
                "\n_spawn_probability must be an int between 0 and 1, but a " + type(spawn_probability).__name__ +
                " is given."
            )

    ###############################################################
    ########################## GET_HEIGHT #########################
    ###############################################################
    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la hauteur de l'arbre
        # =============================
        return self.get_body().get_height()

    ###############################################################
    ########################## GET_WIDTH ##########################
    ###############################################################
    def get_width(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la largeur de l'arbre
        # =============================
        return self.get_body().get_width()
