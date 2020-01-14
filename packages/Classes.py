##############################################################
########################## CASE ##############################
##############################################################
# Classe définissant une case, caractérisée par :
# - son type
# - sa Température
# - sa Pluviometrie Annuelle
class Case:

	def __init__(self, type, Temp, PlAn, PrlN):
		# CONSTRUCTION DE LA CLASSE #
		self.type = type
		self.Temp = Temp
		self.PlAn = PlAn
		self.PrlN = PrlN
