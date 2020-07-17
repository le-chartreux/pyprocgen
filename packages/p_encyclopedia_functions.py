# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Créer le dictionnaire biomes_dict
# -----------------------------
# CONTENU :
# - add_in_dict(dict, class)
# - biomes_dict_creation()
# -----------------------------
# PROGRAMMES UTILISATEURS :
# - procedural_generation_2D.py
# ==========================================================

from .p_classes import Biome, Tree, Encyclopedia

###############################################################
######################### add_in_dict #########################
###############################################################


def add_in_dict(biomes_dict: dict, biome: Biome):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Ajoute biome dans le dictionnaire biomes_dict avec
    # biome.name comme référence
    # -----------------------------
    # DÉPEND DE :
    # - p_classes.Biome
    # -----------------------------
    # UTILISÉ PAR :
    # - p_encyclopedia_functions.encyclopedia_creation()
    # =============================

    biomes_dict[biome.name] = biome


###############################################################
################### ENCYCLOPEDIA_CREATION #####################
###############################################################
def encyclopedia_creation() -> Encyclopedia:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Remplie le dictionnaire de l'encyclopédie puis la crée
    # -----------------------------
    # DÉPEND DE :
    # - p_encyclopedia_functions.add_in_dict()
    # - p_classes.Encyclopedia
    # - p_classes.Biome
    # - p_classes.Tree
    # -----------------------------
    # UTILISÉ PAR :
    # - procedural_generation_2D.py
    # =============================

    dict_biomes = {}

    empty_tree = Tree(
        name="empty_tree",
        spawn_probability=0,
        body=[
            []
        ]
    )

    ###############################################################
    ########################## DESERT #############################
    ###############################################################

    ########################### ARBRES ############################

    desert_tree_1 = Tree(
        name="desert_tree_1",
        spawn_probability=0.005,
        body=[
            [None,          "106 82 18",   None,
                None,          "106 82 18"],

            ["106 82 18",   "142 93 60",   None,          "127 85 63",   None],

            [None,          None,          "142 93 60",
                "142 93 60",   "106 82 18"],

            [None,          "106 82 18",   "142 93 60",   None,          None],

            [None,          None,          "142 93 60",   None,          None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="desert_cool",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=-4,
            pluviometry_max=-3,

            ground_color="193 165 133",

            trees=[
                desert_tree_1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="desert_tropical",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=-4,
            pluviometry_max=-3,

            ground_color="247 210 165",

            trees=[
                desert_tree_1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="desert_warm",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=-4,
            pluviometry_max=-3,

            ground_color="207 151 100",

            trees=[
                desert_tree_1
            ]
        )
    )

    ###############################################################
    ######################## DESERT_SCUB ##########################
    ###############################################################

    ########################### ARBRES ############################
    desert_scub_tree_1 = Tree(
        name="desert_scub_tree_1",
        spawn_probability=0.007,
        body=[
            ["156 152 107", "156 152 107", None],

            ["156 152 107", "118 115 98",  "156 152 107"],

            [None,          "118 115 98",  None]
        ]
    )

    desert_scub_tree_2 = Tree(
        name="desert_scub_tree_2",
        spawn_probability=0.015,
        body=[
            [None,          "156 152 107", None],

            ["156 152 107", "118 115 98",  "156 152 107"],

            [None,          "118 115 98",  None]
        ]
    )

    desert_scub_bush_1 = Tree(
        name="desert_scub_bush_1",
        spawn_probability=0.005,
        body=[
            ["118 115 98"]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="desert_scub_cool",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=-3,
            pluviometry_max=-2,

            ground_color="187 158 126",

            trees=[
                desert_scub_tree_1,
                desert_scub_tree_2,
                desert_scub_bush_1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="desert_scub_tropical",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=-3,
            pluviometry_max=-2,

            ground_color="251 224 181",

            trees=[
                desert_scub_tree_1,
                desert_scub_tree_2,
                desert_scub_bush_1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="desert_scub_warm",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=-3,
            pluviometry_max=-2,

            ground_color="193 161 122",

            trees=[
                desert_scub_tree_1,
                desert_scub_tree_2,
                desert_scub_bush_1
            ]
        )
    )

    ###############################################################
    ######################### DRY_FOREST ##########################
    ###############################################################

    ########################### ARBRES ############################

    dry_forest_tree_1 = Tree(
        name="dry_forest_tree_1",
        spawn_probability=0.015,
        body=[
            [None,          None,          "121 105 56",
                None,          None,          None,          None],

            [None,          None,          None,          "133 103 69",
                None,          "133 103 69",  "121 105 56"],

            ["121 105 56",  "133 103 69",  "133 103 69",
                "133 103 69",  "133 103 69",  None,          None],

            [None,          "121 105 56",  None,
                "133 103 69",  None,          None,          None],

            [None,          None,          None,
                "133 103 69",  None,          None,          None],

            [None,          None,          None,
                "133 103 69",  None,          None,          None]
        ]
    )

    dry_forest_tree_2 = Tree(
        name="dry_forest_tree_2",
        spawn_probability=0.01,
        body=[
            [None,          "121 105 56",  None,
                "133 103 69",  "121 105 56"],

            ["121 105 56",  "133 103 69",  None,          "133 103 69",  None],

            [None,          None,          "133 103 69",  None,          None],

            [None,          None,          "133 103 69",  None,          None]
        ]
    )

    dry_forest_tree_3 = Tree(
        name="dry_forest_tree_3",
        spawn_probability=0.005,
        body=[
            [None,          None,          None,          "121 105 56",  None],

            ["121 105 56",  None,          None,
                "133 103 69",  "121 105 56"],

            [None,          "133 103 69",  "133 103 69",  "133 103 69",  None],

            [None,          None,          "133 103 69",  None,          None],

            [None,          None,          "133 103 69",  None,          None],

            [None,          None,          "133 103 69",  None,          None]
        ]
    )

    dry_forest_bush_1 = Tree(
        name="dry_forest_bush_1",
        spawn_probability=0.0005,
        body=[
            ["121 105 56"]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="dry_forest_tropical",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=0,
            pluviometry_max=1,

            ground_color="177 148 108",

            trees=[
                dry_forest_tree_1,
                dry_forest_tree_2,
                dry_forest_tree_3,
                dry_forest_bush_1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="dry_forest_warm",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=-1,
            pluviometry_max=0,
            ground_color="167 138 104",

            trees=[
                dry_forest_tree_1,
                dry_forest_tree_2,
                dry_forest_tree_3,
                dry_forest_bush_1
            ]

        )
    )

    ###############################################################
    ######################## MOIST_FOREST #########################
    ###############################################################

    ########################### ARBRES ############################

    moist_forest_tree_1 = Tree(
        name="moist_forest_tree_1",
        spawn_probability=0.1,
        body=[
            [None,          "54 62 15",    "34 46 10",    "34 46 10",    None],

            ["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    None],

            ["34 46 10",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"],

            [None,          None,          "58 45 26",    None,          None],

            [None,          None,          "58 45 26",    None,          None]
        ]
    )

    moist_forest_tree_2 = Tree(
        name="moist_forest_tree_2",
        spawn_probability=0.05,
        body=[
            [None,          "34 46 10",    "34 46 10",    "34 46 10",    None],

            ["65 71 23",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"],

            [None,          "34 46 10",    "34 46 10",    "34 46 10",    None],

            [None,          "34 46 10",    "58 45 26",    "34 46 10",    None],

            [None,          None,          "58 45 26",    None,          None],

            [None,          None,          "58 45 26",    None,          None],

            [None,          None,          "58 45 26",    None,          None]
        ]
    )

    moist_forest_tree_3 = Tree(
        name="moist_forest_tree_3",
        spawn_probability=0.07,
        body=[
            [None,          "54 62 15",    None],

            ["34 46 10",    "34 46 10",    "34 46 10"],

            ["34 46 10",    "34 46 10",    "34 46 10"],

            [None,          "58 45 26",    None],

            [None,          "58 45 26",    None]
        ]
    )

    moist_forest_tree_4 = Tree(
        name="arbre_moist_forest_4",
        spawn_probability=0.01,
        body=[
            [None,          None,          "36 49 11",
                "34 46 10",    None,          None],

            ["65 71 23",    "34 46 10",    "34 46 10",
                "54 62 15",    "34 46 10",    None],

            ["34 46 10",    "59 58 12",    "34 46 10",
                "34 46 10",    "34 46 10",    "34 46 10"],

            [None,          "48 57 13",    "58 45 26",
                "58 45 26",    "34 46 10",    "54 62 15"],

            [None,          None,          None,
                "58 45 26",    None,          None],

            [None,          None,          None,
                "58 45 26",    None,          None]
        ]
    )

    moist_forest_tree_5 = Tree(
        name="arbre_moist_forest_5",
        spawn_probability=0.015,
        body=[
            [None,          "59 72 30",    None],

            ["44 57 18",    "34 46 10",    "51 65 23"],

            ["46 59 19",    "58 45 26",    "42 54 16"],

            [None,          "58 45 26",    None]
        ]
    )

    moist_forest_tree_6 = Tree(
        name="moist_forest_tree_6",
        spawn_probability=0.005,
        body=[
            [None,          "65 71 23",    None,          None,          None],

            ["54 62 15",    "34 46 10",    "34 46 10",    "34 46 10",    "54 62 15"],

            ["34 46 10",    "34 46 10",    "34 46 10",    "34 46 10",    "34 46 10"],

            ["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"],

            ["34 46 10",    "34 46 10",    "58 45 26",    "34 46 10",    "34 46 10"],

            [None,          None,          "58 45 26",    None,          None],

            [None,          None,          "58 45 26",    None,          None]
        ]
    )

    moist_forest_bush_1 = Tree(
        name="moist_forest_bush_1",
        spawn_probability=0.0005,
        body=[
            ["109 153 97"]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="moist_forest_cool",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=-1,
            pluviometry_max=0,

            ground_color="78 105 36",

            trees=[
                moist_forest_tree_1,
                moist_forest_tree_2,
                moist_forest_tree_3,
                moist_forest_tree_4,
                moist_forest_tree_5,
                moist_forest_tree_6,
                moist_forest_bush_1
            ]

        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="moist_forest_tropical",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=1,
            pluviometry_max=2,

            ground_color="93 84 51",

            trees=[
                moist_forest_tree_1,
                moist_forest_tree_2,
                moist_forest_tree_3,
                moist_forest_tree_4,
                moist_forest_tree_5,
                moist_forest_tree_6,
                moist_forest_bush_1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="moist_forest_warm",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=0,
            pluviometry_max=1,

            ground_color="86 104 56",

            trees=[
                moist_forest_tree_1,
                moist_forest_tree_2,
                moist_forest_tree_3,
                moist_forest_tree_4,
                moist_forest_tree_5,
                moist_forest_tree_6,
                moist_forest_bush_1
            ]
        )
    )

    ###############################################################
    ######################## RAIN_FOREST ##########################
    ###############################################################

    ########################### ARBRES ############################

    rain_forest_tree_1 = Tree(
        name="rain_forest_tree_1",
        spawn_probability=0.15,
        body=[
            [None,          "68 88 39",    "68 88 39",    "68 88 39",    None],

            ["68 88 39",    "68 88 39",    "68 88 39",    "68 88 39",    "68 88 39"],

            [None,          "68 88 39",    "88 107 55",   "68 88 39",    "68 88 39"],

            [None,          None,          "111 129 74",  "68 88 39",    None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          None,          "114 131 77",  None,          None]
        ]
    )

    rain_forest_tree_2 = Tree(
        name="rain_forest_tree_2",
        spawn_probability=0.03,
        body=[
            [None,          "68 88 39",    "68 88 39",    "68 88 39",    None],

            ["68 88 39",    "68 88 39",    "68 88 39",    "68 88 39",    "68 88 39"],

            [None,          "68 88 39",    "88 107 55",   "68 88 39",    "68 88 39"],

            [None,          None,          "111 129 74",  None,          None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          None,          "116 133 78",  None,          None],

            [None,          "114 131 77",  "116 133 78",  None,          None],

            [None,          "114 131 77",  None,          None,          None]
        ]
    )

    rain_forest_tree_3 = Tree(
        name="rain_forest_tree_3",
        spawn_probability=0.05,
        body=[
            ["68 88 39",    "68 88 39",    None],

            ["68 88 39",    "68 88 39",    "68 88 39"],

            ["68 88 39",    "88 107 55",   "68 88 39"],

            [None,          "111 129 74",  None],

            [None,          "116 133 78",  None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="rain_forest",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=1,
            pluviometry_max=2,

            ground_color="89 93 66",

            trees=[
                rain_forest_tree_1,
                rain_forest_tree_2,
                rain_forest_tree_3
            ]
        )
    )

    ###############################################################
    ####################### ROCKS_AND_ICE #########################
    ###############################################################

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="rocks_and_ice",

            temperature_min=-3,
            temperature_max=-2,
            pluviometry_min=-4,
            pluviometry_max=-1,

            ground_color="190 220 255",

            trees=[
                empty_tree
            ]
        )
    )

    ###############################################################
    ########################### STEPPE ############################
    ###############################################################

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="steppe",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=-2,
            pluviometry_max=-1,

            ground_color="160 173 120",

            trees=[
                empty_tree
            ]
        )
    )

    ###############################################################
    #################### STEPPE_WOODLAND_THORN ####################
    ###############################################################

    ########################### ARBRES ############################

    steppe_woodland_thorn_tree_1 = Tree(
        name="steppe_woodland_thorn_tree_1",
        spawn_probability=0.05,
        body=[
            [None,          "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "34 58 26"],

            ["34 58 26",    "34 58 26",    "34 58 26"],

            [None,          "88 73 50",    None]
        ]
    )

    steppe_woodland_thorn_tree_2 = Tree(
        name="steppe_woodland_thorn_tree_2",
        spawn_probability=0.05,
        body=[
            [None,          "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "34 58 26"],

            [None,          "88 73 50",    None]
        ]
    )

    steppe_woodland_thorn_tree_3 = Tree(
        name="steppe_woodland_thorn_tree_3",
        spawn_probability=0.005,
        body=[
            ["34 58 26",    "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "34 58 26"],

            [None,          "88 73 50",    None]
        ]
    )

    steppe_woodland_thorn_tree_4 = Tree(
        name="steppe_woodland_thorn_tree_4",
        spawn_probability=0.005,
        body=[
            [None,          "34 58 26",    "34 58 26"],

            ["34 58 26",    "34 58 26",    "34 58 26"],

            [None,          "88 73 50",    None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="steppe_woodland_thorn",
            temperature_min=1,
            temperature_max=2,
            pluviometry_min=-2,
            pluviometry_max=-1,
            ground_color="160 173 120",

            trees=[
                steppe_woodland_thorn_tree_1,
                steppe_woodland_thorn_tree_2,
                steppe_woodland_thorn_tree_3,
                steppe_woodland_thorn_tree_4
            ]
        )
    )

    ###############################################################
    ########################### TAIGA #############################
    ###############################################################

    ########################### ARBRES ############################

    taiga_tree_1 = Tree(
        name="taiga_tree_1",
        spawn_probability=0.03,
        body=[
            [None,          None,          "34 58 26",    None,          None],

            [None,          None,          "34 58 26",    None,          None],

            [None,          "34 58 26",    "34 58 26",    "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    "34 58 26"],

            [None,          None,          "88 73 50",    None,          None]
        ]
    )

    taiga_tree_2 = Tree(
        name="taiga_tree_2",
        spawn_probability=0.01,
        body=[
            [None,          None,          "34 58 26",    None,          None],

            [None,          None,          "34 58 26",    None,          None],

            [None,          "34 58 26",    "34 58 26",    "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "88 73 50",    "34 58 26",    None],

            [None,          None,          "88 73 50",    None,          None]
        ]
    )

    taiga_tree_3 = Tree(
        name="taiga_tree_3",
        spawn_probability=0.03,
        body=[
            [None,          "34 58 26",    None],

            [None,          "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "34 58 26"],

            [None,          "88 73 50",    None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="taiga_desert",

            temperature_min=-1,
            temperature_max=0,
            pluviometry_min=-4,
            pluviometry_max=-3,
            ground_color="146 126 101",

            trees=[
                taiga_tree_1,
                taiga_tree_2,
                taiga_tree_3
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="taiga_dry",
            temperature_min=-1,
            temperature_max=0,
            pluviometry_min=-3,
            pluviometry_max=-2,
            ground_color="167 175 120",

            trees=[
                taiga_tree_1,
                taiga_tree_2,
                taiga_tree_3
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="taiga_moist",

            temperature_min=-1,
            temperature_max=0,
            pluviometry_min=-2,
            pluviometry_max=-1,

            ground_color="86 104 56",

            trees=[
                taiga_tree_1,
                taiga_tree_2,
                taiga_tree_3
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="taiga_rain",

            temperature_min=-1,
            temperature_max=0,
            pluviometry_min=0,
            pluviometry_max=1,

            ground_color="57 102 21",

            trees=[
                taiga_tree_1,
                taiga_tree_2,
                taiga_tree_3
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="taiga_wet",

            temperature_min=-1,
            temperature_max=0,
            pluviometry_min=-1,
            pluviometry_max=0,

            ground_color="75 102 44",

            trees=[
                taiga_tree_1,
                taiga_tree_2,
                taiga_tree_3
            ]
        )
    )

    ###############################################################
    ########################## TUNDRA #############################
    ###############################################################

    ########################### ARBRES ############################

    tundra_bush_1 = Tree(
        name="tundra_bush_1",
        spawn_probability=0.005,
        body=[
            ["34 58 26",    "34 58 26"]
        ]
    )

    tundra_bush_2 = Tree(
        name="tundra_bush_2",
        spawn_probability=0.002,
        body=[
            ["34 58 26",    "34 58 26",    "34 58 26"]
        ]
    )

    tundra_bush_3 = Tree(
        name="tundra_bush_3",
        spawn_probability=0.001,
        body=[
            [None,          "34 58 26",    None,          None],

            ["34 58 26",    "34 58 26",    "34 58 26",    "34 58 26"]
        ]
    )

    tundra_bush_4 = Tree(
        name="tundra_bush_4",
        spawn_probability=0.001,
        body=[
            [None,          None,          "34 58 26",    None],

            ["34 58 26",    "34 58 26",    "34 58 26",    "34 58 26"]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="tundra_dry",

            temperature_min=-2,
            temperature_max=-1,
            pluviometry_min=-4,
            pluviometry_max=-3,

            ground_color="167 175 120",

            trees=[
                tundra_bush_1,
                tundra_bush_2,
                tundra_bush_3,
                tundra_bush_4
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="tundra_moist",

            temperature_min=-2,
            temperature_max=-1,
            pluviometry_min=-3,
            pluviometry_max=-2,

            ground_color="86 104 56",

            trees=[
                tundra_bush_1,
                tundra_bush_2,
                tundra_bush_3,
                tundra_bush_4
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="tundra_rain",

            temperature_min=-2,
            temperature_max=-1,
            pluviometry_min=-1,
            pluviometry_max=0,

            ground_color="57 102 21",

            trees=[
                tundra_bush_1,
                tundra_bush_2,
                tundra_bush_3,
                tundra_bush_4
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="tundra_wet",

            temperature_min=-2,
            temperature_max=-1,
            pluviometry_min=-2,
            pluviometry_max=-1,

            ground_color="75 102 44",

            trees=[
                tundra_bush_1,
                tundra_bush_2,
                tundra_bush_3,
                tundra_bush_4
            ]
        )
    )

    ###############################################################
    ###################### TROPICAL_FOREST ########################
    ###############################################################

    ########################### ARBRES ############################

    tropical_forest_tree_1 = Tree(
        name="tropical_forest_tree_1",
        spawn_probability=0.15,
        body=[
            [None,          "0 69 41",     "0 69 41",
                "0 69 41",     "0 69 41",     "0 69 41",     None],

            ["0 69 41",     "0 69 41",     "0 69 41",     "0 69 41",
                "0 69 41",     "0 69 41",     "0 69 41"],

            [None,          None,          None,          "88 73 50",
                None,          None,          None],

            [None,          None,          None,          "88 73 50",
                None,          None,          None],

            [None,          None,          None,          "88 73 50",
                None,          None,          None],

            [None,          None,          None,          "88 73 50",
                None,          None,          None],

            [None,          None,          None,          "88 73 50",
                "88 73 50",    None,          None],

            [None,          None,          None,          None,
                "88 73 50",    None,          None],

            [None,          None,          None,          None,
                "88 73 50",    None,          None]
        ]
    )

    tropical_forest_tree_2 = Tree(
        name="tropical_forest_tree_2",
        spawn_probability=0.1,
        body=[
            [None,          "124 168 21",  "124 168 21",
                "124 168 21",  "124 168 21",  None],

            ["124 168 21",  "124 168 21",  "124 168 21",
                "124 168 21",  "124 168 21",  "124 168 21"],

            [None,          None,          "225 219 185",
                None,          None,          None],

            [None,          None,          "225 219 185",
                None,          None,          None],

            [None,          None,          "225 219 185",
                None,          None,          None],

            [None,          None,          "225 219 185",
                None,          None,          None],

            [None,          None,          "225 219 185",
                None,          None,          None],

            [None,          None,          "225 219 185",
                None,          None,          None]
        ]
    )

    tropical_forest_tree_3 = Tree(
        name="tropical_forest_tree_3",
        spawn_probability=0.05,
        body=[
            [None,          "19 84 20",    "19 84 20",    "19 84 20",    None],

            ["19 84 20",    "19 84 20",    "19 84 20",    "19 84 20",    "19 84 20"],

            [None,          None,          "46 27 23",    None,          None],

            [None,          None,          "46 27 23",    None,          None],

            [None,          None,          "46 27 23",    None,          None],

            [None,          None,          "46 27 23",    None,          None],

            [None,          None,          "46 27 23",    None,          None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="tropical_forest_tropical",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=3,
            pluviometry_max=4,

            ground_color="71 94 12",

            trees=[
                tropical_forest_tree_1,
                tropical_forest_tree_2,
                tropical_forest_tree_3
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="tropical_forest_warm",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=2,
            pluviometry_max=3,

            ground_color="94 124 16",

            trees=[
                tropical_forest_tree_1,
                tropical_forest_tree_2,
                tropical_forest_tree_3
            ]
        )
    )

    ###############################################################
    ###################### VERY_DRY_FOREST ########################
    ###############################################################

    ########################### ARBRES ############################

    very_dry_forest_tree_1 = Tree(
        name="very_dry_forest_tree_1",
        spawn_probability=0.055,
        body=[
            [None,          None,          "121 105 56",
                None,          None,          None,          None],

            [None,          None,          None,          "133 103 69",
                None,          "133 103 69",  "121 105 56"],

            ["121 105 56",  "133 103 69",  "133 103 69",
                "133 103 69",  "133 103 69",  None,          None],

            [None,          "121 105 56",  None,
                "133 103 69",  None,          None,          None],

            [None,          None,          None,
                "133 103 69",  None,          None,          None],

            [None,          None,          None,
                "133 103 69",  None,          None,          None]
        ]
    )

    very_dry_forest_tree_2 = Tree(
        name="very_dry_forest_tree_2",
        spawn_probability=0.05,
        body=[
            [None,          "121 105 56",  None,
                "133 103 69",  "121 105 56"],

            ["121 105 56",  "133 103 69",  "133 103 69",  "133 103 69",  None],

            [None,          None,          "133 103 69",  None,          None],

            [None,          None,          "133 103 69",  None,          None]
        ]
    )

    very_dry_forest_tree_3 = Tree(
        name="very_dry_forest_tree_3",
        spawn_probability=0.05,
        body=[
            [None,          None,          None,          "121 105 56",  None],

            ["121 105 56",  None,          None,
                "133 103 69",  "121 105 56"],

            [None,          "133 103 69",  "133 103 69",  "133 103 69",  None],

            [None,          None,          "133 103 69",  None,          None],

            [None,          None,          "133 103 69",  None,          None],

            [None,          None,          "133 103 69",  None,          None]
        ]
    )

    very_dry_forest_bush_1 = Tree(
        name="very_dry_forest_bush_1",
        spawn_probability=0.005,
        body=[
            ["121 105 56"]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="very_dry_forest",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=-1,
            pluviometry_max=0,

            ground_color="191 168 124",

            trees=[
                very_dry_forest_tree_1,
                very_dry_forest_tree_2,
                very_dry_forest_tree_3,
                very_dry_forest_bush_1
            ]
        )
    )

    ###############################################################
    ######################### WET_FOREST ##########################
    ###############################################################

    ########################### ARBRES ############################

    wet_forest_tree_1_v1 = Tree(
        name="wet_forest_tree_1_v1",
        spawn_probability=0.07,
        body=[
            [None,          "38 127 0",    "38 127 0",    "38 127 0",    None],

            ["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"],

            [None,          None,          "95 80 51",    None,          None],

            [None,          None,          "95 80 51",    None,          None],

            [None,          None,          "95 80 51",    None,          None],

            [None,          None,          "95 80 51",    None,          None],

            [None,          None,          "95 80 51",    None,          None],

            [None,          None,          "95 80 51",    None,          None]
        ]
    )

    wet_forest_tree_1_v2 = Tree(
        name="wet_forest_tree_1_v2",
        spawn_probability=0.1,
        body=[
            [None,          "96 142 8",    "96 142 8",    "96 142 8",    None],

            ["96 142 8",    "96 142 8",    "96 142 8",    "96 142 8",    "96 142 8"],

            [None,          None,          "103 103 17",   None,          None],

            [None,          None,          "103 103 17",   None,          None],

            [None,          None,          "103 103 17",   None,          None],

            [None,          None,          "103 103 17",   None,          None],

            [None,          None,          "103 103 17",   None,          None],

            [None,          None,          "103 103 17",   None,          None]
        ]
    )

    wet_forest_tree_1_v3 = Tree(
        name="wet_forest_tree_1_v3",
        spawn_probability=0.08,
        body=[
            [None,          "38 127 0",    "38 127 0",    "38 127 0",    None],

            ["38 127 0",    "38 127 0",    "38 127 0",    "38 127 0",    "38 127 0"],

            [None,          None,          "132 115 95",  None,          None],

            [None,          None,          "132 115 95",  None,          None],

            [None,          None,          "132 115 95",  None,          None],

            [None,          None,          "132 115 95",  None,          None],

            [None,          None,          "132 115 95",  None,          None],

            [None,          None,          "132 115 95",  None,          None]
        ]
    )

    wet_forest_tree_2_v1 = Tree(
        name="wet_forest_tree_2_v1",
        spawn_probability=0.03,
        body=[
            [None,          "38 127 0",    None],

            ["38 127 0",    "38 127 0",    "38 127 0"],

            [None,          "95 80 51",    None],

            [None,          "95 80 51",    None],

            [None,          "95 80 51",    None],

            [None,          "95 80 51",    None]
        ]
    )

    wet_forest_tree_2_v2 = Tree(
        name="wet_forest_tree_2_v2",
        spawn_probability=0.07,
        body=[
            [None,          "96 142 8",    None],

            ["96 142 8",    "96 142 8",    "96 142 8"],

            [None,          "103 103 17",    None],

            [None,          "103 103 17",    None],

            [None,          "103 103 17",    None],

            [None,          "103 103 17",    None]
        ]
    )

    wet_forest_tree_2_v3 = Tree(
        name="wet_forest_tree_2_v3",
        spawn_probability=0.07,
        body=[
            [None,          "38 127 0",    None],

            ["38 127 0",    "38 127 0",    "38 127 0"],

            [None,          "132 115 95",  None],

            [None,          "132 115 95",  None],

            [None,          "132 115 95",  None],

            [None,          "132 115 95",  None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="wet_forest_cool",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=0,
            pluviometry_max=1,

            ground_color="128 168 104",

            trees=[
                wet_forest_tree_1_v1,
                wet_forest_tree_2_v1
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="wet_forest_tropical",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=2,
            pluviometry_max=3,

            ground_color="128 168 104",

            trees=[
                wet_forest_tree_1_v2,
                wet_forest_tree_2_v2
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="wet_forest_warm",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=1,
            pluviometry_max=2,

            ground_color="128 168 104",

            trees=[
                wet_forest_tree_1_v3,
                wet_forest_tree_2_v3,
            ]
        )
    )

    ###############################################################
    ####################### WOODLAND_THORN ########################
    ###############################################################

    ########################### ARBRES ############################

    woodland_thorn_tree_1 = Tree(
        name="woodland_thorn_tree_1",
        spawn_probability=0.06,
        body=[
            [None,          "39 67 0",     "39 67 0",
                "39 67 0",     "39 67 0",     "39 67 0",     None],

            ["39 67 0",     "39 67 0",     "39 67 0",     "39 67 0",
                "39 67 0",     "39 67 0",     "39 67 0"],

            [None,          "138 127 99",  None,          "118 98 65",
                None,          "138 127 99",  None],

            [None,          None,          None,          "118 98 65",
                None,          "138 127 99",  None],

            [None,          None,          None,          None,
                "118 98 65",   None,          None],

            [None,          None,          None,          None,
                "118 98 65",   None,          None]
        ]
    )

    woodland_thorn_tree_2 = Tree(
        name="woodland_thorn_tree_2",
        spawn_probability=0.03,
        body=[
            [None,          "39 67 0",     "39 67 0",     None],

            ["39 67 0",     "39 67 0",     "39 67 0",     "39 67 0"],

            ["138 127 99",  None,          "118 98 65",   None],

            [None,          None,          "118 98 65",   None],

            [None,          None,          "118 98 65",   None]
        ]
    )

    woodland_thorn_tree_3 = Tree(
        name="woodland_thorn_tree_3",
        spawn_probability=0.01,
        body=[
            [None,          "39 67 0",     "39 67 0",
                "39 67 0",     "39 67 0",     None],

            ["39 67 0",     "39 67 0",     "39 67 0",
                "39 67 0",     "39 67 0",     "39 67 0"],

            ["138 127 99",  None,          "118 98 65",
                None,          "138 127 99",  None],

            ["138 127 99",  None,          "118 98 65",
                None,          "138 127 99",  None],

            [None,          None,          "118 98 65",
                None,          None,          None],

            [None,          None,          "118 98 65",
                None,          None,          None],

            [None,          "118 98 65",   None,
                None,          None,          None]
        ]
    )

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="woodland_thorn",

            temperature_min=2,
            temperature_max=3,
            pluviometry_min=-2,
            pluviometry_max=-1,

            ground_color="149 163 140",

            trees=[
                woodland_thorn_tree_1,
                woodland_thorn_tree_2,
                woodland_thorn_tree_3
            ]
        )
    )

    ###############################################################
    ############################ WATER ############################
    ###############################################################

    ########################### BIOMES ############################

    add_in_dict(
        dict_biomes,
        Biome(
            name="water",

            temperature_min=0,
            temperature_max=0,
            pluviometry_min=0,
            pluviometry_max=0,

            ground_color="30 144 235",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_1",

            temperature_min=1.85,
            temperature_max=2,
            pluviometry_min=3,
            pluviometry_max=4,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_2",

            temperature_min=0.85,
            temperature_max=1,
            pluviometry_min=2,
            pluviometry_max=3,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_3",

            temperature_min=-0.25,
            temperature_max=0,
            pluviometry_min=1,
            pluviometry_max=2,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_4",

            temperature_min=-1.25,
            temperature_max=-1,
            pluviometry_min=0,
            pluviometry_max=1,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_Water_5",

            temperature_min=-2.25,
            temperature_max=-2,
            pluviometry_min=-1,
            pluviometry_max=0,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_6",

            temperature_min=1,
            temperature_max=2,
            pluviometry_min=3,
            pluviometry_max=3.15,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_7",

            temperature_min=0,
            temperature_max=1,
            pluviometry_min=2,
            pluviometry_max=2.15,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_8",

            temperature_min=-1,
            temperature_max=0,
            pluviometry_min=1,
            pluviometry_max=1.15,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_9",

            temperature_min=-2,
            temperature_max=-1,
            pluviometry_min=0,
            pluviometry_max=0.15,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    add_in_dict(
        dict_biomes,
        Biome(
            name="cyan_water_10",

            temperature_min=-3,
            temperature_max=-2,
            pluviometry_min=-1,
            pluviometry_max=-0.85,

            ground_color="64 164 223",

            trees=[
                empty_tree
            ]
        )
    )

    return Encyclopedia("Classique", dict_biomes)
