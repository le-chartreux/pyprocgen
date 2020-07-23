# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Box, une case
# -----------------------------
# CONTENU :
# - __init__()
# - get_color(self) -> str
# ==========================================================

from packages.classes.Board import Board
from packages.classes.Biome import Biome
from packages.classes.Encyclopedia import Encyclopedia
from packages.classes.Position import Position
from packages.classes.Tree import Tree


class Box:

    def __init__(
        self,
        biome: Biome
    ):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Box (case), caractérisée par :
        # - son biome
        # =============================
        self.biome = biome

    def get_color(self) -> str:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Revoie la couleur de la case,
        # donc celle du sol puisque il n'y a pas d'arbre
        # =============================
        return self.biome.ground_color.get_rgb()
