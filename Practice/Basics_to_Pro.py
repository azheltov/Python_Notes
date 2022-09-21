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


### matrix  [r] [c]
arr = [[0 for i in range(4)] for i in range(4)]                 #empty matrix
for i in range(4): #rows
	for j in range(4): #columns
		arr[i][j] = x
		x += 1
		
sum = 0
for i in range (4):
	for j in range(4):
		sum += arr[j][i]
print("Sum of the column")




###
		
		
		
		
		


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

val = int(input("Please enter a number: "))
print(type(val))
print(val//2)

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

for i in range(200):
    if i%10 != 8:
        print("file",i,".jpg")
    else:
        continue

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


###

inpStr = str(input("Enter course code: "))

result = inpStr.find(" ")
print(result)

if int(inpStr[result:]) < 100 or int(inpStr[result:]) > 499:
    print("Error")
else:
    print("Thanks")

### OR ###

#int(inpStr.split()[1])
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

L = 'helloworld'
k = []
for char in L:
    k.append(char)
s = sorted(k)
print(s)

##

s = "helloworld"
L = [s.count(s.count(c) for c in "abcdefghijklmnopqrstuvwxyz"]
print(L)
	     
	     ##
string1 = "python?"
string2 = "Python!"
L = []
for x in range(len(string1)):
    if string1[x] != string2[x]:
        print("yes",x)
        L.append(x)
print(L)
	     
#comprehesion 
#k = [L.append(x) for x in range(len(string1)) if string1[x] != string2[x]]
#print(L)
	     
	     #OR just
	     #L = [x for x in range(len(string1)) if string1[x] != string2[x]]
	     #print(L)
	     
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[1][2])
for l in nested_list:
    for val in l:
        print(val,end='')

#comprehension
k = [l for l in nested_list]
print(k)

                                        # new line (don forget!)  \n

for i in range(7,9):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')         # print with       f'{}'
	     
#   [i * j for j in range(1,11) for i in range(7,9)] - flat output
#   [[i * j for j in range(1,11)] for i in range(7,9)] - nested list
	     
from random import randint
L = [[randint(0,1) for x in range(10)]for x in range(10)]                 #randint
print(L)
	     
#OR
	     
	    
from random import randint
arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(randint(0,1))

print(arr) 

	     ##                                                 BATTLESHIP
from random import randint
arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(randint(0,1))

r = int(input("Enter two row from 0 to 9: "))
c = int(input("Enter colomn number from 0 - 9: "))

if arr[r][c] == 0:
    print("Missed")
else:
    print("Hit")
	     
	     ##

from random import randint
k =[]
k = [[randint(0, 2) for i in range(6)]for i in range(6)]
print(k)

r1 = eval(input("Enter starting row: "))
r2 = eval(input("Enter ending row: "))
c1 = eval(input("Enter starting col: "))
c2 = eval(input("Enter ending col: "))

total = 0
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        total += k[i][j]

print(total)
	     
	     ##
# 6 x 6 list of integers from 0 to 5
# if there are two consecutive zeros in the list
# horizontally or vertically


from random import randint
k =[]
#k = [[randint(0, 5) for i in range(6)]for i in range(6)]
#print(k)


for i in range(6):
    k.append([])

    for j in range(6):
        k[i].append(randint(0, 5))
    print(k[i],end='\n')

# horizontally
flag = False
for i in range(len(k)):
    for j in range(len(k[i])):
        if k[i][j]==k[i-1][j]==0:
            flag = True


# vertically
for i in range(len(k)):
    for j in range(len(k[i])):
        if k[i][j-1] == k[i][j] == 0:
            flag = True

if flag:
    print("There are consecutive zeros!")
else:
    print("None!")
	     
	     ###
		#bulds up a list
	        #by adding random numbers 1-10 to the list
	        #stopping whenn the fifth 10
	     
from random import randint
count = 0
L = []
while count < 5:
    L.append((randint(1,10)))
    
    if L[-1] == 10:
        count += 1
	     
	     ###
	     
#couple havign kids until boy
#percentage of boys and girls?
#random outcome for a couple (B or G)
#range of 10000 couples


from random import choice

boys = 0
girls = 0

for i in range(10000):
    child = choice("BG")
    while child == "G":
        girls += 1
        child = choice("BG")
    boys += 1

print("Boys", 100 * boys /(boys + girls), "Girls", 100 * girls / (boys + girls))
	     
	     
###
	     # set of 100 items
# 20 items per package are different
# HOW long until collect all 100
# randmly generating packages of 20 and adding them to a collection until the collection has all 100 items


from random import sample
T = [i for i in range(1,101)]
C = []
n = 0
while len(C) != 100:
    P = sample(T,20)                                                     #SAMPLE FUNCTION
    for x in P:
        if x not in C:
            C.append(x)
    n += 1
print(n)
	     
###
	     
# net amount of bank account -
# transaction log is two vars: D and amount, W and amount, " " for exit
# console input
total = 0
while True:
    s = input().split()                                                  #INPUT + SPLIT           split function
    if not s:
        break
    cm, num = map(str, s)                                                 # MAP function

    if cm == "D":
        total += int(num)
    if cm == "W":
        total -= int(num)

print(total)


#    x = ['1','2','3','4']
#    map(int, x)                       # int - it's a function here, x - list

inpStr = str(input("Enter course code: "))

result = inpStr.find(" ")
print(result)

if int(inpStr[result:]) < 100 or int(inpStr[result:]) > 499:
    print("Error")
else:
    print("Thanks")

### OR ###

#int(inpStr.split()[1])
	     
s = input("enter nums separated by semicolon: ")
total = 0
for i in s.split(":"):
    total += int(i)

print(total)
	     
	     ###
	     
	     
	     ### zip function                                               DICTIONARIES
	     keys = ['x','y','z']
	     values = [1, 2, 5]
	     simpDict = dict(zip(keys, values))
	     
	     #unzip
	     result = list(zip(keys, values))
	     
	     keys, values = zip(*result)                                     ### * STAR
	     
	     
	     
	     
str = ['abc', 'bds', 'adsfasdf']
val = [7, 11, 13]
	     
dick = dict(zip(str, val))
print(dick)
print(dick['bds'])
	     
	     dick.keys()                                 #keys
	     list(dick.keys())
	     
	     for k in dick:
	     	print(k,dick[k])
	     
	     if 'abc' in dick:
	     	print('yes')
	     else:
	     	print('no')
	     
	     dick.values()                                 #values
	     
###	     
	     
dict1 = { }
dict2 = { }
dict3 = {**dict1,**dict2}
	     
	     
	     result = 0
	     for i in dict3:
	     	result += dict3[i]
	     print(result)
	     
	     
	     
###
	     
sampleDict = {	     
	'Physics1' : 82,
	'Math1' : 65,
	'History1' : 75
}
sampleDict.get("Math1")                                                       # GET
	     
mx = min(sampleDict)
mx
	     
for i in sampleDict:
	if sampleDict[i]>66:
	     sampleDict.get(i) +  sampleDict[mx]                            # i - is a key
	     
###
	     
sampleDict = {
'emp1' : {'name' : "John", 'salary' : 7500},
'emp2' : {'name' : "Emma", 'salary' : 8000},
'emp3' : {'name' : "Brad", 'salary' : 6500}
}

print(sampleDict)
sampleDict['emp3']['salary'] = 8999
print(sampleDict)  
	     
print('emp2' in sampleDict.keys())
	     
	     ###
	     
dict1 = {'a':1, "b":2, "c":3, "d":4, "e":5}

d = {}
for k,v in dict1.items():
    d[k] = v*2
print(d)
	     
d = {k:v*2 for k,v in dict1.items()}                                    #dict comprehension
print(d)
	     
	     ###
	     
	     new_dict = {n:n**2 for n in range(10) if n%2 == 0}
	     
	     ###
	     
	     
dictTemp = {'t1':-30, "t2":-20, "t3":-10, "t4":0}

Celcius = {}
for k,v in dictTemp.items():
    Celcius[k] = ((v-32)*5)/9
print(Celcius)

Celcius = {k:((v-32)*5)/9 for k,v in dictTemp.items()}
print(Celcius)
	     
	     ###
	     
dictTemp = {'t1':-30, "t2":-20, "t3":-10, "t4":0}

bla = {k:v for k,v in dictTemp.items() if v > -20}
print(bla)
	     
	     ###
	     
#repeatedly ask the user to enter a word
#key:words, valuse: count of vowels
#" " for break
#print dictionary as output
words = {}
vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    word = input('Enter a word : ')
    if word ==' ':
        break
    else:
        words[word] = word

        counter = 0
        for i in range(len(word)):
            #print(word[i])
            if word[i] in vowels:
                counter += 1
                #print(counter)

        words[word] = counter

    print(words)


    # OR
    # words[word] = sum(word.count(c) for c in "aeiou")
	     
###

from random import randint
h = []
for i in range(100):
    h.append(randint(0, 1))
print(h)
for i in range(len(h)):
    if h[i] == 0:
        print("?", end='')
    else:
        print("*", end='')

###
	     

for x in range(1,101):
    print(x)
    if 21*x**2 - x**3 + 21904 == 0:
        print("Bingo! ", x)
	     
###
	     
from random import randint

num1 = randint(20,50)
num2 = randint(20,50)
num3 = randint(20,50)


for i in range(10):
    num1 = randint(20, 50)
    num2 = randint(20, 50)
    num3 = randint(20, 50)
    problem = num1 + num2 + num3
    print(num1,"+", num2,"+", num3, "= ?")

    for x in range(5):
        answer = eval(input("Please provide your answer: "))
        if answer == problem:
            print("Right!")
        elif answer <= problem + 5 and answer >= problem - 5:
            print("Close!")
        else:
            print("Wrong")
	     
###
	     
counter = 0
for i in range(10000):
     fiveDice = []
     for d in range(5):
          dice = randint(1, 6)
          fiveDice.append(dice)
          #print(fiveDice)

     if len(set(fiveDice)) == 1:
          print(fiveDice)
          counter+=1

answer = counter*100/10000
print(answer*100,"%" )
	     
###
	     
p = [2,3,4,6,7,8,9]
l = [str(choice(p)) +'x'  + str(choice(p) for i in range(20)]
				
###
				
d = {"question":"answer", "question":"answer"}
				
from random import shaffle
keys = list(d.keys())
shuffle(keys)
				
for k in keys:
	guess = input(k+ " ")
	if guess.lower() = d[k].lower():
		print("Right")
	else:
		print("Wrong")
