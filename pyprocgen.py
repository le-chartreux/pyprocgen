# ==========================================================
# INFORMATIONS :
# -----------------------------
# UTILITÉ :
# Corps du programme de génération
# procédurale de carte en 2D
# -----------------------------
# DÉPEND DE :
# - les packages appelés
# -----------------------------
# UTILISÉ PAR :
# - None
# ==========================================================

import time
import sys
from packages.board_functions import generate_seed, create_empty_board, seed_to_string, string_to_seed, is_seed
from packages.decisional import genererate_box
from packages.encyclopedia_functions import encyclopedia_creation
from packages.image_creation import write_image_header, write_image_body
from packages.trees_generation import generate_trees
from packages.utilities import is_integer, is_float, print_progress


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

    if width != None:
        print("  Enter an integer.")

    width = input("  Width : ")

width = int(width)

# Pour la hauteur :
height = None
while not is_integer(height):

    if height != None:
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
        while not is_seed(seed_in_string):

            if seed_in_string != "":
                print("  This is not a seed.")

            seed_in_string = input("  Enter the seed : ")

        seed = string_to_seed(seed_in_string)

    else:
        seed = generate_seed()

    print("")

    # ... de l'intensité de la variation
    choice = input(
        "- Do you want to change the intensity of the variation between two boxes ? (y / N) : ")

    if choice == "y" or choice == "Y":
        print("Tip : enter a number between 0.1 and 10, 1 is the basic choice.")
        variation_intensity = None
        while not is_float(variation_intensity):
            variation_intensity = float(input("My choice : "))
    else:
        variation_intensity = 1.0

    print("")

    # ... de la présence d'arbres
    choice = input("- Do you want trees on the map ? (Y / n) : ")
    place_trees = (choice != "n" and choice != "N")

    print("")

###############################################################
######################## MODE BASIQUE #########################
###############################################################
else:

    seed = generate_seed()
    variation_intensity = 1.0
    place_trees = True


###############################################################
######################### CONSTANTES ##########################
###############################################################
begin_time = time.time()
print_progress_opt = ("idlelib" not in sys.modules)
print("Seed of the map : " + seed_to_string(seed) + "\n")
encyclopedia = encyclopedia_creation()

###############################################################
############### CRÉATION DU HEADER DE L'IMAGE #################
###############################################################
destination_file = open("generated_map.ppm", "w")
write_image_header(destination_file, height, width, seed_to_string(seed))


###############################################################
############### CRÉATION DE L'IMAGE AVEC ARBRES ###############
###############################################################
if place_trees:

    chunk_height = encyclopedia.max_height_of_trees()

    # Création du chunk initial
    # L'image se crée par chunk de width*chunk_height
    # pour économiser la RAM
    actual_chunk = create_empty_board(width, chunk_height)

    for line_number in range(chunk_height):

        for column_number in range(width):

            actual_chunk[line_number][column_number] = genererate_box(
                encyclopedia, column_number, line_number, seed, variation_intensity)

    # Création des chunks intermédiaires
    for chunk_number in range(int(height / chunk_height)):

        chunk_number += 1

        next_chunk = create_empty_board(width, chunk_height)

        for line_number in range(chunk_height):

            for column_number in range(width):

                next_chunk[line_number][column_number] = genererate_box(
                    encyclopedia,
                    column_number,
                    chunk_number * chunk_height + line_number,
                    seed,
                    variation_intensity
                )

        chunk_amalgamation = actual_chunk + next_chunk

        generate_trees(chunk_amalgamation, encyclopedia)

        actual_chunk = chunk_amalgamation[:chunk_height]

        write_image_body(destination_file, actual_chunk, encyclopedia)

        actual_chunk = chunk_amalgamation[chunk_height:]

        if print_progress_opt:
            print_progress("Creation of the map :        ",
                           ((chunk_number + 1) * chunk_height) / height)

        chunk_number -= 1

    # Création du dernier chunk
    last_chunk = actual_chunk[0:(height % chunk_height)]

    write_image_body(destination_file, last_chunk, encyclopedia)

    if print_progress_opt:
        print_progress("Creation of the map :        ", 1.0)


###############################################################
############### CRÉATION DE L'IMAGE SANS ARBRES ###############
###############################################################
else:

    for line_number in range(height):    # L'image se crée ligne par ligne

        chunk = create_empty_board(width, 1)

        for column_number in range(width):

            chunk[0][column_number] = genererate_box(
                encyclopedia, column_number, line_number, seed, variation_intensity)

        write_image_body(destination_file, chunk, encyclopedia)

        if print_progress_opt:
            print_progress(
                "Creation of the map :        ", (line_number + 1) / height)


###############################################################
################ AFFICHAGE DES MESSAGES DE FIN ################
###############################################################
destination_file.close()
print("")
print("Done")
print("Execution time : ", time.time() - begin_time)
