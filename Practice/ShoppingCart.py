
class Item:
	def __init__(self, name, price):
		self.name = name
		self.price = price
		     
	def __str__(self):                                            # HUMAN READABLE !!!
		return'{},{:.2f)'.format(self.name, self.price)
		      
item = Item('hat', 12.40)
		      
	def__repr__(self):
	    	return'{},{:.2f)'.format(self.name, self.price)
		    
		
class ShoppingCard:
	    def __init__(self):
	    	self.intems = []
	    
	    def add(self,item):
	    	self.items.append(item)
	    
	    def total(self):
	    	return sum(item.price for item in self.items)
		      
	    def remove_items(self):
		self.items = [for item in self.items!=name]
		      
	    def __str__(self):
		return '\n'.join(str(item) for item in self.items)
		      
cart  = SoppingCard()
cart.add(Item("shirt", 18.99))
cart.add(Item("tshirt", 22.59))
