import random
from packages.p_biomes_creation import f_creation_constantes_biomes
from packages.p_board_functions import *
from packages.p_decisional import f_generer_case
from packages.p_image_creation import f_image_creation

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.
Biomes = f_creation_constantes_biomes()

nbx=eval(input("x = "))
nby=eval(input("y = "))
print("")

Seed = {}
Seed["Tx"] = random.randint(-100000,100000)
Seed["Ty"] = random.randint(-100000,100000)
Seed["Px"] = random.randint(-100000,100000)
Seed["Py"] = random.randint(-100000,100000)

print("Seed coordinates :")
print("Temperature : x =",Seed["Tx"],", y =",Seed["Ty"])
print("Pluviometry : x =",Seed["Px"],", y =",Seed["Py"])
print("")

Plateau = f_creer_plateau_vide(nbx,nby)

for i in range (len(Plateau)) :
	for j in range (len(Plateau[0])) :
		Plateau[i][j] = f_generer_case(Biomes, i, j, Seed)
	print("Vectorial creation of the map : ",round((i + 1)/len(Plateau)*100,2),"%", end = "\r")
print("")

#Afficher_Plateau(Plateau)

f_image_creation(Plateau, Seed)

print("Done")
