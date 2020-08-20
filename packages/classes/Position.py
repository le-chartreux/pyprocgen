# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Position,
# dont les objets définissent une position en 2D
# -----------------------------
# CONTENU :
# - __init__()
# ==========================================================


class Position:

    def __init__(self, x: int, y: int):
        if isinstance(x, int):
            self.x = x
        else:
            raise Exception(
                "Error: Impossible to set x for a " + type(self).__name__ + ":" +
                "\nx is an int, but a " + type(x).__name__ + " is given."
            )
        if isinstance(y, int):
            self.y = y
        else:
            raise Exception(
                "Error: Impossible to set y for a " + type(self).__name__ + ":" +
                "\ny is an int, but a " + type(y).__name__ + " is given."
            )