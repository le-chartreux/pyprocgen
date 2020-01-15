import os
import subprocess

def Lire_Mots_Depuis_Fichier(Fichier):  ###Renvoie le(s) mot(s) d'une ligne sans le \n
	string=""
	courant=Fichier.read(1) #Lit le 1er caractère de la ligne
	while courant!="\n" and courant!="" :
		string+=courant
		courant=Fichier.read(1) #Lit le caractère après le dernier caractère lu
	return string

def Lire_Ligne(Fichier,num_ligne):
	for i in range(num_ligne + 6):
		Lire_Mots_Depuis_Fichier(Fichier)
	return Lire_Mots_Depuis_Fichier(Fichier)


def image_creation(Plateau):
	FichierDest = open("Generation_procedurale.ppm","w")
	FichierDest.write("P3\n")
	FichierDest.write("# Generation_procedurale.ppm\n")
	FichierDest.write(str(16 * len(Plateau[0])))
	FichierDest.write("\n")
	FichierDest.write(str(16 * len(Plateau)))
	FichierDest.write("\n")
	FichierDest.write("255\n")
	FichierDest.write("\n")

	for num_ligne_tableau in range(len(Plateau)):
		for num_ligne in range(16):
			for i in range(len(Plateau[0])):
				Nom = Plateau[num_ligne_tableau][i]
				Fichier=open("image_creation/images/" + str(Nom) + ".ppm","r")
				a = Lire_Ligne(Fichier,num_ligne)
				FichierDest.write(a)
				FichierDest.write(" ")
				Fichier.close()
			FichierDest.write("\n")
		print("Processing : ",round((num_ligne_tableau + 1)/len(Plateau)*100,2),"%", end = '\r')
	print("")
