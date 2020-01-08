import random
import math

########################## FONCTIONS ##########################

############# FONCTIONS DE CREATION ##############

T_Type_Case = []
T_Type_Case.append(["DsCh",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],0,125])
T_Type_Case.append(["FHmd",["boreal"],500,1000])
T_Type_Case.append(["FHmd",["tempere_frais"],1000,2000])
T_Type_Case.append(["FHmd",["tempere_tiede","sous-tropical"],2000,4000])
T_Type_Case.append(["FHmd",["tropical"],4000,8000])
T_Type_Case.append(["FPlv",["boreal"],1000,2000])
T_Type_Case.append(["FPlv",["tempere_frais"],2000,4000])
T_Type_Case.append(["FTrp",["tempere_tiede","sous-tropical"],4000,8000])
T_Type_Case.append(["FTrp",["tropical"],8000,16000])
T_Type_Case.append(["FTpr",["boreal"],250,500])
T_Type_Case.append(["FTpr",["tempere_frais"],500,1000])
T_Type_Case.append(["FTpr",["tempere_tiede","sous-tropical"],1000,2000])
T_Type_Case.append(["FTpr",["tropical"],2000,4000])
T_Type_Case.append(["FSch",["tempere_tiede","sous-tropical"],500,1000])
T_Type_Case.append(["FSch",["tropical"],1000,2000])
T_Type_Case.append(["FTSc",["tropical"],500,1000])
T_Type_Case.append(["MaqD",["tempere_frais","tempere_tiede","sous-tropical","tropical"],125,250])
T_Type_Case.append(["Maqi",["tempere_tiede","sous-tropical","tropical"],250,500])
T_Type_Case.append(["MaqS",["boreal"],125,250])
T_Type_Case.append(["Stpe",["tempere_frais"],250,500])
T_Type_Case.append(["RoEG",["polaire"],0,125])
T_Type_Case.append(["Taig",["polaire"],125,500])
T_Type_Case.append(["TndS",["sous-polaire"],0,125])
T_Type_Case.append(["Toun",["sous-polaire"],125,1000])

T_Type_Case.append(["NULL",[""],0,0])




class Biome:

	def __init__(self, id, temps, min_hum, max_hum):

		self.id = id
		self.temps = temps
		self.min_humidity = min_hum
		self.max_humidity = max_hum

	def in_range(self, temp, hum):
		return temp in self.temps and self.min_humidity <= hum <= self.max_humidity

biomes = {}

def add_biome(biome):
	global biomes
	biomes[biome.id] = biome

def get_biome(temp, hum):

	for biome in biomes.values():
		if biome.in_range(temp, hum):
			return biome.id

	return None

add_biome(Biome("DsCh", ["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"], 0, 125))
add_biome(Biome("FHmd", ["boreal"], 500, 1000))


def Between(val,min,max):
	if val >= min and val <=max :
		return True
	else :
		return False


def Type_Case(T_Type_Case):

	aleatTemp = random.randint(0,100)

	if Between(aleatTemp,0,15) :
		Temperature = "polaire"

	elif Between(aleatTemp,15,25) :
		Temperature = "sous-polaire"


	else :
		Temperature = random.choice(["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"])



	#print(Temperature)

	if Temperature == "polaire":
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500)])

	elif Temperature == "sous-polaire" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000)])

	elif Temperature == "boreal" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000)])

	elif Temperature == "tempere_frais" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000)])

	elif Temperature == "tempere_tiede" or Temperature == "sous-tropical" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000)])

	elif Temperature == "tropical" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000),random.randint(8000,16000)])

	#print(PlAn)

	i = 0

	while i < len(T_Type_Case) - 1 and not (Temperature in T_Type_Case[i][1] and Between(PlAn,T_Type_Case[i][2],T_Type_Case[i][3])) :
		i += 1
	#print(T_Type_Case[i][0])
	return T_Type_Case[i][0]

#print(Type_Case(T_Type_Case))


T=[]
for j in range(100000):
	T.append(Type_Case(T_Type_Case))

print("FTrp : ",T.count("FTrp")/1000)
print("Voulu : 8")
print("FPlv : ",T.count("FPlv")/1000)
print("Voulu : 3.5")
print("FHmd : ",T.count("FHmd")/1000)
print("Voulu : 3")
print("FTpr : ",T.count("FTpr")/1000)
print("Voulu : 8.7")
print("FSch : ",T.count("FSch")/1000)
print("Voulu : 7.8")
print("Stpe : ",T.count("Stpe")/1000)
print("Voulu : 6.9")
print("FTSc : ",T.count("FTSc")/1000)
print("Voulu : 6.9")
print("Maqi : ",T.count("Maqi")/1000)
print("Voulu : 5")
print("MaqD : ",T.count("MaqD")/1000)
print("Voulu : 3")
print("MaqS : ",T.count("MaqS")/1000)
print("Voulu : 1")
print("DsCh : ",T.count("DsCh")/1000)
print("Voulu : 19.1")
print("TndS : ",T.count("TndS")/1000)
print("Voulu : 1.5")
print("Toun : ",T.count("Toun")/1000)
print("Voulu : 8.0")
print("Taig : ",T.count("Taig")/1000)
print("Voulu : 10.3")
print("RoEG : ",T.count("RoEG")/1000)
print("Voulu : 7.6")
print("NULL : ",T.count("NULL")/1000)
print("Voulu : 0")
