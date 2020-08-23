# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Génère les arbres dans le plateau
# -----------------------------
# CONTENU :
# - generate_trees(board)
# - possible_to_place_tree(board, encyclopedia, x, y)
# - put_tree(board, encyclopedia, x, y)
# ==========================================================

import random

from packages.short_class_import import BoardBox, Box, BoxWithTree, Tree, Position


###############################################################
####################### GENERATE_TREES ########################
###############################################################
def generate_trees(board: BoardBox) -> None:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Place les arbres dans board (ne calcule que pour la moitié supérieure)
    # -----------------------------
    # PRECONDITIONS :
    # - encyclopedia a un dictionnaire de
    #   biomes comprend une liste d'au moins un arbre par biome
    # =============================
    width = board.get_width()
    # Car on ne traite que les arbres de la premiere partie :
    height = int(board.get_height() / 2)

    for line in range(height):

        for column in range(width):

            box = board.get_element(x=column, y=line)

            if box.get_biome().get_name() != "tree":

                # Creation d'une liste à ordre aléatoire des arbres possibles
                trees_list = box.get_biome().get_trees()
                random.shuffle(trees_list)

                # Essaye de placer un arbre en essayant tous les éléments de trees_list dans l'ordre jusqu'à en trouver
                # un qu'il est possible de placer ou arriver à la fin
                counter = 0
                placed = False

                while counter < len(trees_list) and not placed:

                    if (
                            possible_to_place_tree(
                                board=board,
                                tree=trees_list[counter],
                                x=column,
                                y=line
                            )
                            and random.random() < trees_list[counter].get_spawn_probability()
                    ):
                        put_tree(
                            board=board,
                            tree=trees_list[counter],
                            x=column,
                            y=line
                        )

                        placed = True

                    counter += 1


###############################################################
################### POSSIBLE_TO_PLACE_TREE ####################
###############################################################
def possible_to_place_tree(board: BoardBox, tree: Tree, x: int, y: int):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Renvoie si il est possible de placer l'arbre
    # -----------------------------
    # DEPEND DE :
    # - classes.Box
    # - classes.Tree
    # - random
    # -----------------------------
    # UTILISE PAR :
    # - trees_creation.generate_trees()
    # =============================

    if x >= board.get_width() or y >= board.get_height():
        print("Warning from trees_generation.possible_to_place_tree():")
        print("Attempting to look if a tree can be put outside the board.")
        return False

    type_of_source_box = board.get_element(x=x, y=y).get_biome().get_name()

    tree_height = tree.get_height()
    tree_width = tree.get_width()

    # Traitement des cas où l'arbre est en bordure d'image :
    # on coupe le modèle à la bordure (pour ne pas essayer d'accèder à une case en dehors du tableau)
    if y + tree_height > board.get_height():
        tree_height = board.get_height() - y

    if x + tree_width > board.get_width():
        tree_width = board.get_width() - x

    line = 0
    column = 0
    possible = True

    while line < tree_height and possible:

        while column < tree_width and possible:

            possible = (
                    board.get_element(x=(x + column), y=(y + line)).get_biome().get_name() == type_of_source_box and
                    not isinstance(board.get_element(x=(x + column), y=(y + line)), BoxWithTree)
            )

            column += 1

        line += 1
        column = 0

    return possible


###############################################################
######################### PUT_TREE ############################
###############################################################
def put_tree(board: BoardBox, tree: Tree, x: int, y: int):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Place un arbre depuis le point board[y][x]
    # =============================

    tree_height = tree.get_height()
    tree_width = tree.get_width()

    # Traitement des cas où l'arbre est en bordure d'image :
    # on coupe le modèle à la bordure (pour ne pas essayer d'accèder à une case en dehors du tableau)

    if y + tree_height > board.get_height():
        tree_height = board.get_height() - y

    if x + tree_width > board.get_width():
        tree_width = board.get_width() - x

    # Placement de l'arbre
    for line in range(tree_height):

        for column in range(tree_width):

            if tree.get_body().get_element(x=column, y=line) is not None:

                old_box = board.get_element(x=(x + column), y=(y + line))
                new_box = BoxWithTree(
                    biome=old_box.get_biome(),
                    tree=tree,
                    position_in_tree=Position(x=column, y=line)
                )
                board.set_element(value=new_box, x=(x + column), y=(y + line))
