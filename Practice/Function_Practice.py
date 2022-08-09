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


