###############################################################
################### CLASS BIOME ###############################
###############################################################
# Classe définisant un biome, caractérisé par :
# - son identifiant (en 4 caractères)
# - sa temperature
# - sa Pluviometrie Annuelle Minimale
# - sa Pluviometrie Annuelle Maximale
class Biome:

	def __init__(self, id, Temperature, PlAnMin, PlAnMax):
		self.id = id
		self.Temperature = Temperature
		self.PlAnMin = PlAnMin
		self.PlAnMax = PlAnMax

	# Renvoit True si la Temperature et les PlAn correspondent
	# à celles de ce biome
	def in_range(self, Temperature, PlAn):
		return Temperature in self.Temperature and self.PlAnMin <= PlAn < self.PlAnMax

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
	Ajout_Biome(Biomes, Biome("DsCh1",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],0,125))
	Ajout_Biome(Biomes, Biome("FHmd1",["boreal"],500,1000))
	Ajout_Biome(Biomes, Biome("FHmd2",["tempere_frais"],1000,2000))
	Ajout_Biome(Biomes, Biome("FHmd3",["tempere_tiede","sous-tropical"],2000,4000))
	Ajout_Biome(Biomes, Biome("FHmd4",["tropical"],4000,8000))
	Ajout_Biome(Biomes, Biome("FPlv1",["boreal"],1000,2000))
	Ajout_Biome(Biomes, Biome("FPlv2",["tempere_frais"],2000,4000))
	Ajout_Biome(Biomes, Biome("FTpr1",["boreal"],250,500))
	Ajout_Biome(Biomes, Biome("FTpr2",["tempere_frais"],500,1000))
	Ajout_Biome(Biomes, Biome("FTpr3",["tempere_tiede","sous-tropical"],1000,2000))
	Ajout_Biome(Biomes, Biome("FTpr4",["tropical"],2000,4000))
	Ajout_Biome(Biomes, Biome("FTrp1",["tempere_tiede","sous-tropical"],4000,8000))
	Ajout_Biome(Biomes, Biome("FTrp2",["tropical"],8000,16000))
	Ajout_Biome(Biomes, Biome("FSch1",["tempere_tiede","sous-tropical"],500,1000))
	Ajout_Biome(Biomes, Biome("FSch2",["tropical"],1000,2000))
	Ajout_Biome(Biomes, Biome("FTSc1",["tropical"],500,1000))
	Ajout_Biome(Biomes, Biome("MaqD1",["tempere_frais","tempere_tiede","sous-tropical","tropical"],125,250))
	Ajout_Biome(Biomes, Biome("Maqi1",["tempere_tiede","sous-tropical","tropical"],250,500))
	Ajout_Biome(Biomes, Biome("MaqS1",["boreal"],125,250))
	Ajout_Biome(Biomes, Biome("Stpe1",["tempere_frais"],250,500))
	Ajout_Biome(Biomes, Biome("RoEG1",["polaire"],0,125))
	Ajout_Biome(Biomes, Biome("Taig1",["polaire"],125,500))
	Ajout_Biome(Biomes, Biome("TndS1",["sous-polaire"],0,125))
	Ajout_Biome(Biomes, Biome("Toun1",["sous-polaire"],125,1000))

	return Biomes
