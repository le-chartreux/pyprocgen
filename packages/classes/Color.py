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

from packages.constants import COLOR_RGB_MIN, COLOR_RGB_MAX


class Color:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_red",
        "_green",
        "_blue"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _red: int
    _green: int
    _blue: int

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
        # - COLOR_RGB_MIN <= (red, green & blue) <= COLOR_RGB_MAX
        # =============================
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_red(self) -> int:
        return self._red

    def get_green(self) -> int:
        return self._green

    def get_blue(self) -> int:
        return self._blue

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_red(self, red: int) -> None:
        if isinstance(red, int):
            if COLOR_RGB_MIN <= red <= COLOR_RGB_MAX:
                self._red = red
            else:
                raise Exception(
                    "Error: impossible to set _red for a " + type(self).__name__ + ":" +
                    "\n_red must be between " + str(COLOR_RGB_MIN) + " and " + str(COLOR_RGB_MAX) +
                    " but input's value equals " + str(red) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _red for a " + type(self).__name__ + ":" +
                "\n_red must be an int, but a " + str(type(red)) + " is given."
            )

    def set_green(self, green: int) -> None:
        if isinstance(green, int):
            if COLOR_RGB_MIN <= green <= COLOR_RGB_MAX:
                self._green = green
            else:
                raise Exception(
                    "Error: impossible to set _green for a " + type(self).__name__ + ":" +
                    "\n_green must be between " + str(COLOR_RGB_MIN) + " and " + str(COLOR_RGB_MAX) +
                    " but input's value equals " + str(green) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _green for a " + type(self).__name__ + ":" +
                "\n_green must be an int, but a " + str(type(green)) + " is given."
            )

    def set_blue(self, blue: int) -> None:
        if isinstance(blue, int):
            if COLOR_RGB_MIN <= blue <= COLOR_RGB_MAX:
                self._blue = blue
            else:
                raise Exception(
                    "Error: impossible to set _blue for a " + type(self).__name__ + ":" +
                    "\n_blue must be between " + str(COLOR_RGB_MIN) + " and " + str(COLOR_RGB_MAX) +
                    " but input's value equals " + str(blue) + "." +
                    "\nChange the relative constant in packages/constants.py to allow."
                )
        else:
            raise Exception(
                "Error: impossible to set _blue for a " + type(self).__name__ + ":" +
                "\n_blue must be an int, but a " + str(type(blue)) + " is given."
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
        return hex(self.get_red()) + hex(self.get_green())[2:] + hex(self.get_blue())[2:]  # [2:] pour enlever le 0x

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
        return str(self.get_red()) + " " + str(self.get_green()) + " " + str(self.get_blue())

    ###############################################################
    ########################### __STR__ ###########################
    ###############################################################
    def __str__(self):
        return self.get_rgb()
