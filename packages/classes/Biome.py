from packages.classes.Color import Color


class Biome:

    def __init__(
        self,
        name: str,
        temperature_min: int,
        temperature_max: int,
        pluviometry_min: int,
        pluviometry_max: int,
        ground_color: Color,
        trees: list
    ):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Biome, caractérisé par :
        # - son nom
        # - sa température minimale
        # - sa température maximale
        # - sa pluviometrie minimale
        # - sa pluviometrie maximale
        # - la couleur de son sol
        # - une liste des arbres qui y poussent
        # -----------------------------
        # UTILISE PAR :
        # - encyclopedia_functions.().encyclopedia_creation()
        # - decisional.choice_biome()
        # =============================
        self.name = name

        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.pluviometry_min = pluviometry_min
        self.pluviometry_max = pluviometry_max

        self.ground_color = ground_color

        self.trees = trees

    def in_range(self, temperature: float, pluviometry: float) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Renvoie si la température et la pluviométrie
        # correspondent à celles de ce Biome
        # -----------------------------
        # UTILISE PAR :
        # - p_decisional.f_choice_biome()
        # =============================
        return (
            self.temperature_min <= temperature <= self.temperature_max
            and self.pluviometry_min <= pluviometry < self.pluviometry_max
        )
