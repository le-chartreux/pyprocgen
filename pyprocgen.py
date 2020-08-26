# ==========================================================
# INFORMATIONS :
# -----------------------------
# UTILITÉ :
# Corps du programme de génération
# procédurale de carte en 2D
# ==========================================================

import time
import sys

from packages.short_class_import import BoardBox, Seed

from packages.decisional import generate_box
from packages.encyclopedia_functions import encyclopedia_creation
from packages.image_creation import write_image_header, write_image_body
from packages.trees_generation import generate_trees
from packages.utilities import is_integer, print_progress


###############################################################
################## CHOIX DE L'UTILISATEUR #####################
###############################################################
print("Hello, welcome to pyprocgen, a 2D procedural map generator. \n")


# ... de la taille de la map :
print("- Enter the map's dimensions :")
print("  Tip : enter integers between 100 and 5000")

# Pour la largeur :
width = None
while not is_integer(width):

    if width is not None:
        print("  Enter an integer.")

    width = input("  Width : ")

width = int(width)

# Pour la hauteur :
height = None
while not is_integer(height):

    if height is not None:
        print("  Enter an integer.")

    height = input("  Height : ")

height = int(height)

print("")


# ... du mode d'utilisation
advanced_mode = input("- Do you want to use advanced mode ? (y - N) : ")
print("")

###############################################################
######################## MODE AVANCÉ ##########################
###############################################################
if advanced_mode == "y" or advanced_mode == "Y":

    # ... du seed
    choice = input("- Do you want to enter a seed ? (y / N) : ")

    if choice == "y" or choice == "Y":
        print("  Tip : a seed looks like a:b:c:d where a,b,c,d are integers")

        seed_in_string = ""
        while not Seed.is_seed(seed_in_string):

            if seed_in_string != "":
                print("  This is not a seed.")

            seed_in_string = input("  Enter the seed : ")

        seed = Seed(seed_in_string=seed_in_string)

    else:
        seed = Seed()

    print("")

    # ... de la présence d'arbres
    choice = input("- Do you want trees on the map ? (Y / n) : ")
    place_trees = (choice != "n" and choice != "N")

    print("")

###############################################################
######################## MODE BASIQUE #########################
###############################################################
else:

    seed = Seed()
    place_trees = True


###############################################################
######################### CONSTANTES ##########################
###############################################################
begin_time = time.time()
print_progress_opt = ("idlelib" not in sys.modules)
print("Seed of the map : " + str(seed) + "\n")
encyclopedia = encyclopedia_creation()

###############################################################
############### CRÉATION DU HEADER DE L'IMAGE #################
###############################################################
destination_file = open("generated_map.ppm", "w")
write_image_header(destination_file, height, width, str(seed))


###############################################################
############### CRÉATION DE L'IMAGE AVEC ARBRES ###############
###############################################################
if place_trees:

    chunk_height = encyclopedia.get_max_height_of_trees()

    # Création du chunk initial
    # L'image se crée par chunk de width*chunk_height
    # pour économiser la RAM
    actual_chunk = BoardBox.create_empty_board(width=width, height=chunk_height)

    for line_number in range(chunk_height):

        for column_number in range(width):

            actual_chunk.set_element(
                value=generate_box(
                    encyclopedia=encyclopedia,
                    x=column_number,
                    y=line_number,
                    seed=seed
                ),
                x=column_number,
                y=line_number
            )

    # Création des chunks intermédiaires
    for chunk_number in range(int(height / chunk_height)):

        chunk_number += 1

        next_chunk = BoardBox.create_empty_board(width=width, height=chunk_height)

        for line_number in range(chunk_height):

            for column_number in range(width):

                next_chunk.set_element(
                    value=generate_box(
                        encyclopedia=encyclopedia,
                        x=column_number,
                        y=line_number + chunk_number*chunk_height,
                        seed=seed
                    ),
                    x=column_number,
                    y=line_number
                )

        chunk_amalgamation = BoardBox(actual_chunk.get_elements() + next_chunk.get_elements())

        generate_trees(chunk_amalgamation)

        actual_chunk = BoardBox(chunk_amalgamation.get_elements()[:chunk_height])

        write_image_body(destination_file, actual_chunk)

        actual_chunk = BoardBox(chunk_amalgamation.get_elements()[chunk_height:])

        if print_progress_opt:
            print_progress(
                text="Creation of the map : ",
                progression=((chunk_number + 1) * chunk_height) / height
            )

        chunk_number -= 1

    # Création du dernier chunk
    last_chunk = BoardBox(actual_chunk.get_elements()[0:(height % chunk_height)])

    write_image_body(destination_file, last_chunk)

    if print_progress_opt:
        print_progress("Creation of the map : ", 1.0)


###############################################################
############### CRÉATION DE L'IMAGE SANS ARBRES ###############
###############################################################
else:

    for line_number in range(height):    # L'image se crée ligne par ligne

        chunk = BoardBox.create_empty_board(width, 1)

        for column_number in range(width):

            chunk.set_element(
                value=generate_box(
                    encyclopedia,
                    column_number,
                    line_number,
                    seed
                ),
                x=column_number,
                y=0
            )

        write_image_body(destination_file, chunk)

        if print_progress_opt:
            print_progress(
                "Creation of the map : ", (line_number + 1) / height)


###############################################################
################ AFFICHAGE DES MESSAGES DE FIN ################
###############################################################
destination_file.close()
print("")
print("Done")
print("Execution time : ", time.time() - begin_time)
