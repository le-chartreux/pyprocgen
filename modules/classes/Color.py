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

from modules.settings import DEBUG_MOD, COLOR_RGB_MIN, COLOR_RGB_MAX
from modules.utilities import check_attribute_type_set, check_number_between_to_set


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
        # Crée un objet Color, caractérisé par :
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
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=red,
                type_to_check=int,
                name_of_attribute_to_check="_red",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=red,
                min_value=COLOR_RGB_MIN,
                max_value=COLOR_RGB_MAX,
                name_of_attribute_to_check="_red",
                object_to_set=self
            )
        self._red = red

    def set_green(self, green: int) -> None:
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=green,
                type_to_check=int,
                name_of_attribute_to_check="_green",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=green,
                min_value=COLOR_RGB_MIN,
                max_value=COLOR_RGB_MAX,
                name_of_attribute_to_check="_green",
                object_to_set=self
            )
        self._green = green

    def set_blue(self, blue: int) -> None:
        if DEBUG_MOD:
            check_attribute_type_set(
                attribute_to_check=blue,
                type_to_check=int,
                name_of_attribute_to_check="_blue",
                object_destination=self
            )
            check_number_between_to_set(
                number_to_check=blue,
                min_value=COLOR_RGB_MIN,
                max_value=COLOR_RGB_MAX,
                name_of_attribute_to_check="_blue",
                object_to_set=self
            )
        self._blue = blue

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
