# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Gérer l'évolution du terrain et
# prendre la décision du type de case à placer en (y, x)
# -----------------------------
# CONTENU :
# - generate_box()
# - choice_biome()
# ==========================================================

from packages.short_class_import import Box, Biome, Encyclopedia, Seed
from packages.perlin_noise import SimplexNoise

from packages.settings import (
    BIOME_PLUVIOMETRY_MAX,
    BIOME_TEMPERATURE_MAX,
    DECISIONAL_NUMBER_OF_ITERATIONS_NOISE,
    DECISIONAL_DISTANCE_BETWEEN_NOISES,
    DECISIONAL_VARIATION_INTENSITY
)


###############################################################
######################## GENERATE_BOX #########################
###############################################################
def generate_box(encyclopedia: Encyclopedia, x: int, y: int, seed: Seed) -> Box:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Génère une case en pour la case en (y, x)
    # =============================

    # Calcul de la température et de la pluviométrie de la case avec le bruit de Perlin
    noise = SimplexNoise()

    temperature = 0
    pluviometry = 0

    for i in range(1, DECISIONAL_NUMBER_OF_ITERATIONS_NOISE):
        power = 2 ** i

        temperature += noise.noise2(
            seed.get_temperature_x() +
            DECISIONAL_DISTANCE_BETWEEN_NOISES * i +
            x / (DECISIONAL_VARIATION_INTENSITY * power),

            seed.get_temperature_y() +
            DECISIONAL_DISTANCE_BETWEEN_NOISES * i +
            y / (DECISIONAL_VARIATION_INTENSITY * power)
        ) * power

        pluviometry += noise.noise2(
            seed.get_pluviometry_x() +
            DECISIONAL_DISTANCE_BETWEEN_NOISES * i +
            x / (DECISIONAL_VARIATION_INTENSITY * power),

            seed.get_pluviometry_y() +
            DECISIONAL_DISTANCE_BETWEEN_NOISES * i +
            y / (DECISIONAL_VARIATION_INTENSITY * power)
        ) * power

    temperature = temperature * BIOME_TEMPERATURE_MAX / (2**DECISIONAL_NUMBER_OF_ITERATIONS_NOISE - 1)
    pluviometry = pluviometry * BIOME_PLUVIOMETRY_MAX / (2**DECISIONAL_NUMBER_OF_ITERATIONS_NOISE - 1)

    # Génération
    return Box(biome_choice(encyclopedia, temperature, pluviometry))


###############################################################
######################## CHOICE_BIOME #########################
###############################################################
def biome_choice(encyclopedia: Encyclopedia, temperature: float, pluviometry: float) -> Biome:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Renvoie le nom du biome qui a les caractéristiques de température
    # et de pluviométrie correspondantes parmi ceux de l'encyclopédie
    # =============================

    for biome in encyclopedia.get_biomes().values():

        if biome.in_range(temperature, pluviometry):
            return biome

    return encyclopedia.get_biome("water")
