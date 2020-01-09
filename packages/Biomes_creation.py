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
	Ajout_Biome(Biomes, Biome("DsCh1",3,35,62,125))
	Ajout_Biome(Biomes, Biome("FHmd1",3,6,500,1000))
	Ajout_Biome(Biomes, Biome("FHmd2",6,12,1000,2000))
	Ajout_Biome(Biomes, Biome("FHmd3",12,24,2000,4000))
	Ajout_Biome(Biomes, Biome("FHmd4",24,35,4000,8000))
	Ajout_Biome(Biomes, Biome("FPlv1",3,6,1000,2000))
	Ajout_Biome(Biomes, Biome("FPlv2",6,12,2000,4000))
	Ajout_Biome(Biomes, Biome("FTpr1",3,6,250,500))
	Ajout_Biome(Biomes, Biome("FTpr2",6,12,500,1000))
	Ajout_Biome(Biomes, Biome("FTpr3",12,24,1000,2000))
	Ajout_Biome(Biomes, Biome("FTpr4",24,35,2000,4000))
	Ajout_Biome(Biomes, Biome("FTrp1",12,24,4000,8000))
	Ajout_Biome(Biomes, Biome("FTrp2",24,35,8000,16000))
	Ajout_Biome(Biomes, Biome("FSch1",12,24,500,1000))
	Ajout_Biome(Biomes, Biome("FSch2",24,35,1000,2000))
	Ajout_Biome(Biomes, Biome("FTSc1",24,35,500,1000))
	Ajout_Biome(Biomes, Biome("MaqD1",6,35,125,250))
	Ajout_Biome(Biomes, Biome("Maqi1",12,35,250,500))
	Ajout_Biome(Biomes, Biome("MaqS1",3,6,125,250))
	Ajout_Biome(Biomes, Biome("Stpe1",6,12,250,500))
	Ajout_Biome(Biomes, Biome("RoEG1",-10,1.5,62,125))
	Ajout_Biome(Biomes, Biome("Taig1",-10,1.5,125,500))
	Ajout_Biome(Biomes, Biome("TndS1",1.5,3,62,125))
	Ajout_Biome(Biomes, Biome("Toun1",1.5,3,125,1000))

	return Biomes
