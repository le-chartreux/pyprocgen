# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Créer une image à partir d'un tableau de Biomes
# -----------------------------
# CONTENU :
# - write_image_header(destination_file, height, width, seed)
# - write_image_body(v_plateau)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# ==========================================================

import os
from .p_classes import Box, Encyclopedia
from .p_utilities import print_progression


###############################################################
##################### WRITE_IMAGE_HEADER ######################
###############################################################
def write_image_header(destination_file, height: int, width: int, seed: str):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Écrit le header de destination_file
    # selon le modèle d'un header de fichier ppm.
    # Si Generated_map.ppm existe déjà, il est
    # supprimé, sinon il est créé.
    # -----------------------------
    # DEPEND DE :
    # - os
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
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

def write_image_body(destination_file, board: list, encyclopedia: Encyclopedia):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Place à la suite de destination_file la couleur
    # de chaque case de board
    # -----------------------------
    # DEPEND DE :
    # - os
    # - p_classes.Box
    # - p_classes.Encyclopedia
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================

    for line in range(len(board)):

        for column in range(len(board[0])):

            color = board[line][column].get_color(encyclopedia)
            if color == None:
                color = "0 0 0"
            destination_file.write(
                color
            )
            destination_file.write(" ")

        destination_file.write("\n")
