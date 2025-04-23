def marsExploration(s):
    # Write your code here
    counter = 0
    sos_msg = "SOS"
    
    s_list = [s[i:i+3] for i in range(0, len(s), 3)]
    print(s_list)
    for item in s_list:
        if item != "SOS":
            if item[0]!="S":
                counter+=1
            if item[1]!="O":
                counter+=1
            if item[2]!="S":
                counter+=1
            else:
                continue
    return(counter)
