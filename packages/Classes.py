##############################################################
########################## CASE ##############################
##############################################################
# Classe définissant une case, caractérisée par :
# - son type
# - sa Température
# - sa Pluviometrie Annuelle
class Case:

	def __init__(self, type, Temperature, PlAn):
		# CONSTRUCTION DE LA CLASSE #
		self.type = type
		self.Temperature = Temperature
		self.PlAn = PlAn
