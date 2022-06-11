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


