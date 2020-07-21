# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Gérer l'évolution du terrain et
# prendre la décision du type de case à placer en (y, x)
# -----------------------------
# CONTENU :
# - genererate_box(encyclopedia, x, y, seed, variation_intensity)
# - choice_biome(encyclopedia, temperature, pluviometry)
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# ==========================================================

from packages.short_class_import import Encyclopedia, Box
from packages.perlin_noise import SimplexNoise


###############################################################
######################## GENERATE_BOX #########################
###############################################################
def genererate_box(encyclopedia: Encyclopedia, x: int, y: int, seed: dict, variation_intensity: float) -> Box:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Génère une case en pour la case en (y, x)
    # -----------------------------
    # PRECONDITIONS :
    # - seed["Tx"], seed["Ty"] : integers not null
    # - seed["Px"], seed["Py"] : integers not null
    # -----------------------------
    # DEPEND DE :
    # - perlin_noise.py
    # - decisional.choice_biome()
    # -----------------------------
    # UTILISE PAR :
    # - procedural_generation_2D.py
    # =============================

    # Calcul de la température et de la pluviométrie de la case avec le bruit de perlin
    noise = SimplexNoise()

    temperature = 0
    pluviometry = 0

    for i in range(1, 9):

        power = 2**i

        temperature += noise.noise2(
            seed["Tx"] + 100000*i + x / (variation_intensity * power),
            seed["Ty"] + 100000*i + y / (variation_intensity * power)
        ) * power

        pluviometry += noise.noise2(
            seed["Px"] + 100000*i + x / (variation_intensity * power),
            seed["Py"] + 100000*i + y / (variation_intensity * power)
        ) * power

    temperature *= 0.00587    # temperature = temperature * 3 / (2**9 - 1)
    pluviometry *= 0.00783    # pluviometry = pluviometry * 4 / (2**9 - 1)

    # Génération
    return Box(biome_choice(encyclopedia, temperature, pluviometry))


###############################################################
######################## CHOICE_BIOME #########################
###############################################################
def biome_choice(encyclopedia: Encyclopedia, temperature: float, pluviometry: float) -> str:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Renvoie le nom du biome qui a les caracteristiques de température
    # et de pluviométrie correspondantes parmis ceux de l'encyclopédie
    # -----------------------------
    # DEPEND DE :
    # - classes.biome
    # - classes.encyclopedia
    # -----------------------------
    # UTILISÉ PAR :
    # - decisional.generate_box()
    # =============================

    for biome in encyclopedia.biomes.values():

        if biome.in_range(temperature, pluviometry):

            return biome

    return encyclopedia.biomes.get("water")
