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
	T_Type_Case.append(["Trop",0.6,1,25,30])
	T_Type_Case.append(["Feui",0.5,1,10,25])
	T_Type_Case.append(["Sapn",0.4,0.8,5,10])
	T_Type_Case.append(["Taig",0.3,0.8,-10,5])
	T_Type_Case.append(["Toun",0,0.3,-20,0])
	T_Type_Case.append(["Stpe",0,0.3,0,20])
	T_Type_Case.append(["Savn",0,0.3,20,30])
	T_Type_Case.append(["DsCh",0,0.2,30,50])
	T_Type_Case.append(["RoEG",0.3,0.45,-20,-10])

	HMin = 0
	HMax = 1
	TMin = -20
	TMax = 50

	HMin
	temperature = random.uniform(TMin,TMax)
	#print(temperature)
	humidite = random.random()
	#print(humidite)

	for i in range(len(T_Type_Case)):
		if Between(humidite,T_Type_Case[i][1],T_Type_Case[i][2]) and Between(temperature,T_Type_Case[i][3],T_Type_Case[i][4]) :
			return T_Type_Case[i][0]
	return None



T=[]
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
print("Voulu : 7.6")

print("Fini :)")
