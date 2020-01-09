from .Classes import Case
###############################################################
#################### FONCTIONS DU PLATEAU  ####################
###############################################################

#################### CREER_PLATEAU_VIDE #######################
# Crée un plateau vide de x cases de largeur et y de longueur

def Creer_Plateau_Vide():
	nbx=eval(input("x = "))
	nby=eval(input("y = "))
	Plateau=[]
	for i in range (nby) :
		Plateau.append([])
		for j in range (nbx) :
			Plateau[i].append(Case(None,None,None))
	return Plateau


#################### AFFICHER_PLATEAU #########################
def Afficher_Plateau(Plateau):
	for i in range (len(Plateau)) :
		for j in range (len(Plateau[0])) :
			if Plateau[i][j].type == None :
				print(Plateau[i][j].type, ' ',end='')
			else :
				print(Plateau[i][j].type[0:4], ' ',end='')
		print('')
