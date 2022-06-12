for i in range(29, 3, -1):
    print(i, end=" ")
    

    
    
    
    
    
from math import sqrt	
L = []	
for i in range(1, 100):	
	L.append(round(sqrt(i), 4))
print(L)	



# AND, OR, NOT

num = eval(input ("Please enter a number: "))                                 # eval - convert to int
if not (num == 0 or num ==2 or num==5 or 10<num<15 or 20<num<25):
	print("Ok")
else:
	print("Not okay")
	

l = input("Enter prog language: ")
l = l.lower()
if l == "python":
	return "Yes"
	

# l.replace()
# x.isalpha()

# x = 'abc'
# x.index("b")             - gives index of the char

breakpoint = name.index(' ')
first = name.[:breakpoint]
last = name[breakpoint+1:]

###
#1
s = 'The weather is so nice'
print(s[0],end="")
for i in range(len(s)):
    if s[i] == " ":
        print(s[i+1],end="")
	
#2
s = 'The weather is so nice'
z = s.split()
a = []
for i in range(len(z)):
	a.append(z[i][0])

print(a)

# split is based on " "
##

email = 'johndoe@hotmail.com'
breakpoint = email.index("@")
print("User name:", email[:breakpoint], "Domain: ", email[breakpoint+1:])

##
L = blal bla bla numbers
mx = max(L)

for x in L:
	if 10 < x < mx:
		mx = x
print("Smallest thing grater than 10: ", mx)

##
#JOIN concaternates STRRINGs
#JOIN converts list.join(num(list))         JOIN and SEPARATOR

ourList = ['1','2','3']
sep = ','
print(sep.join(ourList))

##

L = [18,25,30]
M = [18,2,30]

##

L = eval(input("Enter a list of integer: "))                             # create an input list 
M = [x+1 for x in L if x%2 == 0]                                         # comprehesion 1) loop 2) if 3) begging
print(M)

##


myList = []
for x in range(len(L)):
	if L[x] > M[x]:
		myList.append(L[x])
	else:
		myList.append(M[x])
print(myList)

##

from random import randint
studentList = []
for s in range(10):
    x = randint(90,100)
    studentList.append(x)
print(studentList)

lucky_index = randint(0,9)
studentList[lucky_index] = 0
print(studnetList)

##

L = ['a','bc','d','e','fg']
I = [4,2]

for i in range(len(I)):
    L.pop(I[i])

print(L)

#OR

L = ['a','bc','d','e','fg']
I = [4,2]

M = []
for x in range(len(L)):
	if x not in I:                         # NOT IN
		M.append(L[x])
print(M)

##

from random import choice
s = ''
for i in range(100):
    s += choice('HT')                         # CHOICE
print(s)

##
						# % probability
letter = 'A'*60 + 'B'*30 + 'C'*8 + 'D'*2
s = []
for i in range(1000):
	s.append(choice(letter))

print(''.join(s))

##

from random import smaple                                  # SAMLE function !!!
from random import sample
c = "python"
indices = []

for i in range(len(c)):
    indices.append(i)

spots = sample(indices,3)
t = ''

for i in range(len(c)):
    if i in spots:
        t += "*"
    else:
        t += c[i]

print(t)

##

myList = []
for i in range(100):
    myList.append(i ** 2)

print(myList)

list_using_compre = [i**2 for i in range(100)]               # COMPREHENSION
print(list_using_compre)

# OR

from math import sqrt
L=[round(sqrt(i),2) for i in range(100)]                     # ROUND        2 decemal
print(L)

##
L = [[1,23],[2,3], [34,78]]
L1 = []
for x in range(len(L)):
    y = L[x]
   L1.append(y[-1])
print(L1)

#OR with comprehension

L = [[1,23],[2,3], [34,78]] 
M = [x[-1] for x in L]
print(M)

##
