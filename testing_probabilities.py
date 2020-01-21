from packages.p_biomes_creation import *
from packages.p_decisional import *
from packages.p_board_functions import *
import random


Biomes = Creation_Constantes_Biomes()
A = []
for j in range(100000):
	seed = {}
	seed['Tx'] = random.randint(-100000,100000)
	seed['Ty'] = random.randint(-100000,100000)
	seed['Px'] = random.randint(-100000,100000)
	seed['Py'] = random.randint(-100000,100000)
	A.append(Placer_Case(Biomes, 1, 1, seed).type)

print("Desert_Cool : ", end = '')
print(A.count("Desert_Cool")/1000)
print("Desert_Tropical : ", end = '')
print(A.count("Desert_Tropical")/1000)
print("Desert_Warm : ", end = '')
print(A.count("Desert_Warm")/1000)
print("TOTAL : ", end = '')
print(A.count("Desert_Cool")/1000 + A.count("Desert_Tropical")/1000 + A.count("Desert_Warm")/1000)

print("")

print("Desert_Scub_Cool : ", end = '')
print(A.count("Desert_Scub_Cool")/1000)
print("Desert_Scub_Tropical : ", end = '')
print(A.count("Desert_Scub_Tropical")/1000)
print("Desert_Scub_Warm : ", end = '')
print(A.count("Desert_Scub_Warm")/1000)
print("TOTAL : ", end = '')
print(A.count("Desert_Scub_Cool")/1000 + A.count("Desert_Scub_Tropical")/1000 + A.count("Desert_Scub_Warm")/1000)
print("")

print("Dry_Forest_Tropical : ", end = '')
print(A.count("Dry_Forest_Tropical")/1000)
print("Dry_Forest_Warm : ", end = '')
print(A.count("Dry_Forest_Warm")/1000)
print("TOTAL : ", end = '')
print(A.count("Dry_Forest_Tropical")/1000 + A.count("Dry_Forest_Warm")/1000)

print("")

print("Moist_Forest_Cool : ", end = '')
print(A.count("Moist_Forest_Cool")/1000)
print("Moist_Forest_Tropical : ", end = '')
print(A.count("Moist_Forest_Tropical")/1000)
print("Moist_Forest_Warm : ", end = '')
print(A.count("Moist_Forest_Warm")/1000)
print("TOTAL : ", end = '')
print(A.count("Moist_Forest_Cool")/1000 + A.count("Moist_Forest_Tropical")/1000 + A.count("Moist_Forest_Warm")/1000)

print("")

print("Rain_Forest : ", end = '')
print(A.count("Rain_Forest")/1000)

print("")

print("Rocks_and_ice : ", end = '')
print(A.count("Rocks_and_ice")/1000)

print("")

print("Steppe : ", end = '')
print(A.count("Steppe")/1000)

print("")

print("Steppe_Woodland_Thorn : ", end = '')
print(A.count("Steppe_Woodland_Thorn")/1000)

print("")

print("Taiga_Desert : ", end = '')
print(A.count("Taiga_Desert")/1000)
print("Taiga_Dry : ", end = '')
print(A.count("Taiga_Dry")/1000)
print("Taiga_Moist : ", end = '')
print(A.count("Taiga_Moist")/1000)
print("Taiga_Rain : ", end = '')
print(A.count("Taiga_Rain")/1000)
print("Taiga_Wet : ", end = '')
print(A.count("Taiga_Wet")/1000)
print("TOTAL : ", end = '')
print(A.count("Taiga_Desert")/1000 + A.count("Taiga_Dry")/1000 + A.count("Taiga_Moist")/1000 + A.count("Taiga_Rain")/1000 + A.count("Taiga_Wet")/1000)

print("")

print("Toundra_Dry : ", end = '')
print(A.count("Toundra_Dry")/1000)
print("Toundra_Moist : ", end = '')
print(A.count("Toundra_Moist")/1000)
print("Toundra_Rain : ", end = '')
print(A.count("Toundra_Rain")/1000)
print("Toundra_Wet : ", end = '')
print(A.count("Toundra_Wet")/1000)
print("TOTAL : ", end = '')
print(A.count("Toundra_Dry")/1000 + A.count("Toundra_Moist")/1000 + A.count("Toundra_Rain")/1000 + A.count("Toundra_Wet")/1000)

print("")

print("Tropical_Forest_Tropical : ", end = '')
print(A.count("Tropical_Forest_Tropical")/1000)
print("Tropical_Forest_Warm : ", end = '')
print(A.count("Tropical_Forest_Warm")/1000)
print("TOTAL : ", end = '')
print(A.count("Tropical_Forest_Tropical")/1000 + A.count("Tropical_Forest_Warm")/1000)

print("")

print("Very_Dry_Forest : ", end = '')
print(A.count("Very_Dry_Forest")/1000)
print("Wet_Forest_Cool : ", end = '')
print(A.count("Wet_Forest_Cool")/1000)
print("Wet_Forest_Tropical : ", end = '')
print(A.count("Wet_Forest_Tropical")/1000)
print("Wet_Forest_Warm : ", end = '')
print(A.count("Wet_Forest_Warm")/1000)
print("TOTAL : ", end = '')
print(A.count("Very_Dry_Forest")/1000 + A.count("Wet_Forest_Cool")/1000 + A.count("Wet_Forest_Tropical")/1000 + A.count("Wet_Forest_Warm")/1000)

print("")

print("Woodland_Thorn : ", end = '')
print(A.count("Woodland_Thorn")/1000)
