def string_reverse(s):                                             
  i = len(s)
  reverse = ""
  while i > 0:
    reverse += S[i-1]                                                      #reverse String
    i -= 1
  return reverse

s = "string"
print(sting_reverse('string'))
    
###

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
