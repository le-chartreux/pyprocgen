import os
### Fonctions de lecture de l'image ###

def Lire_Mots_Depuis_Fichier(Fichier):  ###Renvoie le(s) mot(s) d'une ligne sans le \n
	string=""
	courant=Fichier.read(1) #Lit le 1er caractère de la ligne
	while courant!="\n" and courant!="" :
		string+=courant
		courant=Fichier.read(1) #Lit le caractère après le dernier caractère lu
		return string


def Quelle_Indentation(LesDonnées) :    ###Regarde combien il y a d'espaces entre chaque nombre et retourne l'indentation

	return "\n"


def Conv_Fichier_Vers_Liste_Propre(NomComplet, TypeFichier): ###Lit l'image et stock ses nombres dans une liste
	global x, y, NomFichierHeader, NiveauGoC
	a=0
	Fichier=open(NomComplet,"r")
	if TypeFichier=="pbm" : NombreLignesDuBody=-4    #Compte le nombre de lignes du body, part de -4 ou -5 pour ne pas inclure le header
	else :NombreLignesDuBody=-5
	for line in Fichier : NombreLignesDuBody += 1

	Fichier.seek(0) #Repart en haut du fichier
	NM=Lire_Mots_Depuis_Fichier(Fichier)   #Nombre Magique
	NomFichierHeader=Lire_Mots_Depuis_Fichier(Fichier)   #Nom du fichier
	x=Lire_Mots_Depuis_Fichier(Fichier)    #Nombre de pixels horizontaux de l'image (normalement)
	if " " in x and Est_ce_un_nombre(x[0]) and not Est_ce_un_nombre(x[len(x)-1]) :  #Regarde si le x et y sont sur la même ligne
		EspacePassé=False
		y=""
		for i in range(len(x)) :
			if EspacePassé and Est_ce_un_nombre(x[i]) :
				y+=x[i]
			elif not EspacePassé and x[i]==" " :
				EspacePassé=True
				a=i
		x2=""
		for i in range(a) :
			x2+=x[i]
		x=x2

	else : y=int(Lire_Mots_Depuis_Fichier(Fichier))    #Nombre de pixels verticaux de l'image
	if TypeFichier!="pbm" : NiveauGoC=Lire_Mots_Depuis_Fichier(Fichier)   #Niveaux de gris ou de couleur
	LesDonnées=Fichier.read(-1) #Lit tout le reste du fichier
	if a!=0 :   #Pour règler un bug dont on ne comprenanait pas la cause, on a été obligé de créer un fichier original avec le x et le y sur des lignes différentes
		Fichier.close()
		os.remove(NomComplet)
		Fichier=open(NomComplet,"w")
		Fichier.write(NM)
		Fichier.write(NomFichierHeader + "\n")
		Fichier.write(x + "\n")
		Fichier.write(y + "\n")
		if TypeFichier!="pbm" : Fichier.write(NiveauGoC + "\n")
		Fichier.write(LesDonnées)
		Fichier.close()
		ListeDonnéesPropres=Conv_Fichier_Vers_Liste_Propre(NomComplet, TypeFichier)

	else :
		Indentation=Quelle_Indentation(LesDonnées)
		ListeDonnéesPropres=NettoyerDonnées(LesDonnées, NombreLignesDuBody, Indentation)
		Fichier.close()
	return ListeDonnéesPropres


def NettoyerDonnées(LesDonnées, NombreLignesDuBody, Indentation) :  ###Nettoie le str des données en supprimant les \n et l'indentation
	ListeDonnées=LesDonnées.split("\n") #Transforme le str du body en liste coupée à chaque \n
	DonnéesVrac=ListeDonnées[0]
	for i in range(NombreLignesDuBody-1) :  #-1 parce qu'on a déjà le 0 grace a la ligne précédente
		DonnéesVrac+=Indentation + ListeDonnées[i+1]
	ListeDonnées=DonnéesVrac.split(Indentation) #Supprime d'indentation
	while "" in ListeDonnées : ListeDonnées.pop(ListeDonnées.index("")) #Supprime d'éventuels cellules vides dans la liste
	return ListeDonnées


### Fonctions de sécurité, pour éviter les erreurs ###

def Est_ce_un_nombre(Symbole):  ###Regarde si le symbole demandé est un nombre
	try:
		float(Symbole)
		return True
	except ValueError:
		return False

def Ske_Le_Fichier_Existe(NomFichier, TypeFichier) :    ###Regarde si le fichier existe
	try:
		open(NomFichier  + "." + TypeFichier,"r")
		return True
	except FileNotFoundError:
		return False



def RenomerFichier(old, new) :  ### Regarde si le nom qu'on veut donner à notre nouveau fichier
	try:                        ### n'est pas déjà utlisé dans le dossier. Si oui, supprime l'ancien
		os.rename(old,new)      ### et renomme le nouveau
	except FileExistsError:
		os.remove(new)
		os.rename(old,new)


### Fonction de création de fichier

def ListeCleanToFichier(LesDonnées, NomFichier, TypeFichier):   ###Transforme la liste de données post-décompression en fichier lisible
	global x, y, NomFichierHeader, NiveauGoC, fich
	x = int(x)
	y = int(y)
	fich.write("P3\n")
	fich.write(str(x))
	fich.write("\n")
	fich.write(str(y))
	fich.write("\n")
	fich.write("255"+"\n")
	Compteur=0
	print(x)
	print(y)

	for i in range(y):
		for j in range(x*3):
			#print(Compteur)
			fich.write(str(LesDonnées[Compteur]))
			fich.write(" ")
			Compteur+=1
		fich.write("\n")
	fich.close()



NomFichier = input("Entrez le nom du fichier")
ListeDonnéesPropresFI=Conv_Fichier_Vers_Liste_Propre(NomFichier + ".ppm", "ppm")

fich = open(NomFichier + ".ppm","w")
ListeCleanToFichier(ListeDonnéesPropresFI, NomFichier,".ppm")
