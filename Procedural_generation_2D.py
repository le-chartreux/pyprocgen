import random
import math

########################## FONCTIONS ##########################

############# FONCTIONS DE CREATION ##############

def Creer_Plateau_Vide():
    nbx=eval(input("x = "))
    nby=eval(input("y = "))
    Plateau=[]
    for i in range (nby) :
        Plateau.append([])
        for j in range (nbx) :
            Plateau[i].append(Case(None,None, None))
    return Plateau

def Placer_1ere_Case(Plateau):
    """altitude = math.exp(random.uniform(1,8))
    print(altitude)"""
    temperature = random.uniform(-20,50)
    print(temperature)
    if temperature < 0:
        humidite = random.uniform(0,0.2)
    else :
        humidite = random.random()
    print(humidite)
    Plateau[0][0]=Case(Type_Case(humidite,temperature),humidite,temperature)
    return Plateau

def Type_Case(humidite,temperature):
    if humidite < 0.1 :
        if temperature > 25 :
            return "DsCh"
        elif temperature < 0 :
            return "Toun"
        else :
            return "Alpn"
    elif humidite < 0.3 :
        if temperature < 15  :
            return "Taig"
        else :
            return "Savn"
    else :
        if temperature < 0 :
            return "Plne"
        else :
            return "Feui"



############# FONCTIONS D AFFICHAGE ##############

def Afficher_Plateau(Plateau):
    for i in range (len(Plateau)) :
        for j in range (len(Plateau[0])):
            print(Plateau[i][j].type, ' ',end='')
        print('')

########################## CLASSE #################################

class Case:
    """ Classe définissant une case caractérisée par :
    - son type
    - son humidite
    - sa température
    """

    def __init__(self, type, humidite, temperature):
        # CONSTRUCTION DE LA CLASSE #
        self.type = type
        self.humidite = humidite
        self.temperature = temperature



##################### CORPS DU PROGRAMME ######################

Plateau=Creer_Plateau_Vide()
#Afficher_Plateau(Plateau)
Plateau = Placer_1ere_Case(Plateau)
Afficher_Plateau(Plateau)
print("Hello git 2 !")
