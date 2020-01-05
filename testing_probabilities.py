import random
import math

########################## FONCTIONS ##########################

############# FONCTIONS DE CREATION ##############

def Between(val,min,max):
	if val >= min and val <=max :
		return True
	else :
		return False


def Type_Case():

	T_Type_Case = []
	T_Type_Case.append(["FTrp",["tempere_tiede","sous-tropical","tropical"],4000,16000,["surhumide"]])
	T_Type_Case.append(["FPlv",["boreal","tempere_frais"],1000,4000,["surhumide"]])
	T_Type_Case.append(["FHmd",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],500,8000,["tres_humide"]])
	T_Type_Case.append(["Ftpr",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],250,4000,["humide"]])
	T_Type_Case.append(["FSch",[]])
	T_Type_Case.append([])
	T_Type_Case.append([])
	T_Type_Case.append([])
	T_Type_Case.append([])
	T_Type_Case.append([])

	HMin = 0
	HMax = 1
	TMin = -20
	TMax = 50

	latitude = random.choice(["polaire","sous-polaire","boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"])
	print(latitude)

	PlAn = random.choice([125,250,500,1000,2000,4000,8000])
	print(PlAn)

	PvEv = random.choice(["suraride","tres_aride","aride","aride","mi-aride","sous-humide","humide","tres_humide","surhumide"])
	print(PvEv)







	"""i = 0

	while i < len(T_Type_Case) - 2 and not (Between(humidite,T_Type_Case[i][1],T_Type_Case[i][2]) and Between(temperature,T_Type_Case[i][3],T_Type_Case[i][4])) :
		i += 1
	return T_Type_Case[i][0]"""


Type_Case()

"""T=[]
for j in range(100000):
	T.append(Type_Case())

print("Trop : ",T.count("Trop")/1000)
print("Voulu : 8")
print("Feui : ",T.count("Feui")/1000)
print("Voulu : 15")
print("Sapn : ",T.count("Sapn")/1000)
print("Voulu : 5")
print("Taig : ",T.count("Taig")/1000)
print("Voulu : 10.3")
print("Toun : ",T.count("Toun")/1000)
print("Voulu : 8.0")
print("Stpe : ",T.count("Stpe")/1000)
print("Voulu : 6.9")
print("Savn : ",T.count("Savn")/1000)
print("Voulu : 13.8")
print("DsCh : ",T.count("DsCh")/1000)
print("Voulu : 19.1")
print("RoEG : ",T.count("RoEG")/1000)
print("Voulu : 7.6")"""
