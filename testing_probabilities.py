import random
import math

########################## FONCTIONS ##########################

############# FONCTIONS DE CREATION ##############

def Type_Case():
    temperature = random.uniform(-20,50)
    #print(temperature)
    humidite = random.random()
    #print(humidite)
    if humidite > 0.7 and temperature > 25 and temperature < 30 :
        return "Trop"
    elif humidite > 0.5 and temperature > 10 and temperature < 25 :
        return "Feui"
    elif humidite > 0.5 and temperature > 5 and temperature < 25 :
        return "Sapn"
    elif humidite > 0.3 and temperature > -5 and temperature < 5 :
        return "Taig"
    elif humidite < 0.3 and temperature < -5 :
        return "Toun"


T=[]
for j in range(100000):
    T.append(Type_Case())

print("DsCh : ",T.count("DsCh")/1000)
print("Toun : ",T.count("Toun")/1000)
print("Voulu : 8")
print("Alpn : ",T.count("Alpn")/1000)
print("Taig : ",T.count("Taig")/1000)
print("StSv : ",T.count("StSv")/1000)
print("Feui : ",T.count("Feui")/1000)
print("Voulu : 9")
print("Trop : ",T.count("Trop")/1000)
print("Voulu : 16")
print("Sapn : ",T.count("Sapn")/1000)
print("Voulu : 3")
