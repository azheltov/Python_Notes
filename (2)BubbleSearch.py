#BUBBLE SORT
our_list = [9, 5, 2, 7, 8]
temp = 0

#outer loop decreases
i = len(our_list) - 1
#outer loop
while i > 1:
    j = 0
    #inner loop
    while j < i:
        print("\nIs {} > {}".format(our_list[j], our_list[j+1]))
        print()
        if our_list[j] > our_list[j+1]:
            print("Switch")
            temp = our_list[j]
            our_list[j] = our_list[j+1]
            our_list[j+1] = temp
            #our_list =
        else:
            print("Don't Switch")
        j += 1
        for k in our_list:
            print(k, end="")
        print()
    print("End of Round")
    i -= 1
    for k in our_list:
        print(k, end="")
    print()


"""
"""