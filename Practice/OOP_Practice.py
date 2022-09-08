def string_reverse(s):                                             
  i = len(s)
  reverse = ""
  while i > 0:
    reverse += S[i-1]                                                      #reverse String
    i -= 1
  return reverse

s = "string"
print(sting_reverse('string'))
    
### ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

from random import choice

def rand_lower_string(n):
  n = int(input("Please enter an int: "))
  s = ""
  for i in range(n):
    s += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  return s

### OR

def rand_lower_string(n):
  return ' '.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(n))

###

def daily_blogs(*args):                    #args can be replaced with blog_1, blog_2, blog_3
  for post in args:
    print(post)
    
###
###OOP
###

class item:
    def __init__(self,name, price):
        self.name = name
        self.price = price
    def __str__(self):                                                  #### __str__ for human-readable OR def __repr__
        return '{},{:.2f}'.format(self.name, self.price)                #### {:.2f} decimal

item = item('hat', 12.40)
print(item)

###



def my_sum(*args):
  sum = 0
  for x in args:
    sum+=n
  return result

my_sum(1,2,5,6,7)

###

def concatenates(**kwargs)                                #kwargs  - for dictionaries
  for values in kwargs.values():
    print value end=' '                  ### OR result = '' and then in the loop result+=values and then print result
    
###

r =  lambda a : a+20                                      # LAMBDA FUNCTION
print(r(10))

y = lambda x,y : x*y
print(y(12,3))

###

def our_convert_function(list1, list2):
  our_dict = dict(zip(list1,list2))
  ### OR our_dict = {list1:list2  for list1,list2 in zip(list1,list2)}               comprehension
  return our_dict




stocks = ["reliance", "infosys", "tcs"]
prices = [2134, 234556, 5567]

print(our_convert_function(stocks,prices))

###
### sum two lists

def sumx(a,b):
  return a+b

list(map(sumx, list1, list2))

##OR

map(lambda x,y : x+y, list1, list2)

###

alpha = ['A','B','C','D','E','F','T','U','V','W','X','Y','Z']
vow = ['A','E','I','O','U']

print(list(filter(lambda x : x in vow, alpha)))

###
def changes_by_one(lst):
    ind = []
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] == 1:
            ind.append(i+1)

    return ind

    #OR
    #return [ind.append(i+1) for i in range(len(lst)-1) if lst[i+1] - lst[i] == 1]
    #OR
    #return [i for i in range(1,len(lst)) if lst[i]==lst[i-1]+1]

x = [1,2,5,5,10,11,12,15,16]
print(changes_by_one(x))

###

def union(lst1,lst2):
    lst3 = lst1 + lst2
    #lst3 = sorted(lst3)
    #print(lst3)
    lst3 = set(lst3)
    return lst3


x = [1,1,2,3,8]
y = [2,3,3,6,10]
print(union(x,y))

###

def print_2d(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j],end = " ")
        print()


L = [[1,2,3],[4,5,6],[7,8,9]]
print(print_2d(L))

###

class Ticket:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time

    def __str__(self):
        return "Ticket cost ("+str(self.cost) + ',' + str(self.time) + ")"

    def is_evening_time(self):
        hour = int(self.time.split(':')[0])
        return 18<=hour<=23

    def bulk_discount(self,n):
        if 5<=n<9:
            return 10
        elif n>=10:
            return 20
        else:
            return 0

ticket = Ticket(49.99,"19:00")
print(ticket)
print(ticket.is_evening_time())
print(ticket.bulk_discount(15))

###

class Ticket:                                                 #PARENT CLASS
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time

    def __str__(self):
        return "Ticket cost ("+str(self.cost) + ',' + str(self.time) + ")"

    def is_evening_time(self):
        hour = int(self.time.split(':')[0])
        return 18<=hour<=23

    def bulk_discount(self,n):
        if 5<=n<9:
            return 10
        elif n>=10:
            return 20
        else:
            return 0

ticket = Ticket(49.99,"19:00")
print(ticket)
print(ticket.is_evening_time())
print(ticket.bulk_discount(15))


class MovieTicket(Ticket):                                        #CHILD CLASS
    def __init__(self,cost,time,movie_name):
        self.cost = cost
        self.time = time
        self.movie_name = movie_name
    def __str__(self):
        return "Ticket ("+str(self.cost)+','+str(self.time)+','+str(self.movie_name)
    def afternoon_discount(self):
        hour = int(self.time.split(':')[0])
        if 12<=hour<=17:
            return 10
        else:
            return 0

m_ticket = MovieTicket(49.99, "14:25", "Snakes on a Plane")
print(m_ticket)
print(m_ticket.afternoon_discount())
print(m_ticket.is_evening_time())

###
#avoid repetition
Ticket.__init__(self,cost,time)

#super method
super().__init__(cost,time)                                         #no need for SELF

###

class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students_IDs = []

    def is_full(self):
        return len(self.students_IDs) > self.capacity

    def add_student(self, x):
        #2 conditions
        if not self.is_full() and x not in self.students_IDs:
            self.students_IDs.append(x)

course = Course("CompScie",3)
course.add_student("123")
course.add_student("123")
course.add_student("456")
course.add_student("789")
course.add_student("999")
print(course.is_full())
print(course.students_IDs)

###

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def compute_area(self, length, width):
        return length * width


rectangle = Rectangle(3,2)
print(rectangle.compute_area(3,2))

###

class NumberToRoman:
    def roman_symbol(self,user_num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]

        i = 0
        roman_num = ''

        while user_num > 0:
            for _ in range(user_num//val[i]):
                roman_num+=syb[i]
                user_num-=val[i]
            i+=i
        return roman_num




print(NumberToRoman().roman_symbol(2549))
