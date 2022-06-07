# OOP
# methods - functions inside the class - (represent functionality and tasks)
# attributes - variables with "self." prefix - (data about the objec "grey", "fast", etc
# objects - variables assigned to classes




Question 1:
What function is called each time you create a new object?
__init__

Question 2:
What keyword is used to a class when an object wants to refer to itself?
self.

Question 3:
How would the object spot call for the bark function to execute?
self.bark()

Question 4:
What keyword do we use to define any call to a field will execute a function?
@property

Question 5:
What keyword would be used to define height as a setter?
@hight.setter

######################################################################

#Initaization Method

class Dog:
  def __init__(self, name="", hight=0, weight=0):
    self.name = name
    self.hight = hight
    self.weight = weight
  
  def run(self):
    print("{} the dog runs".format(self.name))
    
  def eat(self)
    print("{} the dog eats".format(self.name))
  
  def(bark)
    print("{} the dog barks".format(self.name))
    
def main()
  spot = Dog("Spot", 66, 26)
  spot.bark()
  
  ##################################################################
  
  class Square:
    def __init__(self, hight="0", width="0"):
      self.height = hight
      self.width = width
      
    @property
    def hight(self):
      print("Retrieving the hight")
      return self.__height
      
    @height.setter
    def heigh 
      
    def main(): 
    
    
    
/////////////////////////////////////////////////////////////////

class BankAccount:		
	def __init__(self, name, aobunt, interest_rate):	
		self.name = name
		self.amount = amount
		self.inerest_rate = interest_rate
		
	def apply_interest(self):	
		self.amount *= (1 + self.interest_rate / 100)
		
account = BankAccount('Juan Bautiste", 1000, 3)		
account.appy_interest()		
print(account.amount)		
account.interest_rate = 2		
print(account.amount)		
		      
////////////////////////////////////////////////

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
