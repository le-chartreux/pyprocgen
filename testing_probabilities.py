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
	T_Type_Case.append(["FSch",["tempere_tiede","sous-tropical","tropical"],1000,2000,["sous-humide"]])
	T_Type_Case.append(["Stpe",["tempere_frais"],250,500,["montagne"]])
	T_Type_Case.append(["MaqS",["boreal"],125,250,["sous-alpin"]])
	T_Type_Case.append(["FTSc",["tropical"],500,1000,["mi-aride"]])
	T_Type_Case.append(["MaqD",["tempere_frais","tempere_tiede","sous-tropical","tropical"],125,250,["tres_aride","aride","mi-aride"]])
	T_Type_Case.append(["MaqS",["boreal"],125,250,["sous-humide"]])
	T_Type_Case.append(["DsCh",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],0,125,["suraride","tres_aride","aride","mi-aride"]])
	T_Type_Case.append(["TndS",["sous-polaire"],0,125,["sous-humide"]])
	T_Type_Case.append(["Toun",["sous-polaire"],125,1000,["humide","tres_humide","surhumide"]])
	T_Type_Case.append(["Taig",["polaire"],0,500,["humide","tres_humide","surhumide"]])
	T_Type_Case.append(["NULL",[""],0,0,[""]])

	Climat = random.choice(["polaire","sous-polaire","boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"])
	#print(Climat)

	PlAn = random.choice([125,250,500,1000,2000,4000,8000])
	#print(PlAn)

	PvEv = random.choice(["suraride","tres_aride","aride","aride","mi-aride","sous-humide","humide","tres_humide","surhumide"])
	#print(PvEv)


	i = 0

	while i < len(T_Type_Case) - 1 and not (Climat in T_Type_Case[i][1] and Between(PlAn,T_Type_Case[i][2],T_Type_Case[i][3]) and PvEv in T_Type_Case[i][4]) :
		i += 1
	return T_Type_Case[i][0]

#print(Type_Case())

T=[]
for j in range(100000):
	T.append(Type_Case())

print("FTrp : ",T.count("FTrp")/1000)
print("Voulu : 8")
print("FPlv : ",T.count("FPlv")/1000)
print("Voulu : ?")
print("FHmd : ",T.count("FHmd")/1000)
print("Voulu : ?")
print("Ftpr : ",T.count("Ftpr")/1000)
print("Voulu : ?")
print("FSch : ",T.count("FSch")/1000)
print("Voulu : ?")
print("Stpe : ",T.count("Stpe")/1000)
print("Voulu : 6.9")
print("FTSc : ",T.count("FTSc")/1000)
print("Voulu : 6.9")
print("MaqD : ",T.count("MaqD")/1000)
print("Voulu : ?")
print("MaqS : ",T.count("MaqS")/1000)
print("Voulu : ?")
print("DsCh : ",T.count("DsCh")/1000)
print("Voulu : 19.1")
print("TndS : ",T.count("Tnds")/1000)
print("Voulu : 10.3")
print("Taig : ",T.count("Taig")/1000)
print("Voulu : 10.3")
print("Toun : ",T.count("Toun")/1000)
print("Voulu : 8.0")
print("NULL : ",T.count("NULL")/1000)
print("Voulu : 0")
print("RoEG : ",T.count("RoEG")/1000)
print("Voulu : 7.6")
