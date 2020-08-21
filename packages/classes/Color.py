# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Color, une couleur au format rgb
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + get_color()
# + get_hexadecimal()
# + __str__()
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

        for color in (red, green, blue):
            if isinstance(color, int):
                if not (0 <= color <= 255):
                    raise Exception(
                        "Error: impossible to set an element for a " + type(self).__name__ + ":"
                        "\nan input's value is not between 0 and 255."
                    )
            else:
                raise Exception(
                    "Error: impossible to set an element for a " + type(self).__name__ + ":" +
                    "\nan input is a " + str(type(color)) + ", must be an int."
                )

        self.red = red
        self.green = green
        self.blue = blue

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
