# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Color, une couleur au format rgb
# -----------------------------
# CONTENU :
# - __slots__
# - HINTS
# - __init__()
# - GETTERS
# - SETTERS
# - get_color(self)
# ==========================================================


class Color:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "red",
        "green",
        "blue"
    )

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(self, red: int, green: int, blue: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Color, caractérisé par:
        # - red
        # - green
        # - blue
        # -----------------------------
        # PRÉCONDITION:
        # - 0 < (red, green & blue) < 255
        # =============================
        if Color.is_part_of_color(red) and Color.is_part_of_color(green) and Color.is_part_of_color(blue):
            self.red = red
            self.green = green
            self.blue = blue
        else:
            raise Exception(
                "Error: impossible to set element for a Color, inputs are " +
                str(red) + str(green) + str(blue) +
                ", they must be between 0 and 255."
            )

    ###############################################################
    ##################### IS_PART_OF_COLOR ########################
    ###############################################################
    @staticmethod
    def is_part_of_color(number: int) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Vérifie si number est un int et renvoi True si 0 < number < 255
        # =============================
        if isinstance(number, int):
            return 0 <= number <= 255
        else:
            raise Exception(
                "Error: impossible to set element for a Color, an input is a " +
                str(type(number)) +
                ", must be an int."
            )

    ###############################################################
    ###################### GET_HEXADECIMAL ########################
    ###############################################################
    def get_hexadecimal(self) -> str:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoi la couleur en hexadecimal
        # =============================
        return hex(self.red) + hex(self.green)[2:] + hex(self.blue)[2:]

    ###############################################################
    ########################### GET_RGB ###########################
    ###############################################################
    def get_rgb(self) -> str:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoi la couleur en rgb
        # =============================
        return str(self.red) + " " + str(self.green) + " " + str(self.blue)

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self):
        return self.get_rgb()

