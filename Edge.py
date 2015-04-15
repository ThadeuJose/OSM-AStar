class edge:

	def __init__(self,sDestiny,iCost):
		self.sDestiny=sDestiny
		self.iCost=iCost
	
	def __str__(self):
		return str(str(self.sDestiny)+' '+str(self.iCost))
	
	def __hash__(self):
		return hash(self.sDestiny)		
