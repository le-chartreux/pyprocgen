###############################################################
################### CLASS BIOME ###############################
###############################################################
# Classe définisant un biome, caractérisé par :
# - son identifiant (en 4 caractères)
# - sa temperature
# - sa Pluviometrie Annuelle Minimale
# - sa Pluviometrie Annuelle Maximale
class Biome:

	def __init__(self, id, TempMin,TempMax, PlAnMin, PlAnMax):
		self.id = id
		self.TempMin = TempMin
		self.TempMax = TempMax
		self.PlAnMin = PlAnMin
		self.PlAnMax = PlAnMax

	# Renvoit True si la Temperature et les PlAn correspondent
	# à celles de ce biome
	def in_range(self, Temp, PlAn):
		return self.TempMin <= Temp <= self.TempMax and self.PlAnMin <= PlAn < self.PlAnMax

###############################################################
######################### AJOUT_BIOME #########################
###############################################################
# Ajoute Biome dans le dicionnaire Biomes
def Ajout_Biome(Biomes, Biome):
	Biomes[Biome.id] = Biome

###############################################################
################# CREATION_CONSTANTES_BIOMES ##################
###############################################################
def Creation_Constantes_Biomes():
	Biomes = {}
	Ajout_Biome(Biomes, Biome("Desert_Boreal",2,3,0,1))
	Ajout_Biome(Biomes, Biome("Desert_Cool",3,4,0,1))
	Ajout_Biome(Biomes, Biome("Desert_Tropical",5,6,0,1))
	Ajout_Biome(Biomes, Biome("Desert_Warm",4,5,0,1))

	Ajout_Biome(Biomes, Biome("Desert_Scub_Cool",3,4,1,2))
	Ajout_Biome(Biomes, Biome("Desert_Scub_Tropical",5,6,1,2))
	Ajout_Biome(Biomes, Biome("Desert_Scub_Warm",4,5,1,2))

	Ajout_Biome(Biomes, Biome("Dry_Forest_Tropical",5,6,4,5))
	Ajout_Biome(Biomes, Biome("Dry_Forest_Warm",4,5,3,4))

	Ajout_Biome(Biomes, Biome("Moist_Forest_Cool",3,4,3,4))
	Ajout_Biome(Biomes, Biome("Moist_Forest_Tropical",5,6,5,6))
	Ajout_Biome(Biomes, Biome("Moist_Forest_Warm",4,5,4,5))

	Ajout_Biome(Biomes, Biome("Rain_Forest",3,4,5,6))

	Ajout_Biome(Biomes, Biome("Rocks_and_ice",0,1,0,3))

	Ajout_Biome(Biomes, Biome("Steppe",3,4,2,3))

	Ajout_Biome(Biomes, Biome("Steppe_Woodland_Thorn",4,5,2,3))

	Ajout_Biome(Biomes, Biome("Taiga_Dry",2,3,1,2))
	Ajout_Biome(Biomes, Biome("Taiga_Moist",2,3,2,3))
	Ajout_Biome(Biomes, Biome("Taiga_Rain",2,3,4,5))
	Ajout_Biome(Biomes, Biome("Taiga_Wet",2,3,3,4))

	Ajout_Biome(Biomes, Biome("Toundra_Dry",1,2,0,1))
	Ajout_Biome(Biomes, Biome("Toundra_Moist",1,2,1,2))
	Ajout_Biome(Biomes, Biome("Toundra_Rain",1,2,3,4))
	Ajout_Biome(Biomes, Biome("Toundra_Wet",1,2,2,3))

	Ajout_Biome(Biomes, Biome("Tropical_Forest_Tropical",5,6,7,8))
	Ajout_Biome(Biomes, Biome("Tropical_Forest_Warm",4,5,6,7))

	Ajout_Biome(Biomes, Biome("Very_Dry_Forest",5,6,3,4))

	Ajout_Biome(Biomes, Biome("Wet_Forest_Cool",3,4,4,5))
	Ajout_Biome(Biomes, Biome("Wet_Forest_Tropical",5,6,6,7))
	Ajout_Biome(Biomes, Biome("Wet_Forest_Warm",4,5,5,6))

	Ajout_Biome(Biomes, Biome("Woodland_Thorn",5,6,2,3))


	return Biomes
