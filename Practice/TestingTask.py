# Online Python - IDE, Editor, Compiler, Interpreter

D = [2, 5]
T = ["PGP", "M"]

def find_first_house(t, houses):
    res = -1
    for i in range(len(houses)):
        if t in houses[i]:
            return i
            break
    return res

max_time = 0

for t in "MGP":
    time = 0
    time_home = 0
    new_T = T.copy()
    new_D = D.copy()
    first_house = find_first_house(t, new_T)
    while first_house != -1:
        time_home += sum(new_D[:first_house+1])
        time += sum(new_D[:first_house+1]) + new_T[first_house].count(t)
        new_D = new_D[first_house+1:]
        new_T = new_T[first_house+1:]
        first_house = find_first_house(t, new_T)
    
    time = time + time_home
    
    if time > max_time:
        max_time = time
        
print(max_time)
