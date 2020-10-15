# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Créer une image à partir d'un tableau de Biomes
# -----------------------------
# CONTENU :
# - write_image_header(destination_file, height, width, seed)
# - write_image_body(board)
# ==========================================================

from typing import TextIO

from modules.short_class_import import BoardBox


###############################################################
##################### WRITE_IMAGE_HEADER ######################
###############################################################
def write_image_header(destination_file: TextIO, height: int, width: int, seed: str):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Écrit le header de destination_file
    # selon le modèle d'un header de fichier ppm.
    # -----------------------------
    # DEPEND DE :
    # - os
    # =============================

    destination_file.write("P3\n")
    destination_file.write("# Seed : " + seed + "\n")
    destination_file.write(str(width))
    destination_file.write("\n")
    destination_file.write(str(height))
    destination_file.write("\n")
    destination_file.write("255\n")
    destination_file.write("\n")


###############################################################
####################### WRITE_IMAGE_BODY ######################
###############################################################

def write_image_body(destination_file: TextIO, board: BoardBox):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Place à la suite de destination_file la couleur
    # de chaque case de board
    # =============================

    for line in range(board.get_height()):

        for column in range(board.get_width()):
            color = board.get_element(x=column, y=line).get_color().get_rgb()
            destination_file.write(color)
            destination_file.write(" ")

        destination_file.write("\n")
