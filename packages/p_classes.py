##############################################################
########################## CASE ##############################
##############################################################
# Classe définissant une case, caractérisée par :
# - son type
# - sa Température
# - sa Pluviometrie Annuelle
class C_Case:

	# CONSTRUCTION DE LA CLASSE #
	def __init__(self, type, Temp, PlAn):
		self.type = type
		self.Temp = Temp
		self.PlAn = PlAn


##############################################################
########################## IMAGE #############################
##############################################################
# Classe définissant une image, caractérisée par :
# - le nom du biome qu'elle represente
# - le vecteur de son body (16 string)
class C_Image:

	# CONSTRUCTION DE LA CLASSE #
	def __init__(self, NomBiome,Vect):
		self.NomBiome = NomBiome
		self.Vect = Vect
