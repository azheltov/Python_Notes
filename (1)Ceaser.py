#Ceaser encryption
msg_for_enc = "Come with me if you want to live" #input("Enter your message: ")
enc_msg = ""
temp = 0
temp2 = 0
given_num = 5 #int(input("choose a number from 1-26"))
for i in msg_for_enc:
    if i == " ":
        enc_msg = enc_msg + " "

    elif i.isupper():
#A-Z have the numbers 65-90 in unicode
        temp = ord(i) + given_num
        if temp > 90:
            temp2 = temp - 90
            temp = 65+temp2
            temp = chr(temp)
            temp = "".join(temp)
            enc_msg += temp
        else:
            temp = chr(temp)
            temp = "".join(temp)
            enc_msg += temp
    else:
# a-z have the numbers 97-122
        temp = ord(i) + given_num
        if temp > 122:
            temp2 = temp - 122
            temp = 97+temp2
            temp = chr(temp)
            temp = "".join(temp)
            enc_msg = enc_msg + temp
        else:
            temp = chr(temp)
            temp = "".join(temp)
            enc_msg = enc_msg + temp
print(enc_msg)
deco = input("Do you want to decode?")
if deco == "yes" or "Yes" or "Y":
     

else:
    print("Goodbye!")












"""
#Convert to Acronym
string_chopper = "Get to the Chopper!"
temp = []
string_chopper = string_chopper.upper()
string_chopper = string_chopper.split()
for i in string_chopper:
    temp.append(i[0][0])
print("".join(temp))

#OR
#for word in string_chopper:
#   print(word[0], end="")
#print()


"""



"""


secret_num = 7
num = int(input("enter number 1-10: "))
while num != secret_num:



    try:
        print(" you didn't guess")
        num = int(input("enter number 1-10: "))



    except ValueError:
        print("it's not a number")

if num == secret_num:
    print("you got it")
"""

"""
while True:
    try:
        number = int(input("Please enter a number: "))
        break

    except ValueError:
        print("It is not a number.")
    except:
        print("what the heck happend?")
print("thank you for entering a number!")
"""

"""
numOfMiles = input("Enter the number of miles: ")
numOfMiles = int(numOfMiles)
numOfKm = numOfMiles * 8.0467
print (numOfKm)
"""
