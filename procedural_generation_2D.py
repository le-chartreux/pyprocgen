import random
from packages.p_biomes_creation import f_creation_constantes_biomes
from packages.p_board_functions import *
from packages.p_decisional import f_generer_case
from packages.p_image_creation import f_image_creation

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.
v_dic_biomes = f_creation_constantes_biomes()

v_nbx=eval(input("x = "))
v_nby=eval(input("y = "))
print("")

v_seed = {}
v_seed["Tx"] = random.randint(-100000,100000)
v_seed["Ty"] = random.randint(-100000,100000)
v_seed["Px"] = random.randint(-100000,100000)
v_seed["Py"] = random.randint(-100000,100000)

print("Seed coordinates :")
print("Temperature : x =",v_seed["Tx"],", y =",v_seed["Ty"])
print("Pluviometry : x =",v_seed["Px"],", y =",v_seed["Py"])
print("")

v_plateau = f_creer_plateau_vide(v_nbx,v_nby)

for v_num_colonnes in range (len(v_plateau)) :
	for v_num_ligne in range (len(v_plateau[0])) :
		v_plateau[v_num_colonnes][v_num_ligne] = f_generer_case(v_dic_biomes, v_num_colonnes, v_num_ligne, v_seed)
	print("Vectorial creation of the map : ",round((v_num_colonnes + 1)/len(v_plateau)*100,2),"%", end = "\r")
print("")

#Afficher_Plateau(Plateau)

f_image_creation(v_plateau, v_seed)

print("Done")
